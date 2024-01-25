from sqlalchemy import Integer, String, Column, Boolean
from sqlalchemy.orm import relationship

from core.configs import settings

class UsuarioModel(settings.DBBaseModel):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(256), nullable=True)
    sobrenome = Column(String(256), nullable=True)
    senha = Column(String(256), nullable=False)
    email = Column(String(256), index=True, nullable=False, unique=True)
    eh_admin = Column(Boolean, default=False)
    artigos = relationship("ArtigoModel", cascade="all,delete-orphan", uselist=True, lazy="joined") 