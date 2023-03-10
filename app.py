import openai
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *

# set up the OpenAI API key
openai.api_key = os.environ["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"]

# set up the Line Bot API and WebhookHandler
app = Flask(__name__)
line_bot_api = LineBotApi(os.environ['CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['CHANNEL_SECRET'])

# handle incoming messages
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # get user input message
    user_input = event.message.text
    
    # set up the OpenAI prompt with user input
    prompt = f"User: {user_input}\nAI:"
    
    # generate AI response using OpenAI's GPT model
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    
    # get the AI response text from the OpenAI response
    ai_response = response.choices[0].text.strip()
    
    # send the AI response back to the user
    message = TextSendMessage(text=ai_response)
    line_bot_api.reply_message(event.reply_token, message)

# set up the Flask app to handle incoming requests
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)