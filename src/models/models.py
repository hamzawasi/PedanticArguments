import datetime
import logging
import os
from pathlib import Path
from dotenv import load_dotenv
from peewee import *

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

db_name = os.environ["DATABASE"]

db = SqliteDatabase(db_name)

def init_db():
    try:
        db_tables = db.get_tables()
        if len(db_tables) == 0:
            with db:
                db.create_tables([Pedanter, PedanticArgument], safe = True)
    except BaseException as exc:
        logging.exception(exc)

def getDBinstance():
    try:
        return db
    except BaseException as exc:
        logging.exception(exc)


class BaseModel(Model):
    class Meta:
        database = db


class Pedanter(BaseModel):
    id = AutoField(primary_key = True)
    name = CharField(unique = True)
    slackId = CharField(unique = True, null = True)
    createdAt = DateTimeField(default = datetime.datetime.now)
    updatedAt = DateTimeField(null = True)
    deletedAt = DateTimeField(null = True)

Pedanter.add_index(SQL('CREATE INDEX idx_pedanter ON PEDANTER(id, name)'))


class PedanticArgument(BaseModel):
    id = AutoField(primary_key = True)
    pedanterId = IntegerField()
    currentStreakCount = IntegerField(default = 0)
    reason = CharField()
    createdAt = DateTimeField(default = datetime.datetime.now)
    updatedAt = DateTimeField(null = True)
    deletedAt = DateTimeField(null = True)

PedanticArgument.add_index(SQL('CREATE INDEX idx_pedanterargument ON PedanticArgument(id, pedanterId)'))