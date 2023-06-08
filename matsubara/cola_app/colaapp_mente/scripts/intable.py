import sys
from colaapp_mente import db
from sqlalchemy import Column,String,Date,Integer,DateTime,DECIMAL,VARCHAR


#from datetime import datetime

class Colakind(db.Model):
    __tablename__ = 'colakind'
    cola_id = db.Column('cola_id', db.Integer, primary_key = True)
    cola_name = db.Column('cola_name', db.VARCHAR(20))
    cola_text = db.Column('cola_text', db.String(20))
    cola_taste = db.Column('cola_taste', db.Integer)    

    def __init__(self, cola_id=None, cola_name=None, cola_text=None, cola_taste=None):
        self.cola_id = cola_id
        self.cola_name = cola_name
        self.cola_text = cola_text
        self.cola_taste = cola_taste

    def __repr__(self):
        return '<cola_id:{} cola_name:{} cola_text:{} cola_taste:{}>'.format(self.cola_id, self.cola_name,self.cola_text,self.cola_taste)
    
