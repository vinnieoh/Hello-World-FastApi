from fastapi import APIRouter


from .v1_endpoits import usuario_routes


api_router = APIRouter()


api_router.include_router(usuario_routes.router, prefix='/usuarios', tags=['usuarios'])