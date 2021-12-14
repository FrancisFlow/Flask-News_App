from flask import Flask

from config import DevConfig

#initialization of application

app= Flask(__name__)


#configuration set up
app.config.from_object(DevConfig)

from app import views