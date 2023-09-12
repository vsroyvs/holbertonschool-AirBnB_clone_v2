## AirBnB clone - Web framework
### Learning Objectives
* What is a Web Framework
* How to build a web framework with Flask
* How to define routes in Flask
* What is a route
* How to handle variables in a route
* What is a template
* How to create a HTML response in Flask by using a template
* How to create a dynamic template (loops, conditions…)
* How to display in HTML data from a MySQL database


Ex.

        from flask import Flask, request
        from markupsafe import escape

        app = Flask(__name__)

        @app.route('/')
        def hello():
        name = request.args.get("name", "World")
        return f'Hello, {escape(name)}!'