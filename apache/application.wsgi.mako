

from pyramid.paster import get_app, setup_logging
ini_path = "${current_directory}/${modwsgi_config}" #use a full path cause it will be runned from apache directory
setup_logging(ini_path)
application = get_app(ini_path, 'main')
