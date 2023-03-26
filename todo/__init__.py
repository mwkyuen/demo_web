import os
from . import db
from . import todo
from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, 'todo_app.sqlite'),
    )

    # ensure the instance folder exists
    os.makedirs(app.instance_path, exist_ok=True)
    
    db.init_app(app)
    app.register_blueprint(todo.bp)

    return app


