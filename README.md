---------------------------------------------
What:
---------------------------------------------
This project is REST API that keeps track of notes from different people.

This project was made to demonstrate understanding of...
    - Handling relationships using SQLAlchemy
    - Working with multiple tables within a database
    - Utilizing Marshmallow to serialize data
    - Using nested schemas with Marshmallow
    - Delivering SQL commands in a pythonic way
    - Using Swagger UI to build API documentation
    - Managing HTTP requests with Connexion
    - Utilizing the flask library to build a REST API 

---------------------------------------------
Why is this useful:
---------------------------------------------
This enables users to utilise a digital sticky board whereby users can write announcements and reminders for themselves and others.

---------------------------------------------
How to get started:
---------------------------------------------
1. Create and start virtual environment:

```console
$ python -m venv venv
$ source venv/bin/activate
```

2. Install the modules from 'requirements.txt':
```console
$ python -m pip install -r requirements.txt
```

2a. (Optional) Initiate/restart database:
```console
$ python build_database.py
```

3. Start Flask App:
```console
$ python app.py
```

4. Explore:
Homepage link: `http://127.0.0.1:8000`
Swagger UI API documentation link: `http://127.0.0.1:8000/api/ui`
User list link: `http://127.0.0.1:8000/api/people`
Notes list link: `http://127.0.0.1:8000/api/notes`


---------------------------------------------
Where to get help:
---------------------------------------------



---------------------------------------------
Maintainers and Contributors:
---------------------------------------------
Author: Warren Kuah
Backend Foundations: Philipp Acsany
    - https://realpython.com/flask-connexion-rest-api-part-3/
Frontend Advice: Richard Pienaar