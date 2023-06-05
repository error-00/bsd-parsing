import sys
import os
import django

sys.path.append('D:/2 Projects/work/1/pars/pars_project')
os.environ['DJANGO_SETTINGS_MODULE'] = 'pars_project.settings'
django.setup()