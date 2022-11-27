from models.models import Pedanter, getDBinstance
from peewee import *

class PedanterRepository:
    def __init__(self):
        pass

    def createPedanter(self, username, slackId):
        peda = Pedanter()

        peda.name = username
        peda.slackId = slackId

        peda.save()
    
    def getPedanters():
        pass
    
    def getPedanters():
        pass
    
    def getPedanters():
        pass