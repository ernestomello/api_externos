#!/usr/bin/python 
import site
import sys 
import site
import logging 
logging.basicConfig(stream=sys.stderr) 
#site.addsitedir('/var/www/hitme/lib/python3.6/site-packages')
sys.path.insert(0,'/home/ernesto/Escritorio/api_externos/') 
sys.path.insert(0,'/home/ernesto/Escritorio/api_externos/venv/lib/python3.6/site_packages') 
                    
from cobranza import app as application 
application.secret_key = 'Todos somos buenos'