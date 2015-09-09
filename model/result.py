__author__ = 'ym1ng'
from db_conn import db


class Result(object):
    def __init__(self, username, id=None, result={}, db=db):
        self.db = db.result
        self.username = username
        self.result = result
        if not id:
            try:
                self.id = db.find().sort('_id', 1).next()[0]+1
            except:
                self.id = 0
        else:
            self.id = id

    def save(self):
        db = self.db
        id = self.id
        username = self.username
        result = self.result
        db.insert({'_id': id, 'username': username, 'result': result})
        db.save()

    @classmethod
    def filter(cls, id=None, username=None):
        if id:
            return db.find_one({'_id': id})
        elif username:
            ret = []
            for i in db.find({'username': username}).sort('_id', 1):
                ret.append(i)
            return ret
        else:
            return None