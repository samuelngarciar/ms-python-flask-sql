from flask import jsonify, request, abort
import logging
import bcrypt

from services.sys_objects_service import SysObjectsService
from utils.input_validation import validate_input

logger = logging.getLogger(__name__)


def authenticate(username, password, app):
    logger.info("authenticate")
   
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    secretKey = app.config['SECRET_KEY']    
    if username == "test" and bcrypt.checkpw(secretKey.encode(), hashed_password):
        return True
    return False


def setup_auth_sys_objects_api(app, sys_objects_service: SysObjectsService):
    @app.route('/protected/sysobjects', methods=['GET'])
    def protected_sysobjects():
        auth = request.authorization
        if not auth or not authenticate(auth.username, auth.password, app):
            return jsonify({"message": "Authentication required"}), 401, {'WWW-Authenticate': 'Basic realm="Login Required"'}
        try:
            limit = request.args.get('limit', default=10, type=int)
            offset = request.args.get('offset', default=0, type=int)
            validate_input(limit)
            validate_input(offset)
        except ValueError as e:
            logger.error(f'Validation failed - {str(e)}')
            abort(400, description=str(e))

        sysobjects = sys_objects_service.get_sys_objects(limit, offset)
        return jsonify(sysobjects)

def setup_auth_sys_objects_with_model_api(app, sys_objects_service: SysObjectsService):
    @app.route('/protected/msysobjects', methods=['GET'])
    def protected_msysobjects():
        auth = request.authorization
        if not auth or not authenticate(auth.username, auth.password, app):
            return jsonify({"message": "Authentication required"}), 401, {'WWW-Authenticate': 'Basic realm="Login Required"'}
        try:
            limit = request.args.get('limit', default=10, type=int)
            offset = request.args.get('offset', default=0, type=int)
            validate_input(limit)
            validate_input(offset)
        except ValueError as e:
            logger.error(f'Validation failed - {str(e)}')
            abort(400, description=str(e))

        sysObjectsModelList: List[SysObjectsModel] = sys_objects_service.get_sys_tables_with_model(limit, offset)
        final_sysObjectsModelList = [{"object_id": c.object_id, "name": c.name, "type_desc": c.type_desc} for c in sysObjectsModelList]
        return jsonify(final_sysObjectsModelList)
