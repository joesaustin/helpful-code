import jamysql


class JASample():
    
    def __init__(self):
        '''Here we are using the default db set in the jamysql which is based on the domain/enviorment that you are interacting with'''
        self.database = jamysql.JAMysql()
    
    '''to confirm if a record you created now exist in the db perform a simple query for a count. In this example you are
    checking for a specific user in an accounts table. For this to work you have to make sure the user you created has
    a unique user name so make sure if you are creating a new user add a date timestamp to it (johnYYYYMMDDHHMMSS)
    and pass that user name as your parameter'''
            
    def get_username_count(self,user):
        cursor = self.database.connect_to_db()
        cursor.execute("select count(*) from accounts where username =%s;" % user)
        '''fetch the returned count.'''
        row = cursor.fetchone()
        count = row[0]
        print count
    
    '''In this example you are returning several columns from a row'''
    def get_name_and_age(self,user):
        cursor = self.database.connect_to_db()
        cursor.execute("select first_name, last_name, age from accounts where username =%s;" % user)
        
        '''the result is in an array ordered by the way you listed the columns in the select.'''
        row = cursor.fetchone()
        first_name = row[0]
        last_name = row[1]
        age = row[2]
        print "This user's name is "+first_name+" "+last_name+" and they are "+age+" old." 
