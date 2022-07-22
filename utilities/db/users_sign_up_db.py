from utilities.db.db_manager import dbManager


class signUpDB:
    def __init__(self):
        pass

    def email_is_exist(self, email):
        query_result = dbManager.fetch("SELECT user_id FROM users where users.email='%s'" % email)
        if query_result:
            return True
        return False


    def get_cities_list(self):
       cities_list = dbManager.fetch("SELECT city_name FROM cities")
       return cities_list


usersSignUpDbManager = signUpDB()
