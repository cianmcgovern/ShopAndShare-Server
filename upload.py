import cherrypy
from logger import write
import logging
import datetime
import parsefile
import constants

class upload(object):
       
    def index(self):

        return """
            <html>
            <body>
            <form action="upload" method = "post" enctype="multipart/form-data">
            File: <input name="inputfile" type="file" />
            Location: <input name="location" type="text" />
            Store: <input name="store" type="text" />
            <input type="submit" />
            </form>
            </body>
            </html>
            """
    index.exposed = True

    def upload(self,inputfile,location,store):
            write("File uploaded",logging.INFO)
            self.savefile(inputfile,location,store)
    upload.exposed = True

    def savefile(self,inputfile,location,store):
        filename = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")
        save = open(constants.UPLOADS + filename,"w")

        for line in inputfile.file:
            save.write(line)

        save.close()
        
        write("File saved to: " + constants.UPLOADS + filename,logging.INFO)
        parsefile.parsefile(filename,location,store)
