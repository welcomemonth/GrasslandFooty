from werobot import WeRoBot

myrobot = WeRoBot(token='zzylvhyy')


@myrobot.handler
def hello(message):
    return 'Hello World!'