__author__ = 'ym1ng'
import mongo
import ConfigParser

_config = ConfigParser.ConfigParser()
_config.read('config.ini')

_host = _config.get('mongo', 'host')
_port = int(_config.get('mongo', 'port'))
_username = _config.get('mongo', 'username')
_password = _config.get('mongo', 'password')



def _get_db(host=_host, port=_port, username=_username, password=_password):
    conn = mongo.pymongo.MongoClient(host, port)
    db = conn.tmxss
    if username and password:
        db.authenticate(username, password)
    return db


db = _get_db()


