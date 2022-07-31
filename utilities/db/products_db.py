from utilities.db.db_manager import dbManager


class productsDB:
    def __init__(self):
        pass

    def get_all_products(self):

        query_result = dbManager.fetch('SELECT * FROM toys')
        return query_result


    def get_category_products(self,category):
      query_result = dbManager.fetch("SELECT * FROM toys where toy_category='%s'" % category)
      return query_result

    def get_products_by_user_id(self,user_id):
        query_result = dbManager.fetch("SELECT *  FROM toys join user_toys on toys.id=user_toys.toy_id where user_toys.user_id=%s" % user_id)
        return query_result

    def get_last_user_toy_id(self,user_id):
        toy_id_result = dbManager.fetch(
            "SELECT toy_id FROM user_toys where user_toys.user_id=%s order by 1 desc LIMIT 1" % user_id)
        toy_id = toy_id_result[0].toy_id
        return toy_id+1
        
productsDbManager = productsDB()