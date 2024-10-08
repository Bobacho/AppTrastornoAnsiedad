from utils.db import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class tbRecomendApoyo(db.Model):
    __tablename__ = 'tbRecomendApoyo'
    idRecomendApoyo: int 
    idEspecialista: int
    idResultadoTest: int
    descripRecomendApoyo: str
    fechaRecomendApoyo: datetime
    nivelAnsiedadRevision: str

    idRecomendApoyo = db.Column(db.Integer, primary_key=True)
    idEspecialista = db.Column(db.Integer, db.ForeignKey('tbEspecialista.idEspecialista'))
    idResultadoTest = db.Column(db.Integer, db.ForeignKey('tbResultadoTest.idResultadoTest'))
    descripRecomendApoyo = db.Column(db.String(500))
    fechaRecomendApoyo = db.Column(db.DateTime)
    nivelAnsiedadRevision = db.Column(db.String(255))

    def __init__(self, idEspecialista, idResultadoTest, descripRecomendApoyo, fechaRecomendApoyo, nivelAnsiedadRevision):
        self.idEspecialista = idEspecialista
        self.idResultadoTest = idResultadoTest
        self.descripRecomendApoyo = descripRecomendApoyo
        self.fechaRecomendApoyo = fechaRecomendApoyo
        self.nivelAnsiedadRevision = nivelAnsiedadRevision