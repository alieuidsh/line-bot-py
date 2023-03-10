from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
#import openai
import os

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ['CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['CHANNEL_SECRET'])
#openai.api_key = os.environ['openai.api_key']

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
    pretty_note = '♫♪♬'
    pretty_text = ''
    for i in event.message.text:
        pretty_text += i
        pretty_text += random.choice(pretty_note)
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=pretty_text))
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
