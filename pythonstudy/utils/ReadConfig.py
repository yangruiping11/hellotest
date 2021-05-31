import configparser

# 创建读取配置文件的对象
cf = configparser.ConfigParser()

# 读取配置文件，如果写绝对路径就不需要用os模块
cf.read('E:/software/git/HelloTest/pythonstudy/config/config.ini')

class ReadConfig:
    #获取文件汇总所有的section，一个配置文件中以[]包裹的信息。
    sections = cf.sections()

    #print(sections)

    #读取该section下的所有键。
    options = cf.options('mysql-database')
    #print(options)

    items = cf.items('mysql-database')

    @classmethod
    def  get_host(cls):
        host = cf.get('mysql-database','host')
        return host

    @classmethod
    def  get_port(cls):
        port = cf.get('mysql-database','port')
        return port

    @classmethod
    def  get_user(cls):
        user = cf.get('mysql-database','user')
        return user

    @classmethod
    def  get_password(cls):
        password = cf.get('mysql-database','password')
        return password

    @classmethod
    def  get_database(cls):
        database = cf.get('mysql-database','database')
        return database