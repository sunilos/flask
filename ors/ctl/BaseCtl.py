from flask import Flask, jsonify, request
from abc import ABC, abstractmethod

class BaseCtl:

    usecaseid = 0
    id = 0
    def setId(self, id):
        self.id = id

    def execute(self):
        if(request.method == 'GET'):
            return self.display()
        if(request.method == 'POST'):
            return self.submit()
    @abstractmethod    
    def display(self):
        pass    

    @abstractmethod
    def submit(self):
        pass

    def to_dict(self):
        return {
            'name': 'self.name',
            'age': 'self.age'
        }
