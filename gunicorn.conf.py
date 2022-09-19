import os

bind = f"0.0.0.0:{os.getenv('HTTP_PORT', 8009)}"
worker_class = "gevent"
workers = os.getenv("WSGI_WORKERS", 0)
timeout = os.getenv("WSGI_TIMEOUT}", 30)
forwarded_allow_ips = "*"
secure_scheme_headers = {
    os.getenv("FORWARDED_PROTO_HEADER_NAME", "X-Forwarded-Proto").upper(): 'https'
}