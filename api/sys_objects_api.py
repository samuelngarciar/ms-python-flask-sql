from flask import jsonify, request, abort
from services.sys_objects_service import SysObjectsService
from utils.input_validation import validate_input
import logging

#simple map
def setup_sys_objects_api(app, sys_objects_service: SysObjectsService):
    logger = logging.getLogger(__name__)
    @app.route('/sysobjects', methods=['GET'])
    def get_sys_objects_api():
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


