__author__ = 'ym1ng'
from db_conn import db


class Result(object):
    def __init__(self, username, result={}, db=db):
        self.db = db.result
        self.username = username
        self.result = result

    def save(self):
        db = self.db
        username = self.username
        result = self.result
        db.insert({'username': username, 'result': result})
        #db.save()

    @classmethod
    def filter(cls, id=None, username=None):
        if id:
            return db.result.find_one({'_id': id})
        elif username:
            return [i for i in db.result.find({'username': username}).sort('_id', 1)]
        else:
            return None