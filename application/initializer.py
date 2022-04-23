class LoggerInstance(object):
    def __new__(cls):
        from application.main.utility.logger.custom_logging import LogHandler
        return LogHandler()


class IncludeAPIRouter(object):
    def __new__(cls):
        from application.main.routers.api_response import router as recommendator
        from fastapi.routing import APIRouter
        router = APIRouter()
        router.include_router(recommendator, prefix='/api/v1', tags=['recommendation'])
        return router


class DataBaseInstance(object):
    def __new__(cls):
        from application.main.infrastructure.database import db
        return db.DataBase()


# instance creation
logger_instance = LoggerInstance()
db_instance = DataBaseInstance()
