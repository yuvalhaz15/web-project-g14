from utilities.db.db_manager import dbManager


class productsDB:
    def __init__(self):
        pass

    def get_all_products(self):

        query_result = dbManager.fetch('SELECT * FROM toys')
        return query_result

productsDbManager = productsDB()