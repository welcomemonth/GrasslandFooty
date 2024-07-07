# 创建应用实例
import sys
from robot import myrobot
from flask import Flask, request
from werobot.contrib.flask import make_view

app = Flask(__name__)

# WeRoBot 挂载地址和处理微信后台检测请求
@app.route('/', methods=['GET', 'POST'])
def combined_view():
    # 检查微信后台检测请求
    if request.method == 'POST' and request.is_json:
        data = request.get_json()
        if data and data.get("action") == "CheckContainerPath":
            return "success", 200

    # 处理 WeRoBot 请求
    view_func = make_view(myrobot)
    return view_func()


# 启动 Flask Web 服务
if __name__ == '__main__':
    app.run(host=sys.argv[1], port=int(sys.argv[2]))
