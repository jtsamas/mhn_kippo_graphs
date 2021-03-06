# Sqlite3 DB configuration
SQLITE_DB = '/opt/mhn/server/mhn.db'

# Mongo DB configuration
MONGO_HOST = 'localhost'
MONGO_PORT = 27017

# MySQL DB configuration
MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PWD = 'password'

# Kippo sql file path
KIPPO_SQL = '/opt/mhn/scripts/kippo_mysql.sql'

# Graph configuration
KIPPO_GRAPH_PATH = '/opt/mhn/server/mhn/static/img/kippo_graphs/'
KIPPO_GRAPH_RES = 100
KIPPO_GRAPH_FORMAT = 'png'
KIPPO_FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'
KIPPO_FONT_SIZE = 48
KIPPO_THUMB_FACTOR = 2

#You could choose from bmh, dark_background, fivethirtyeight, ggplot or grayscale, visit matplotlib documentation for more information
KIPPO_STYLE = 'ggplot'

__author__ = 'mercolino'
