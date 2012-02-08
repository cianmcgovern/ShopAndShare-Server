from logger import write
import logging
import os
import constants
import db

class parsefile(object):
    

    def __init__(self,path,location,store):

        fullpath = constants.UPLOADS + path;
        self.getlines(fullpath,location,store)

    def getlines(self,path,location,store):

        myfile = open(path,"r")

        for line in myfile:
            if isinstance(line,basestring) and line.strip():
                if "/" in line:
                    item = line.split("/")
                    write("Item parsed from file: " + item[0] + " with price: " + item[1] + "with date: " + item[2],logging.INFO)
                    conn = db.db(constants.DATABASE).getconnector()
                    c = conn.cursor()
                    c.execute("""
                              INSERT INTO items VALUES(null,?,?,?,?,?);
                              """,(item[0],item[1],location,store,item[2]))
                    conn.commit()
                else:
                    write("Unable to find seperator in line from file: " +line,logging.WARN)
            else:
                write("Read a non-string type from file input",logging.WARN)
        myfile.close()

        os.remove(path)
