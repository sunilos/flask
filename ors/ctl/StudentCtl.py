from ctl.BaseCtl import BaseCtl
from flask import Flask, jsonify, request
from ctl.AppResult import AppResult

class StudentCtl(BaseCtl):

    firstName = "Ram"
    lastName = "KUmar"

    def __init__(self):
        self.usecaseid = "StudentCtl"

    def display(self):

        res = AppResult(True, self.firstName)

        if(self.id >0):
            res.data = { 'firstName':'Shyam Kumar', 'lastName' : 'Sharma' }
            print('get the data for id',self.id)

        if(self.id < 1 ):
            res.data = { 'firstName':self.firstName, 'lastName' : self.lastName }
            print('get the data for id',self.id)
        print('this is display method')  
        return res  

    def submit(self):
        data = request.get_json()
        res = AppResult(True, self.firstName)
        res.data = { 'firstName':self.firstName, 'lastName' : self.lastName }
        print('this is submit method', data )
        return res          
    
    def search(self):
        data = request.get_json()
        res = AppResult(True, 'This is search method')
        res.data = { 'firstName':self.firstName, 'lastName' : self.lastName }
        return res          
    
    def list(self):
        data = request.get_json()
        res = AppResult(True, 'This is list method')
        res.data = { 'firstName':self.firstName, 'lastName' : self.lastName }
        return res          
        