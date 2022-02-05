import telebot, wikipedia, re
import dotenv
import os
dotenv.load_dotenv()
token = os.getenv("token")
bot = telebot.TeleBot(token)
wikipedia.set_lang('ru')
def getwiki(s):
    try:
        ny = wikipedia.page(s)
        wikitext = ny.content[:1000]
        wikimas = wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ''
        for x in wikimas:
            if len(x.strip()) > 3:
                wikitext2 = wikitext2 + x + '.'
            else:
                break
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
        return wikitext2
    except Exception as e:
        return 'В энциклопедии нет информации об этом'


@bot.message_handler(commands=['start'])
def start(message):
   bot.send_message(message.chat.id, 'Напишите слово, которое нужно найти')


@bot.message_handler(content_types=['text'])
def search(message):
    bot.send_message(message.chat.id, getwiki(message.text))


bot.polling()
