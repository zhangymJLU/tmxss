__author__ = 'ym1ng'
from db_conn import db

class Payload(object):
    def __init__(self, payload, id=None, author=None , comment=None, db=db):
        self.db = db.payload
        if not id:
            try:
                self.id = db.find().sort('_id', 1).next()[0]+1
            except:
                self.id = 0
        else:
            self.id = id
        self.payload = payload
        self.author = author
        self.comment = comment

    def save(self):
        db = self.db
        id = self.id
        author = self.author
        payload = self.payload
        comment = self.comment
        db.insert({'_id': id, 'author': author, 'payload': payload, 'comment': comment})
        db.save()

    @classmethod
    def get_all(cls):
        ret = []
        for i in db.find():
            ret.append(i)
        return ret

    @classmethod
    def filter(cls, id=None, author=None):
        if id:
            return db.find_one({'_id': id})
        elif author:
            ret = []
            for i in db.find({'author':author}):
                ret.append(i)
            return ret
        else:
            return None
