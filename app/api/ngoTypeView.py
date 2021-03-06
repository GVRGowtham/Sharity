from flask import request
from app.MethodView import SuperView
import json


class NgoTypeView(SuperView): 
    """ Create Ngo Type service
    """
    method_decorators = []
    _decorators = []

    resource = 'ngoType'
    mask = {}

    def post(self):
      body = request.json
      return self.insert(body)

    def put(self, ngoTypeId):
      body = request.json
      db = self.getConnection()
      db.ngo.update({"ngotypeId" : ngoTypeId}, {"$set" : { "ngotypeId" : body['ngotype']}})
      return self.update(ngoTypeId, body)

    def delete(self, ngoTypeId):
      return self.remove(ngoTypeId)

    def get(self, ngoTypeId):
      return self.retrieve(ngoTypeId)

    def getAll(self):
      return self.retrieveAll()