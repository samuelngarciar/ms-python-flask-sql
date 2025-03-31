#base imports
from flask import Flask
import logging
import secrets
import os

#apis imports
from api.sys_objects_api import setup_sys_objects_api
from api.sys_mobjects_api import setup_sys_objects_with_model_api
from api.health_api import setup_health_api
from api.auth_api import setup_auth_sys_objects_api
from api.auth_api import setup_auth_sys_objects_with_model_api

#services imports
from services.sys_objects_service import SysObjectsService

#repositories import
from repositories.sys_objects_repository import SysObjectsRepository

#main settings
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)


#settings connection
SERVER = os.popen('hostname -i').read().strip()
DATABASE = 'master'
USERNAME = 'sa'
PASSWORD = 'YourPassword01-'
DRIVER = '{ODBC Driver 17 for SQL Server}'
SECRET_KEY = 'password'
app.config['SECRET_KEY'] = SECRET_KEY

logger.info(f"Connection to the DB Server IP: {SERVER}")
connection_string = f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'

#repositories
sys_objects_repository = SysObjectsRepository(connection_string)

#services
sys_objects_service = SysObjectsService(sys_objects_repository)

#api
setup_sys_objects_api(app, sys_objects_service)
setup_sys_objects_with_model_api(app, sys_objects_service)

#api secure version
setup_auth_sys_objects_api(app, sys_objects_service)
setup_auth_sys_objects_with_model_api(app, sys_objects_service)

#health check
setup_health_api(app)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
