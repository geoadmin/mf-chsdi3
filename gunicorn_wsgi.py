# from gevent import monkey
# monkey.patch_all()  # noqa: E402

from eventlet import monkey_patch
monkey_patch() # noqa: E402

# from gunicorn.app.wsgiapp import WSGIApplication

def run():
    """\
    The ``gunicorn`` command line runner for launching Gunicorn with
    generic WSGI applications.
    """
    from gunicorn.app.wsgiapp import WSGIApplication
    WSGIApplication("%(prog)s [OPTIONS] [APP_MODULE]").run()


if __name__ == '__main__':
    run()