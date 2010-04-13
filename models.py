import cgi

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

class Task(db.Model):
	owner = db.UserProperty()
	content = db.StringProperty(multiline=True)
	date = db.DateTimePropery(auto_now_add=True)
	notification_date = db.DateTimeProperty()
	status = db.ReferenceColumn(Status)

class Status(db.Model):
	owner = db.UserProperty()
	name = db.StrtingProperty()
	
