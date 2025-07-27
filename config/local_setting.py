import yaml

# 读取配置文件
with open("/Users/liyifan/PycharmProjects/flaskProject/config/config.yaml", "r") as file:
    config = yaml.safe_load(file)
    # 提取数据库配置
db_config = config.get('database')

# 访问数据库配置信息
username = db_config.get('username')
password = db_config.get('password')

SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{username}:{password}@127.0.0.1:3306/autotest'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SERVER_PORT = 49998
DEBUG = False
SQLALCHEMY_ECHO = False
SQLALCHEMY_ENCODING = 'utf-8'
