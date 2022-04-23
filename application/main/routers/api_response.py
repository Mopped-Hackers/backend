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
router = APIRouter(prefix='/')
logger = logger_instance.get_logger(__name__)


@router.get('/dummy')
async def getDummyData():
    logger.info('Response Manager')
    data = {
        {"id": '0001c1dd-462e-453c-bac8-2fcdc0b0bc8d',
            "category": 'A', "subCategory": 0, "price": 264.61},
        {"id": '0002278b-67e3-406e-bfc2-63c48c195e2b ',
            "category": 'B', "subCategory": 3, "price": 24.30},
        {"id": '0002c59e-df87-47a8-a27d-26b34340bee5 ',
            "category": 'A', "subCategory": 4, "price": 4.30},
    }
    return data
