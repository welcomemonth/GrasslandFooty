# 创建应用实例
import sys
from robot import myrobot
from flask import Flask
from werobot.contrib.flask import make_view

app = Flask(__name__)
app.add_url_rule(rule='/robot/', # WeRoBot 挂载地址
                 endpoint='werobot', # Flask 的 endpoint
                 view_func=make_view(myrobot),
                 methods=['GET', 'POST'])

# 处理微信后台检测请求
@app.route('/check', methods=['POST', 'GET'])
def check():
    data = request.get_json()
    if data and data.get("action") == "CheckContainerPath":
        return "success", 200
    return "", 200


# 启动Flask Web服务
if __name__ == '__main__':
    app.run(host=sys.argv[1], port=sys.argv[2])

