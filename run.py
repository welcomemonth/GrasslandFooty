# # 创建应用实例
# import sys

# from wxcloudrun import app

# # 启动Flask Web服务
# if __name__ == '__main__':
#     app.run(host=sys.argv[1], port=sys.argv[2])

import werobot

robot = werobot.WeRoBot(token='zzylvhyy')

@robot.handler
def hello(message):
    return 'Hello World!'

# 让服务器监听在 0.0.0.0:80
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()
