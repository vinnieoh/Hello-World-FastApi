from typing import Optional

from pydantic import BaseModel, EmailStr


class UsuarioSchemaBase(BaseModel):
    id: Optional[int] = None

    email: EmailStr

    class Config:
        orm_mode = True


class UsuarioSchemaCreate(UsuarioSchemaBase):
    senha: str


class UsuarioSchemaUp(UsuarioSchemaBase):
    email: Optional[EmailStr]
    senha: Optional[str]