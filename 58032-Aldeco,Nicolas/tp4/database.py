from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import func
Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    tipo_de_usuario = Column(String)
    lista_de_act = Column(String)
    actividad = Column(Integer, ForeignKey('actividad.id'))


class Actividad(Base):
    __tablename__ = "actividad"
    id = Column(Integer, primary_key=True)
    tipo_de_mensaje = Column(String)
    tipo = Column(String)
    resultado = Column(Boolean)
    descripcion = Column(Text)
    fecha_de_creacion = Column(DateTime(timezone=True), server_default=func.now())
    persona_vinculada = relationship('User', backref='actividad')


class TipoActividad(Base):
    __tablename__ = 'tipo_actividad'
    id = Column(Integer, primary_key=True)
    tipo = Column(String)
    descripcion = Column(Text)


if __name__ == "__main__":
    engine = create_engine('sqlite:///mydatabase.db', echo=True)
    Base.metadata.create_all(bind=engine)
