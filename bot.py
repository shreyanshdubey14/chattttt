import openai

import telegram

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):

    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi, I'm ChatGPT, how can I help you today?")

def chat(update, context):

    prompt = update.message.text

    response = openai.Completion.create(

        engine="text-davinci-002",

        prompt=prompt,

        max_tokens=1024,

        n=1,

        stop=None,

        temperature=0.5,

    ).get("choices")[0].text

    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

openai.api_key = "YOUR_OPENAI_API_KEY"

bot = telegram.Bot(token="6048217054:AAGCyQZ9AlPt_pCJ6BH4YeQp_NJT7rYssaM")

updater = Updater(token="6048217054:AAGCyQZ9AlPt_pCJ6BH4YeQp_NJT7rYssaM", use_context=True)

dispatcher = updater.dispatcher

start_handler = CommandHandler("start", start)

chat_handler = MessageHandler(Filters.text, chat)

dispatcher.add_handler(start_handler)

dispatcher.add_handler(chat_handler)

updater.start_polling()
