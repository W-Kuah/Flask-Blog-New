
from flask import render_template

#  Connexion module (imported from config.py) allows a Python program to use the OpenAPI specification with Swagger
import config
from models import Person
# The OpenAPI Specification is an API description format for REST APIs and provides a lot of functionality:
## Validation of input and output data to and from your API
## Configuration of the API URL endpoints and the expected parameters



# Initiate flask app

## Create the application instance using Connexion rather than Flask
## The Flask app is still created, but it now has additional functionality added to it.
app = config.connex_app
## Reference swagger.yml in your app.py file, 
## which will connect the API configuration file with the Flask app
app.add_api(config.basedir / "swagger.yml")

## define URL route 
@app.route("/")

## define home URL
def home():
    ### Query the Person model to get all the data from the person table
    people = Person.query.all()
    ### Pass this data on to render_template()
    return render_template("home.html", people=people)

## Run app from port 8000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

