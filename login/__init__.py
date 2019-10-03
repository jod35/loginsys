from flask import Flask
from login.config import DevConfig

app=Flask(__name__)
app.config.from_object(DevConfig)

from login import views
