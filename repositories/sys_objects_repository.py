import pyodbc
import logging
from typing import List, Dict
from models.sys_objects_model import SysObjectsModel

logger = logging.getLogger(__name__)

class SysObjectsRepository:
    def __init__(self, connection_string: str):
        self.connection_string = connection_string

    def _get_connection(self):
        return pyodbc.connect(self.connection_string)
  
   #simple map
    def get_sys_objects(self, limit: int = 10, offset: int = 0) -> List[Dict]:
        logger.info("get_sys_objects begin")
        logger.info(f"offset={offset}, limit={limit}")

        try:
            with self._get_connection() as conn:
                with conn.cursor() as cursor:
                    sql = f"""
                        SELECT object_id, name, type_desc  
                        FROM sys.objects 
                        ORDER BY object_id
                        OFFSET ? ROWS
                        FETCH NEXT ? ROWS ONLY;
                    """
                    cursor.execute(sql, offset, limit)
                    columns = [column[0] for column in cursor.description]
                    results = [dict(zip(columns, row)) for row in cursor.fetchall()]
                    return results
        except pyodbc.Error as ex:
            logger.error(f"Database error: {ex}")
            return []

    #map with model class
    def get_sys_objects_with_model(self, limit: int = 10, offset: int = 0) -> List[SysObjectsModel]:
        logger.info("get_sys_objects_with_models begin")
        logger.info(f"offset={offset}, limit={limit}")
        try:
            with self._get_connection() as conn:
                with conn.cursor() as cursor:
                    sql = f"""
                        SELECT object_id, name, type_desc  
                        FROM sys.objects 
                        ORDER BY object_id
                        OFFSET ? ROWS
                        FETCH NEXT ? ROWS ONLY;
                    """
                    cursor.execute(sql, offset, limit)

                    sysObjectsMoldelList = []
                    for row in cursor.fetchall():
                        sysObjectsMoldelList.append(SysObjectsModel(*row)) 
                    return sysObjectsMoldelList
        except pyodbc.Error as ex:
            logger.error(f"Database error: {ex}")
            return []
