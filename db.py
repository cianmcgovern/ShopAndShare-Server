import sqlite3
import logging
import os

from logger import write

CREATED = False

class db(object):
    
    def __init__(self,filename):

        CREATED = os.path.exists(filename)

        self.conn = sqlite3.connect(filename)

        if not CREATED:
            self.setupdb()
        else:
            write("Database exists at:" + filename,logging.INFO)
    
    def setupdb(self):
        write("Database not created, creating...", logging.WARN)        
        c = self.conn.cursor()
        c.execute("""
                  CREATE TABLE IF NOT EXISTS items(id NOT_NULL AUTO_INCREMENT,product TEXT, price REAL, location TEXT, store TEXT,PRIMARY KEY(id));
                  """)
        c.close()
        CREATED = True
    
    def getconnector(self):
        return self.conn
