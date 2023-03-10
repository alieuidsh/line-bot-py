
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import openai
import os

app = Flask(__name__)

openai.api_key = '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'
line_bot_api = LineBotApi(os.environ['CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['CHANNEL_SECRET'])


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
def handle_message(event):
    #message_text = AliGPT.CH_GPT(event.message.text)
    #sam = event.message.text
    message_text = "我是AI胖胖"+ event.message.text
    #message_text = sam
    #message_text = " (我是AI胖胖)"
    #message_text = " 我是AI胖胖"
    message = TextSendMessage(text=message_text)
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
