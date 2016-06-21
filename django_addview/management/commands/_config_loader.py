import os
import sys
import django
from django.conf import settings
import logging
try:
    # Python2
    from StringIO import StringIO
except ImportError:
    # Python3
    from io import StringIO
tmp_logs = StringIO()

logger = logging.getLogger('addview')
#hdlr = logging.FileHandler('addview.log')
hdlr2 = logging.StreamHandler(tmp_logs)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
#hdlr.setFormatter(formatter)
hdlr2.setFormatter(formatter)
#logger.addHandler(hdlr)
logger.addHandler(hdlr2)
logger.setLevel(logging.INFO)

PROJ_ROOT = os.path.dirname(os.path.realpath(django.__file__))

config = {
    'local_template_dir': os.path.join('{app_path}', 'templates'),
    'global_template_dir': getattr(settings, 'ADDVIEW_GLOBAL_TEMPLATE_DIR', None)
}
