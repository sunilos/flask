# Import necessary modules from Flask
from flask import Flask, jsonify, request
# Import ABC (Abstract Base Class) and abstractmethod for defining abstract methods
from abc import ABC, abstractmethod

# Define a base controller class
class BaseCtl:
    # Class-level attributes for use case ID and object ID
    usecaseid = 0
    id = 0

    # Method to set the ID of an instance
    def setId(self, id):
        self.id = id

    # Method to execute based on the HTTP request method
    def execute(self):
        if request.method == 'GET':  # If the request is GET, call display method
            return self.display()
        if request.method == 'POST':  # If the request is POST, call submit method
            return self.submit()

    # Abstract method to be implemented in subclasses for handling GET requests
    @abstractmethod    
    def display(self):
        pass    

    # Abstract method to be implemented in subclasses for handling POST requests
    @abstractmethod
    def submit(self):
        pass

    # Method to convert object properties to a dictionary (but the values are incorrect as they are strings)
    def to_dict(self):
        return {
            'name': 'self.name',  # This should be self.name without quotes
            'age': 'self.age'  # This should be self.age without quotes
        }
