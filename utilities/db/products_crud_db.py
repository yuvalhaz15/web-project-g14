from utilities.db.db_manager import dbManager
from datetime import datetime


class productsCrudDB:
    def __init__(self):
        pass

    def get_products_id_by_user_id(self, user_id):
        query_result = dbManager.fetch(
            "SELECT toys.id FROM toys join user_toys on toys.id=user_toys.toy_id where user_toys.user_id=%s" % user_id)
        return query_result

    def update_product(self, toy_id, toy_name, toy_category, toy_condition):
        dbManager.commit("UPDATE toys SET toy_name ='%s',toy_category ='%s',toy_condition='%s'WHERE id=%s ;" % (
            toy_name, toy_category, toy_condition, toy_id))
        return True

    def delete_product(self, toy_id_to_delete):
        dbManager.commit("DELETE FROM user_toys WHERE toy_id =%s;" % toy_id_to_delete)
        dbManager.commit("DELETE FROM toys WHERE id =%s;" % toy_id_to_delete)
        return True

    def add_product(self, user_id, toy_name, toy_category, toy_condition):
        dbManager.commit(
            "INSERT into toys  (toy_name ,toy_category ,toy_condition,is_taken )VALUES ('%s','%s', '%s','%s')" % (
                toy_name, toy_category, toy_condition, 0))
        toy_id_result = dbManager.fetch("SELECT id FROM toys   order by 1 desc LIMIT 1     ")
        toy_id = toy_id_result[0].id
        self.add_toy_and_user_into_user_toys_table(user_id,toy_id )

    def add_toy_and_user_into_user_toys_table(self, user_id, toy_id):
        dbManager.commit("INSERT into user_toys  (user_id ,toy_id ,date_added )VALUES ('%s','%s','%s')" % (
            user_id, toy_id, datetime.now()))
        return True


productsCrudDbManager = productsCrudDB()
