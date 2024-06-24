import os
import glob

APP_NAME = 'TEST'

BASE_DIR = os.path.dirname(p=__file__)

COMMENT_VIEW = False
VARIABLE_VIEW = True

NOTIFICATIONS = [template.replace(BASE_DIR + '/notifications/', '') for template in glob.glob(BASE_DIR + '/notifications/*.json')]
TEMPLATES = [template.replace(BASE_DIR + '/templates/', '') for template in glob.glob(BASE_DIR + '/templates/*.html')]