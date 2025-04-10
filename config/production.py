from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\x13\x90m\xc3^Jn\x8b\xf91b\xb5\xd1.\xd5\x9e'
