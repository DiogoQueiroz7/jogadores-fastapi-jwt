from sqlalchemy import Column, Integer, String
from database import Base


class Jogador(Base):
    __tablename__ = "jogadores"

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    posicao = Column(String)

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    senha_hash = Column(String, nullable=False)