import os

WSGI_WORKERS = int(os.getenv("WSGI_WORKERS", 0))
if WSGI_WORKERS <= 0:
    from multiprocessing import cpu_count
    WSGI_WORKERS = (cpu_count() * 2) + 1

bind = f"0.0.0.0:{os.getenv('HTTP_PORT', 8009)}"
worker_class = "gthread"
workers = WSGI_WORKERS
threads = 4
timeout = os.getenv("WSGI_TIMEOUT}", 30)
forwarded_allow_ips = "*"
secure_scheme_headers = {
    os.getenv("FORWARDED_PROTO_HEADER_NAME", "X-Forwarded-Proto").upper(): 'https'
}
preload_app = True
keepalive = 60
timeout = 60
worker_tmp_dir = os.getenv("GUNICORN_TMPFS_DIR")