# 创建应用实例
import sys
from robot import myrobot
from flask import Flask, request, jsonify
from werobot.contrib.flask import make_view

app = Flask(__name__)

# WeRoBot 挂载地址和处理微信后台检测请求
@app.route('/', methods=['GET', 'POST'])
def handle_messages():
    data = request.get_json()
    print('消息推送', data)

    if not data:
        return 'success', 200

    ToUserName = data.get('ToUserName')
    FromUserName = data.get('FromUserName')
    MsgType = data.get('MsgType')
    Content = data.get('Content')
    CreateTime = data.get('CreateTime')

    if MsgType == 'text':
        if Content == '回复文字':
            response = {
                'ToUserName': FromUserName,
                'FromUserName': ToUserName,
                'CreateTime': CreateTime,
                'MsgType': 'text',
                'Content': '这是回复的消息'
            }
        elif Content == '回复图片':
            response = {
                'ToUserName': FromUserName,
                'FromUserName': ToUserName,
                'CreateTime': CreateTime,
                'MsgType': 'image',
                'Image': {
                    'MediaId': 'P-hoCzCgrhBsrvBZIZT3jx1M08WeCCHf-th05M4nac9TQO8XmJc5uc0VloZF7XKI'
                }
            }
        elif Content == '回复语音':
            response = {
                'ToUserName': FromUserName,
                'FromUserName': ToUserName,
                'CreateTime': CreateTime,
                'MsgType': 'voice',
                'Voice': {
                    'MediaId': '06JVovlqL4v3DJSQTwas1QPIS-nlBlnEFF-rdu03k0dA9a_z6hqel3SCvoYrPZzp'
                }
            }
        elif Content == '回复视频':
            response = {
                'ToUserName': FromUserName,
                'FromUserName': ToUserName,
                'CreateTime': CreateTime,
                'MsgType': 'video',
                'Video': {
                    'MediaId': 'XrfwjfAMf820PzHu9s5GYsvb3etWmR6sC6tTH2H1b3VPRDedW-4igtt6jqYSBxJ2',
                    'Title': '微信云托管官方教程',
                    'Description': '微信官方团队打造，贴近业务场景的实战教学'
                }
            }
        elif Content == '回复音乐':
            response = {
                'ToUserName': FromUserName,
                'FromUserName': ToUserName,
                'CreateTime': CreateTime,
                'MsgType': 'music',
                'Music': {
                    'Title': 'Relax｜今日推荐音乐',
                    'Description': '每日推荐一个好听的音乐，感谢收听～',
                    'MusicUrl': 'https://c.y.qq.com/base/fcgi-bin/u?__=0zVuus4U',
                    'HQMusicUrl': 'https://c.y.qq.com/base/fcgi-bin/u?__=0zVuus4U',
                    'ThumbMediaId': 'XrfwjfAMf820PzHu9s5GYgOJbfbnoUucToD7A5HFbBM6_nU6TzR4EGkCFTTHLo0t'
                }
            }
        elif Content == '回复图文':
            response = {
                'ToUserName': FromUserName,
                'FromUserName': ToUserName,
                'CreateTime': CreateTime,
                'MsgType': 'news',
                'ArticleCount': 1,
                'Articles': [{
                    'Title': 'Relax｜今日推荐音乐',
                    'Description': '每日推荐一个好听的音乐，感谢收听～',
                    'PicUrl': 'https://y.qq.com/music/photo_new/T002R300x300M000004NEn9X0y2W3u_1.jpg?max_age=2592000',
                    'Url': 'https://c.y.qq.com/base/fcgi-bin/u?__=0zVuus4U'
                }]
            }
        else:
            response = 'success'
    else:
        response = 'success'

    return jsonify(response), 200

# 启动 Flask Web 服务
if __name__ == '__main__':
    app.run(host=sys.argv[1], port=int(sys.argv[2]))
