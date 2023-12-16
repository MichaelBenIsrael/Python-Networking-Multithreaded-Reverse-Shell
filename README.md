# Python-Networking-Reverse-Shell

A reverse shell is a shell that is running on one computer but accepts requests and relays the responses to another computer.
So it acts on behalf of another computer remotely.
![image](https://github.com/MichaelBenIsrael/Python-Networking-Reverse-Shell/assets/73841983/ec7887c4-474d-44bf-b7c8-04f0699e937c)



### Dependencies

* [Python](https://www.python.org/) - Programming Language
* [Flask](https://flask.palletsprojects.com/) - The framework used
* [SQLAlchemy](https://docs.sqlalchemy.org/) - ORM
* [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation
* [Alembic](https://alembic.sqlalchemy.org/) - Database Migrations
* [Pip](https://pypi.org/project/pip/) - Dependency Management
* [RESTful](https://restfulapi.net/) - REST docs

### Virtual environments

```
$ sudo apt-get install python-virtualenv
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install Flask
```

Install all project dependencies using:

```
$ pip install -r requirements.txt
```

### Running
 
```
$ export FLASK_APP=app.py
$ export FLASK_ENV=development
$ python -m flask run
```


## Contributing

This API was developed based on:

[Flask documentation](https://flask.palletsprojects.com/)

[REST APIs with Flask and Python](https://www.udemy.com/rest-api-flask-and-python/) 

[The Ultimate Flask Course](https://www.udemy.com/the-ultimate-flask-course) 
