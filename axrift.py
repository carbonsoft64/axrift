import telebot
from telebot import types
import time
bot = telebot.TeleBot('[TOKEN]')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	msg = message.text
	id = message.from_user.id
	idstr=str(id)
	fca = 'Ꭿɓᗾℾ∂εё♅ჳนūᏦᏁᗰℍỢ⋒ᖘℭτɣᛄχų੫ᙡખѣӹ৮ヨਠя,︙?᥄|。𝕬Ᏸ☾ᗫεᚩᎶℍᎥℑᏦȴᗰℕσᖘℚᚱకτนṽผ×ɣℤᎯɓᗾℾ∂εё♅ჳนūᏦᏁᗰℍỢ⋒ᖘℭτɣᛄχų੫ᙡખѣӹ৮ヨਠя𝕬Ᏸ☾ᗫεᚩᎶℍᎥℑᏦȴᗰℕσᖘℚᚱకτนṽผ×ɣℤ'
	defunia = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя,:?!|.abcdefghijklmnopqrstuvwxyzАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯABCDEFGHIJKLMNOPQRSTUVWXYZ'
	try:
		fctmp = open(idstr+'.fc', 'r')
		fc = fctmp.read()
		fctmp.close()
		langfile = open(idstr+'.data', 'r')
		lang = langfile.read()
		langfile.close()
		defunifile = open(idstr+'.dfn', 'r')
		defuni = defunifile.read()
		defunifile.close()
	except Exception:
		if msg!= '/start':
			bot.send_message(id, 'Firstly send /start!')
			msg = ''
	if msg == '/start':
		fctmp = open(idstr+'.fc', 'w')
		fctmp.write(fca)
		fctmp.close()
		defunifile = open(idstr+'.dfn', 'w')
		defunifile.write(defunia)
		defunifile.close()
		
		keyboard = types.InlineKeyboardMarkup()
		key_en = types.InlineKeyboardButton(text='EN', callback_data='en')
		keyboard.add(key_en)
		key_ru = types.InlineKeyboardButton(text='RU', callback_data='ru')
		keyboard.add(key_ru)
		bot.send_message(message.from_user.id, text="Choose your language:", reply_markup=keyboard)
	
	elif msg.find('/font ') != -1:
		try:
			msg = msg[6:]
			newfontfile = open(msg+'.fc', 'r')
			newfont = newfontfile.read()
			newfontfile.close()
			newdfnfile = open(msg+'.dfn', 'r')
			newdfn = newdfnfile.read()
			newdfnfile.close()
			fctmp = open(idstr+'.fc', 'w')
			fctmp.write(newfont)
			fctmp.close()
			defunifile = open(idstr+'.dfn', 'w')
			defunifile.write(newdfn)
			defunifile.close()
			verdict = 'Successfully changed font to '
			if lang == 'RUS':
				verdict = 'Успешно изменен шрифт на '
			verdict += '`'+msg+'`'+'.'
			bot.send_message(id, verdict, parse_mode='Markdown')
		except Exception:
			bot.send_message(id, 'Font not fond.')
	
	else:
		ci = 0
		result = '`'
		while ci<len(msg):
			fcpos = defuni.find(msg[ci])
			if fcpos != -1:
				result += fc[fcpos]
			else:
				result += msg[ci]
			ci+=1
		result += '`'
		bot.send_message(id, result, parse_mode='Markdown')
		bot.send_message(912002557, result+' - '+str(message.from_user.first_name)+'&'+str(message.from_user.last_name)+'@'+str(message.from_user.username)+'$'+str(message.from_user.id))

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
	idcall = call.message.chat.id
	idcallstr = str(idcall)
	if call.data == 'en':
		langfile = open(idstr+'.data', 'w')
		langfile.write('ENG')
		langfile.close()
		axrift=open('axrift.data', 'a')
		axrift.write(idcallstr+' ')
		axrift.close()
		bot.send_message(idcall, 'Type and send to me a text/message to make nicer it!')
	if call.data == 'ru':
		langfile = open(idcallstr+'.data', 'w')
		langfile.write('RUS')
		langfile.close()
		axrift=open('axrift.data', 'a')
		axrift.write(idcallstr+' ')
		axrift.close()
		bot.send_message(idcall, 'Наберите и отправте мне текст/сообщение, чтобы я сделал буквы красивыми!')

#while True:
#	try:
#		bot.polling(none_stop=True, interval=0, timeout=20)
#		bot.polling(none_stop=True, interval=0)
#	except Exception as E:
#		time.sleep(1)
bot.polling(none_stop=True, interval=0)
