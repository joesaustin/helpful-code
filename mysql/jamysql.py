import MySQLdb

'''This is basic way to connect to a specific mysql db based on the domain it is linked to. This works even if 2 domains
share the same database
'''
  
class JAMysql():
    def __init__(self):
        self.domain = "food.austin.com" #this can also get set from importing a centralized config file

    def connect_to_db(self, parameters = None):
        if parameters == None: parameters = self.db_config() # you can pass a parameter dictionary or use one of the preset defaults based off the domain
        db = MySQLdb.connect(host= parameters["host"],
                             user = parameters["user"],
                             passwd= parameters["passwd"],
                             db = parameters["db"])
        cursor = db.cursor()
        return cursor

    def db_config(self):
        parameters = {"host":"",
                      "user":"username",
                      "passwd":"password",
                      "db":"sp"}
        
        if "comics.joe.com" in self.domain:
            parameters["host"] = "first_host"
            parameters["passwd"] = "first_password"
            
        elif "food.joe.com" in self.domain:
            parameters["host"] = "second_host"
            parameters["passwd"] = "second_password"
            
        elif "comics.austin.com" or "food.austin.com" in self.domain:
            parameters["host"] = "third_host"
            parameters["passwd"] = "third_password"
        
        return parameters                     
                      
                      
                      
                      
                      
                      
                      
                      