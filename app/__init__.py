from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

#initialization of application

app= Flask(__name__, instance_relative_config = True)

# Creating the app configurations
app.config.from_object(config_options[config_name])

#initializing bootstrap extension
bootstrap.init_app(app)


from .main import views