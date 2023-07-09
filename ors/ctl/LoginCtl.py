from ctl.BaseCtl import BaseCtl
from flask import Flask, jsonify, request, session
from ctl.AppResult import AppResult

class LoginCtl(BaseCtl):

    userid = "abc@abc.com"
    password ="pass1234"
    message ="Invalid Id and Password"

    def __init__(self):
        self.usecaseid = "Login"
    
    def display(self):
        res = AppResult(True, self.message)
        res.data = { 'userid':self.userid, 'password' : self.password }
        print('this is display method')  
        return res  

    def submit(self):
        res = AppResult(True, "This is Post")
        res.data = { 'id':1, 'name' :  self.name }
        print('this is submit method' + self.name)
        return res          
    
    def logout(self):
        #session['usercontext'] = 'abc'
        res = AppResult(True, "user is logout")
        return res          
        