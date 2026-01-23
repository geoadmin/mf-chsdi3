from os import getenv

from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.pyramid import PyramidInstrumentor
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor


def strtobool(value: str) -> bool:
    """Convert a string representation of truth to true (1) or false (0).
    True values are 'y', 'yes', 't', 'true', 'on', and '1'; false values
    are 'n', 'no', 'f', 'false', 'off', and '0'.  Raises ValueError if
    'val' is anything else.
    """
    value = value.lower()
    if value in ('y', 'yes', 't', 'true', 'on', '1'):
        return True
    if value in ('n', 'no', 'f', 'false', 'off', '0'):
        return False
    raise ValueError(f"invalid truth value \'{value}\'")


def instrument_pyramid(config):
    """Instrument Pyramid with OpenTelemetry.

    This must be called after creating the Configurator but before adding routes/views.
    Unlike other instrumentors, Pyramid instrumentation requires the config object.

    Args:
        config: The Pyramid Configurator instance
    """

    tracing_enabled = not strtobool(getenv("OTEL_SDK_DISABLED", "false"))
    if tracing_enabled:
        import logging
        logger = logging.getLogger(__name__)
        _setup_trace_provider()
        PyramidInstrumentor().instrument_config(config)
        logger.info("OTEL Bootstrap - Pyramid instrumented")
        _initialize_tracing()


def _initialize_tracing() -> bool:
    if strtobool(getenv("OTEL_ENABLE_SQLALCHEMY", "false")):
        SQLAlchemyInstrumentor().instrument()
    if strtobool(getenv("OTEL_ENABLE_REQUESTS", "false")):
        RequestsInstrumentor().instrument()


def _setup_trace_provider() -> None:
    tracing_enabled = not strtobool(getenv("OTEL_SDK_DISABLED", "false"))
    if tracing_enabled:
        # Since we created a new tracer, the default span processor is gone. We need to
        # create a new one using the default OTEL env variables and ad it to the tracer.
        span_processor = BatchSpanProcessor(
            OTLPSpanExporter(
                endpoint=getenv('OTEL_EXPORTER_OTLP_ENDPOINT', "http://localhost:4317"),
                headers=getenv('OTEL_EXPORTER_OTLP_HEADERS'),
                insecure=strtobool(getenv('OTEL_EXPORTER_OTLP_INSECURE', "false"))
            )
        )

        provider = TracerProvider(resource=Resource.create())
        provider.add_span_processor(span_processor)
        trace.set_tracer_provider(provider)
