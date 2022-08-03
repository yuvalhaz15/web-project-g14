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

    def add_user(self, email, password, private_name, last_name, phone_number, adress, city, region):
        dbManager.commit(
            "INSERT into users  (private_name ,last_name,email,phone_number,password )VALUES ('%s','%s', '%s','%s','%s')" % (
                private_name, last_name, email,phone_number, password))
        user_id_result = dbManager.fetch("SELECT user_id FROM users   order by 1 desc LIMIT 1 ")
        user_id = user_id_result[0].user_id

        self.add_user_location_to_location_table(user_id, adress, city, region)
        return True

    def add_user_location_to_location_table(self, user_id, adress, city, region):
        print(city)
        dbManager.commit("INSERT into location  (user_id ,adress ,city,region )VALUES ('%s','%s','%s','%s')" % (
            user_id, adress, city, region))
        return True


usersSignUpDbManager = signUpDB()
