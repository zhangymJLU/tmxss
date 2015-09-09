# -*- coding:utf-8 -*-
__author__ = 'ym1ng'
from db_conn import db
import hashlib


class User(object):
    def __init__(self, username, db=db):
        self.db = db
        self.username = username

    def login(self, password):
        username = self.username
        password = hashlib.md5(password)
        db = self.db
        result = db.find_one({'username': username, 'password': password})
        if result:
            return True
        else:
            return False

    def register(self, email, password, comment=None):
        username = self.username
        password = hashlib.md5(password)
        db = self.db
        if db.find_one({'email': email}):
            raise Exception('邮箱已注册')
        if db.find_one({'username': username}):
            raise Exception('用户已存在')
        db.insert({'username': username, 'email': email, 'password': password, 'comment': comment})
        db.save()

    def change_pass(self, ord_password, new_password):
        pass

    @classmethod
    def filter(cls, username=None, email=None, id=None, db=db):
        username = db.find_one({'$or': [{'username': username}, {'email': email}, {'id': id}]})['username']
        if username:
            return cls(username=username)
        return None
