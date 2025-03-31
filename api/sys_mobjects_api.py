from flask import jsonify, request, abort
from services.sys_objects_service import SysObjectsService
from utils.input_validation import validate_input
import logging

#map with model class
def setup_sys_objects_with_model_api(app, sys_objects_service: SysObjectsService):
    logger = logging.getLogger(__name__)
    @app.route('/msysobjects', methods=['GET'])
    def get_sys_objects_api_model():
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
