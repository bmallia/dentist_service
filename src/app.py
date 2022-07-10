
import logging
import logging.config
import time
import json

from fastapi import FastAPI, Request, Response
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from http import HTTPStatus

from pydantic.error_wrappers import ErrorWrapper
from pydantic import ValidationError
##from pydantic import BaseSettings

from src.config import get_settings
from src.api import company
from src.database.setup_database import setup
from src.exceptions import HTTPError


config = get_settings()


logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

logger = logging.getLogger(__name__)
logger_service = logging.getLogger("serviceInfo")


def create_application() -> FastAPI:
    """Cria uma configuração para o fastapi adicionando uma rota

        return: objeto FastAPI
    """
    application = FastAPI(docs_url="/dentist-service/docs")
    application.include_router(
        company.router,
        tags=['Company registration'],
        prefix="/company"
    )
    application.include_router(
        company.router,
        tags=['Address registration'],
        prefix="/address"
    )
    return application


app = create_application()


@app.on_event("startup")
async def startup_event():
    logger.info("Initializing database and application ...")
    setup()
    logger.info('Application initiliazed sucessffuly!')


# class Settings(BaseSettings):
##    openapi_url: str = "/openapi.json"


@app.middleware('http')
async def log_request(request: Request, call_next):
    '''middleware function'''
    start_time = time.time()
    response = await call_next(request)

    extra = {'duration': round(time.time() - start_time, 2), 'host': request.client.host,
             'method': request.method, 'status': response.status_code}
    logger = logging.LoggerAdapter(logger_service, extra)

    binary = b''
    async for data in response.body_iterator:
        binary += data

    body = binary.decode()
    logger.info(body)

    return Response(content=body,
                    status_code=response.status_code,
                    headers=dict(response.headers),
                    media_type=response.media_type
                    )


@app.exception_handler(HTTPError)
async def error_exception_handler(request: Request, exc: HTTPError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": f"{exc.message}"},
    )


@app.exception_handler(RequestValidationError)
async def http__validation_exception_accept_handler(request: Request, exc: RequestValidationError) -> Response:
    """
        Handler to custumize eror msg when raise validationError

        @request (Request): Request from service
        @exec (RequestValidationError) : the error's stack from fastapi
    """
    raw_errors = exc.raw_errors
    error_wrapper: ErrorWrapper = raw_errors[0]
    validation_error: ValidationError = error_wrapper.exc
    overwritten_errors = validation_error.errors()
    json_error = {e['loc'][0]: f"[{e['msg']}]" for e in overwritten_errors}
    dict_error = json.dumps(json_error)
    logger.error('Erro na validacao do modelo da request: %s', dict_error)
    return JSONResponse(status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
                        content={"erros": dict_error})
