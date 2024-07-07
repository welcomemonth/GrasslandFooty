from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def send_message(appid, message):
    url = f"http://api.weixin.qq.com/cgi-bin/message/custom/send?from_appid={appid}"
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, json=message)
    if response.status_code != 200:
        print("接口返回错误", response.text)
        raise Exception(response.text)
    print("接口返回内容", response.json())
    return response.json()

@app.route('/', methods=['POST'])
def handle_messages():
    data = request.get_json()
    print('消息推送', data)
    
    appid = request.headers.get('x-wx-from-appid', '')
    ToUserName = data.get('ToUserName')
    FromUserName = data.get('FromUserName')
    MsgType = data.get('MsgType')
    Content = data.get('Content')
    CreateTime = data.get('CreateTime')
    
    print('推送接收的账号', ToUserName, '创建时间', CreateTime)

    if MsgType == 'text':
        if Content == '回复文字':
            send_message(appid, {
                "touser": FromUserName,
                "msgtype": "text",
                "text": {
                    "content": "这是回复的消息"
                }
            })
        elif Content == '回复图片':
            send_message(appid, {
                "touser": FromUserName,
                "msgtype": "image",
                "image": {
                    "media_id": "P-hoCzCgrhBsrvBZIZT3jx1M08WeCCHf-th05M4nac9TQO8XmJc5uc0VloZF7XKI"
                }
            })
        elif Content == '回复语音':
            send_message(appid, {
                "touser": FromUserName,
                "msgtype": "voice",
                "voice": {
                    "media_id": "06JVovlqL4v3DJSQTwas1QPIS-nlBlnEFF-rdu03k0dA9a_z6hqel3SCvoYrPZzp"
                }
            })
        elif Content == '回复视频':
            send_message(appid, {
                "touser": FromUserName,
                "msgtype": "video",
                "video": {
                    "media_id": "XrfwjfAMf820PzHu9s5GYsvb3etWmR6sC6tTH2H1b3VPRDedW-4igtt6jqYSBxJ2",
                    "title": "微信云托管官方教程",
                    "description": "微信官方团队打造，贴近业务场景的实战教学"
                }
            })
        elif Content == '回复音乐':
            send_message(appid, {
                "touser": FromUserName,
                "msgtype": "music",
                "music": {
                    "title": "Relax｜今日推荐音乐",
                    "description": "每日推荐一个好听的音乐，感谢收听～",
                    "music_url": "https://c.y.qq.com/base/fcgi-bin/u?__=0zVuus4U",
                    "HQ_music_url": "https://c.y.qq.com/base/fcgi-bin/u?__=0zVuus4U",
                    "thumb_media_id": "XrfwjfAMf820PzHu9s5GYgOJbfbnoUucToD7A5HFbBM6_nU6TzR4EGkCFTTHLo0t"
                }
            })
        elif Content == '回复图文':
            send_message(appid, {
                "touser": FromUserName,
                "msgtype": "link",
                "link": {
                    "title": "Relax｜今日推荐音乐",
                    "description": "每日推荐一个好听的音乐，感谢收听～",
                    "thumb_url": "https://y.qq.com/music/photo_new/T002R300x300M000004NEn9X0y2W3u_1.jpg?max_age=2592000",
                    "url": "https://c.y.qq.com/base/fcgi-bin/u?__=0zVuus4U"
                }
            })
        elif Content == '回复小程序':
            send_message(appid, {
                "touser": FromUserName,
                "msgtype": "miniprogrampage",
                "miniprogrampage": {
                    "title": "小程序卡片标题",
                    "pagepath": "pages/index/index",
                    "thumb_media_id": "XrfwjfAMf820PzHu9s5GYgOJbfbnoUucToD7A5HFbBM6_nU6TzR4EGkCFTTHLo0t"
                }
            })
        return 'success', 200
    return 'success', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
