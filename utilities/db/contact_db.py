from utilities.db.db_manager import dbManager
from datetime import datetime


class contactDB:
    def __init__(self):
        pass

    def insert_message(self, user_id, content, message_subject):
        current_date_and_time = datetime.now()
        dbManager.commit(
            "INSERT into contact  (user_id,subject,user_text,date )VALUES ('%s','%s', '%s','%s')" % (
                user_id, message_subject,content,  current_date_and_time))
        return True


contactDbManager = contactDB()
