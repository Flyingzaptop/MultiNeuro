import os
import telebot
import openai
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
#from TTS.api import TTS
openai.api_key ="openai-key"
BOT_TOKEN = 'telegrambot-api'

bot=telebot.TeleBot(BOT_TOKEN)

#model_name = TTS.list_models()[59]
#tts = TTS('tts_models/ja/kokoro/tacotron2-DDC')
#wav = tts.tts("This is a test! This is also a test!!", speaker=tts.speakers[0], language=tts.languages[0])


def split_sentences(text):
    sentences = sent_tokenize(text)
    return sentences

print("Logs:")
@bot.message_handler(command=['start'])
def send_welcome(message):
    print(message.text)
    bot.send_message(message, "Hello! Im Unofficial Telegram Version of GPT-3.5 (ChatGPT). Just type your what you need ;)")
@bot.message_handler(func=lambda msg: True)
def ChatGPT_message(message):
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": message.text}])
    #print("ChatGPT: "+(completion.choices[0].message.content))
    GPT_ans=(completion.choices[0].message.content)
    #tts.tts_to_file(text=GPT_ans, speaker=tts.speakers[0], language=tts.languages[0], file_path="ans.wav")
    sentences = split_sentences(GPT_ans)
    #lastChatId = message.chat.id
    for sentence in sentences:
      bot.send_message(message.chat.id, sentence)
    #bot.reply_to(message, GPT_ans_split)
    #bot.send_audio(lastChatId, audio=open('ans.wav','rb'))
    print("User: "+message.text)
    print("GPT: "+ GPT_ans)
bot.infinity_polling()

