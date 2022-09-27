from flask import Flask
from . import models
from flask_migrate import Migrate

def create_app(): 
    app = Flask(__name__)

    # DB config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Postgres@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    @app.route('/')
    def hello():
        return 'Hello, PetFax!'

    # register pet blueprint 
    from . import pet 
    app.register_blueprint(pet.bp)

    # register fact blueprint 
    from . import fact
    app.register_blueprint(fact.bp)

    # Return the app
    return app