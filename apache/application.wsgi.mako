import ConfigParser
import sys

activate_this = "${current_directory}/.venv/bin/activate_this.py"
execfile(activate_this, dict(__file__=activate_this))

from paste.deploy import loadapp

if sys.version_info >= (2, 6):
    from logging.config import fileConfig
else:
    from paste.script.util.logging_config import fileConfig

configfile = "${current_directory}/${modwsgi_config}"
try:
    fileConfig(configfile)
except:
    pass

application = loadapp("config:" + configfile, name=None)
