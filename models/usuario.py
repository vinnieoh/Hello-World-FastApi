from sqlalchemy import Integer, String, Column

from config.configs import settings


class UsuarioModel(settings.DBBaseModel):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    
    email = Column(String(256), index=True, nullable=False, unique=True)
    senha = Column(String(256), nullable=False)

    