from ctl.BaseCtl import BaseCtl
from flask import Flask, jsonify, request
from ctl.AppResult import AppResult

class UserRegCtl(BaseCtl):

    userName = ""
    emailId =""
    password = ""

    def __init__(self):
        self.usecaseid = "UserRegCtl"

    def display(self):
        print('this is userreg display')
        if(self.id >0):
            print('get the data for id',self.id)
        res = AppResult(True, "no messsage")
        res.data = { 'userName':self.userName, 'emailId' : self.emailId, 'password' : self.password}
        return res  

    def submit(self):
        print('this is userreg submit')
        data = request.get_json()
        print('------data >', data)
        res = AppResult(True, "Data is saved")
        res.data = { 'userName':self.userName, 'emailId' : self.emailId, 'password' : self.password}
        return res          
    
    def search(self):
        data = request.get_json()
        res = AppResult(True, 'This is search method')
        res.data = { 'userName':self.userName, 'emailId' : self.emailId, 'password' : self.password}
        return res          
    