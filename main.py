from fastapi import FastAPI

from config.configs import settings
from router.api_config import api_router


app = FastAPI(title='Curso API - Segurança')
app.include_router(api_router, prefix=settings.API_V1_STR)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level='info', reload=True)

# URL: http://127.0.0.1:8000/api/v1/usuarios/