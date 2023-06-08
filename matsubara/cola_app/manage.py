from flask_script import Manager
from colaapp_mente import app 
from colaapp_mente.models.db import InitDB

if __name__ == "__main__":
    manager = Manager(app) 
    manager.add_command('init_db', InitDB()) 
    manager.run()