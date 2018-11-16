class DefaultConfig(object):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:12345678@db/github'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SESSION_TYPE = 'filesystem'
	
class ProductionConfig(DefaultConfig):
	DEBUG = False
	