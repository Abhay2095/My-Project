import configparser

config = configparser.RawConfigParser()

config.read("E:\\My Project\\Configuration\\config.ini")


class ReadConfig:
    @staticmethod
    def getbaseurl():
        baseurl = config.get('basic info', 'baseurl')
        return baseurl

    @staticmethod
    def getusername():
        username = config.get('basic info', 'username')
        return username

    @staticmethod
    def getpassword():
        password = config.get('basic info', 'password')
        return password








