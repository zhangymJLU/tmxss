__author__ = 'ym1ng'
from db_conn import db

class Payload(object):
    def __init__(self, payload, author=None , comment=None, db=db):
        self.db = db.payload
        self.payload = payload
        self.author = author
        self.comment = comment

    def save(self):
        db = self.db
        author = self.author
        payload = self.payload
        comment = self.comment
        db.insert({'author': author, 'payload': payload, 'comment': comment})
        #db.save()

    @classmethod
    def get_all(cls):
        ret = []
        for i in db.find():
            ret.append(i)
        return ret

    @classmethod
    def filter(cls, id=None, author=None):
        if id:
            return db.payload.find_one({'_id': id})
        elif author:
            return [i for i in db.payload.find({'author':author})]
        else:
            return None
