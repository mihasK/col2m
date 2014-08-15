####################################################
# MySQL settings
####################################################
MYSQL_HOST = 'localhost'
MYSQL_PORT = '3306'
MYSQL_USERNAME = 'root'
MYSQL_PASSWORD = '123'
MYSQL_DBNAME = 'col_test'
####################################################
# PostgreSQL settings
####################################################
# POSTGRESQL_HOST = 'localhost'
# POSTGRESQL_PORT = '5432'
# POSTGRESQL_USERNAME = 'postgres'
# POSTGRESQL_PASSWORD = '123'
# POSTGRESQL_DBNAME = 'c2'
# POSTGRESQL_ECHO_MODE = False

POSTGRESQL_HOST = 'c2-54-197-241-96.compute-1.amazonaws.com'
POSTGRESQL_PORT = '5432'
POSTGRESQL_USERNAME = 'zobzgeddxcapwp'
POSTGRESQL_PASSWORD = 'gQvhHVvFqORe6dsDqUUwLfAqhd'
POSTGRESQL_DBNAME = 'd2efq4ja8ot0s9'
POSTGRESQL_ECHO_MODE = False
####################################################
# MongoDB settings
####################################################
# MONGO_HOST = 'localhost'
# MONGO_PORT = 27017
# MONGO_USERNAME = ''
# MONGO_PASSWORD = ''
# MONGO_DBNAME = 'c2'
MONGO_HOST = 'col5-alpha-api.collectrium.com'
MONGO_PORT = 27017
MONGO_USERNAME = ''
MONGO_PASSWORD = ''
MONGO_DBNAME = 'migration_old_artists'

REFERENCE_DATA_HOST = 'http://reference-api-beta-test.collectrium.com'

from mongoengine import connect

db = connect(MONGO_DBNAME, host=MONGO_HOST)

# gQvhHVvFqORe6dsDqUUwLfAqhd
# postgres://zobzgeddxcapwp:gQvhHVvFqORe6dsDqUUwLfAqhd@ec2-54-197-241-96.compute-1.amazonaws.com:5432/d2efq4ja8ot0s9
