from peewee import *

db = SqliteDatabase("postagens.db")

class Postagem(Model):
    titulo = CharField()
    texto = TextField()
    topico = CharField()

    class Meta:
        database = db
      
