from utilities.db.db_manager import dbManager


class usersDB:
    def __init__(self):
        pass

    def email_is_exist(self, email):
        query_result = dbManager.fetch("SELECT user_id FROM users where users.email='%s'" % email)
        if query_result :
            return True
        return False


    def password_is_correct(self,email, entered_password):
        query_result = dbManager.fetch("SELECT password FROM users where users.email='%s'" % email)
        if query_result:
         user_password=query_result[0].password
            
        return user_password==entered_password

    def get_user_name(self,email):
       private_name_result = dbManager.fetch("SELECT private_name FROM users where users.email='%s'" % email)
       last_name_result=dbManager.fetch("SELECT last_name FROM users where users.email='%s'" % email)
       private_name=private_name_result[0].private_name
       last_name=last_name_result[0].last_name
       return private_name+' '+last_name
    
    
    def get_user_id(self,email):
        user_id_result=dbManager.fetch("SELECT user_id FROM users where users.email='%s'" % email)
        user_id = user_id_result[0].user_id
        return user_id
    
    
usersDbManager = usersDB()
