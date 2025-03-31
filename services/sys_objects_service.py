from repositories.sys_objects_repository import SysObjectsRepository
from typing import List, Dict
from models.sys_objects_model import SysObjectsModel

class SysObjectsService:
    def __init__(self, repository: SysObjectsRepository):
        self.repository = repository
    
    #simple map
    def get_sys_objects(self, limit: int = 10, offset: int = 0) -> List[Dict]:
        sysobjects = self.repository.get_sys_objects(limit, offset)
        return sysobjects

    #map with model class
    def get_sys_tables_with_model(self, limit: int = 10, offset: int = 0) -> List[SysObjectsModel]:
        sysObjectsModelList = self.repository.get_sys_objects_with_model(limit, offset)
        return sysObjectsModelList
