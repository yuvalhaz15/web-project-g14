from utilities.db.db_manager import dbManager


class productsCrudDB:
    def __init__(self):
        pass


    def get_products_id_by_user_id(self,user_id):
        query_result = dbManager.fetch("SELECT toys.id FROM toys join user_toys on toys.id=user_toys.toy_id where user_toys.user_id=%s" % user_id)
        return query_result
    def update_product(self,toy_id,toy_name,toy_category,toy_condition):
        dbManager.commit("UPDATE toys SET toy_name ='%s',toy_category ='%s',toy_condition='%s'WHERE id=%s ;" % (
            toy_name,toy_category,toy_condition,toy_id))
        return True


    def delete_product(self,toy_id_to_delete):
        dbManager.commit("DELETE FROM toys WHERE id =%s;" % toy_id_to_delete)
        dbManager.commit("DELETE FROM user_toys WHERE toy_id =%s;" % toy_id_to_delete)
        return True

productsCrudDbManager = productsCrudDB()