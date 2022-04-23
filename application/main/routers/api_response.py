from typing import List
from typing import Optional

from fastapi.routing import APIRouter
from pydantic import BaseModel

from application.initializer import (db_instance, logger_instance)


class SearchAnswerResponse(BaseModel):
    key1: Optional[float] = None
    key2: Optional[str] = None
    key3: Optional[int] = None


_db = db_instance
router = APIRouter()
logger = logger_instance.get_logger(__name__)


@router.get('/dummy')
async def getDummyData():
    logger.info('Response Manager')
    data = [
        {"id": '0001c1dd-462e-453c-bac8-2fcdc0b0bc8d',
            "category": 'A', "subCategory": 0, "price": 264.61},
        {"id": '0002278b-67e3-406e-bfc2-63c48c195e2b ',
            "category": 'B', "subCategory": 3, "price": 24.30},
        {"id": '0002c59e-df87-47a8-a27d-26b34340bee5 ',
            "category": 'A', "subCategory": 4, "price": 4.30},
        {"id": '000bb6cd-b68d-4d77-8874-c23fbc3b01f9 ',
            "category": 'A', "subCategory": 4, "price": 4.30},
        {"id": '00118113-868f-4dfd-bb55-ee66faf87f97 ',
            "category": 'A', "subCategory": 4, "price": 4.30},
       # {"id": '000e4090-9644-4faf-b6fd-781fc598ec34 ',
        #    "category": 'A', "subCategory": 4, "price": 4.30},
        #{"id": '000e4e01-47ad-4c5b-b3d8-b1b50b70dbc3 ',
         #   "category": 'A', "subCategory": 4, "price": 4.30},
        #{"id": '000e9fc6-2e74-4c7b-8a4b-00f847b5e301 ',
         #   "category": 'A', "subCategory": 4, "price": 4.30},
        #{"id": '000ed492-bd09-40d3-91a3-633ac79f32fe ',
         #   "category": 'A', "subCategory": 4, "price": 4.30},
        #{"id": '000f27eb-78b7-4166-9d8e-aba8721d00f3 ',
         #   "category": 'A', "subCategory": 4, "price": 4.30},
    ]
    return data
