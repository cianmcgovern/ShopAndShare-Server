import cherrypy
import upload
import db
import os
import logging
import constants
import test

from logger import write
from Cheetah.Template import Template

class Index(object):
    
    submit = upload.upload()

    name = os.path.normpath(os.path.abspath(__file__))
    constants.FULL_PATH = os.path.dirname(name)

    write("Full path has been set to: " + constants.FULL_PATH,logging.INFO)

    constants.UPLOADS = constants.FULL_PATH + "/uploads/"

    if not os.path.exists(constants.UPLOADS):
        write(constants.UPLOADS + " doesn't exist, creating!", logging.WARN)
        os.makedirs(constants.UPLOADS)

    else:
        write(constants.UPLOADS + " exists", logging.INFO)

    constants.DATABASE = constants.FULL_PATH + "/shopandshare.db"
    db.db(constants.DATABASE)
    
    def index(self):
        
        t = Template(file="data/templates/index.tmpl")
        conn = db.db(constants.DATABASE).getconnector()
        c = conn.cursor()
        c.execute("SELECT * FROM items;")
        t.title = "Shop And Share"
        t.rows = c.fetchall()

        return str(t)
    index.exposed = True

cherrypy.quickstart(Index(),"/",config="shopandshare.conf")
