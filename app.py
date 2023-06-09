# Importing the Flask class
from flask import Flask
# Importing the json module for JSON serialization
import json
# Importing the dbhelper module
import dbhelper
# Creating a Flask application instance
app=Flask(__name__)
# Route decorator for handling GET requests to '/animals'
@app.get('/animals')
# Create a connection funtion
def get_animals():
     # Call the 'get_animals()' procedure from the 'dbhelper' module and store the result in a variable
    results = dbhelper.run_procedure('CAll get_animals()',[])
      # Checking if the results are of type list
    if(type(results)==list):
        # And if so convert the 'results' list to a JSON string using json.dumps function
        animals_json= json.dumps(results,default=str)
        # Return the animals JSON string
        return animals_json
     # Else return an error message
    else:
        return 'sorry please try again'
 # Route decorator for handling GET requests to '/dogs'
@app.get('/dogs')  
# Create a connection funtion
def get_dogs():
    # Call the 'get_only_dogs()' procedure from the 'dbhelper' module
    results = dbhelper.run_procedure('CAll get_only_dogs()',[])
        # Checking if the results are of type list
    if(type(results)==list):
           # And if so convert the 'results' list to a JSON string
        dogs_json= json.dumps(results,default=str)
         # Return the dogs JSON string
        return dogs_json
     # Else return an error message
    else:
        return 'sorry please try again'
    

@app.get('/cats')  
# Create a connection funtion
def get_cats():
     # Call the 'get_only_cats()' procedure from the 'dbhelper' module
    results = dbhelper.run_procedure('CAll get_only_cats()',[])
    # Checking if the results are of type list
    if(type(results)==list):
        # And if so convert the 'results' list to a JSON string
        cats_json= json.dumps(results,default=str)
         # Return the catss JSON string
        return cats_json
     # Else return an error message
    else:
        return 'sorry please try again'
    # Run the Flask application in debug mode
app.run(debug=True)
