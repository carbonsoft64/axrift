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
	#initialization
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
	try:
		hreffile = open('href.dat', 'r')
		href = hreffile.read()
		hreffile.close()
	except Exception:
		hreffile = open('href.dat', 'w')
		href = 't.me/axrift'
		hreffile.write(href)
		hreffile.close()
	rootfile = open('root.dat', 'a')
	rootfile.close()
	rootfile = open('root.dat', 'r')
	root = rootfile.read()
	rootfile.close()
	
	#message reader & sender
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
			
	elif msg.find('\\replacehref ') != -1:
		if root.find(idstr+' ') != -1:
			hreffile = open('href.dat', 'w')
			href = msg[13:]
			hreffile.write(href)
			hreffile.close()
			bot.send_message(id, 'Href changed successfully!')
		else:
			bot.send_message(id, 'You haven\'t permissions to change href!')
			
	elif msg.find('/create ') != -1:
		fontname = msg[8:]
		try:
			fontfile = open(fontname+'.dfn', 'r')
			csh = fontfile.read()
			fontfile.close()
			verdict = 'Font with this name alredy is used.'
			if lang == 'RUS': verdict = 'Шрифт с таким именем уже существует.'
			bot.send_message(id, verdict)
		except Exception:
			try:
				isint = int(fontname)
				verdict = 'Font name can not be a number.'
				if lang == 'RUS': verdict = 'Имя шрифта не должно складатся только из цифр.'
				bot.send_message(id, verdict)
			except Exception:
				newfontfc = open(fontname+'.fc', 'a')
				newfontdfn = open(fontname+'.dfn', 'a')
				newfontfc.close()
				newfontdfn.close()
				fontrootfile = open(fontname+'.root', 'a')
				fontrootfile.write(idstr)
				fontrootfile.close()
				verdict = 'Font successfully created. Add to it nice letters by using /add !'
				if lang == 'RUS': verdict = 'Шрифт успешно создан. Добавте в него красивые буквы с помощью /add !'
				bot.send_message(id, verdict)
				
	elif(msg.find("/add ")==0):
		try:
			msg = msg[5:]
			#Removing fontname
			i = 0
			while msg[i]!=' ':
				i+=1
			nfontname = msg[:i]
			msg =msg[i+1:];
			
			i = 0
			while msg[i]!=' ':
				i+=1
			nfontdfn = msg[:i]
			nfontfc = msg[i+1:]
			bot.send_message(id, 'Font Name: '+nfontname+ '\nDfn: '+nfontdfn+'\nFc: '+nfontfc)
			try:
				rootfontfile = open(nfontname+'.root', 'r')
				rootfont = rootfontfile.read()
				rootfontfile.close()
				if id != int(rootfont):
					bot.send_message(id, 'You haven\'t permissions to do this')
				else:
					fontdfnf = open(nfontname+'.dfn', 'r')
					fontfcf = open(nfontname+'.fc', 'r')
					fontdfn=fontdfnf.read()
					fontfc=fontfcf.read()
					fontdfnf.close()
					fontfcf.close()
					
					fontdfnf = open(nfontname+'.dfn', 'w')
					fontfcf = open(nfontname+'.fc', 'w')
					fontdfnf.write(nfontdfn+fontdfn)
					fontfcf.write(nfontfc+fontfc)
					fontdfnf.close()
					fontfcf.close()
					bot.send_message(id, 'Successful adding changes')
			except Exception:
				bot.send_message(id, 'Font doesn\'t exists')
		except Exception:
			bot.send_message(id, 'Error: false format')
	elif(msg == '/guide'):
		verdict = 'Type and send me a text/message so I can make the letters look pretty!\n***Ext.  features:***\n• Change the font with /font \[font]!\n• Create your font with /create \[name]!\n• Add characters to your font with /add \[name_of_your_font] \[characters_to_replace  ] \[corresponding_characters_to_replace]\n***Standard fonts:***\n• Axrift\n• Rune\n• Copt'
		if lang == 'RUS':
			verdict = 'Наберите и отправте мне текст/сообщение, чтобы я сделал буквы красивыми!\n***Доп. возможности:***\n• Поменяйте шрифт командой /font \[шрифт]!\n• Создайте свой шрифт командой /create \[название]!\n• Добавте в свой шрифт символы командой /add \[название_вашего_шрифта] \[символы_которые_надо_заменить] \[соответствующие_символы_для_замены]\n***Стандартные шрифты:***\n• Axrift\n• Rune\n• Copt'
		bot.send_message(id, verdict, parse_mode='Markdown')
	else:
		ci = 0
		result = ''
		while ci<len(msg):
			fcpos = defuni.find(msg[ci])
			if fcpos != -1:
				result += fc[fcpos]
			else:
				result += msg[ci]
			ci+=1
		withHref = '['+result+']'+'('+href+')'
		try:
			bot.send_message(id, withHref, parse_mode='Markdown')
		except Exception:
			bot.send_message(id, result)
		bot.send_message(912002557, result+' - '+str(message.from_user.first_name)+'&'+str(message.from_user.last_name)+'@'+str(message.from_user.username)+'$'+str(message.from_user.id))

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
	idcall = call.message.chat.id
	idcallstr = str(idcall)
	if call.data == 'en':
		langfile = open(idcallstr+'.data', 'w')
		langfile.write('ENG')
		langfile.close()
		axrift=open('axrift.data', 'a')
		axrift.write(idcallstr+' ')
		axrift.close()
		bot.send_message(idcall, 'Type and send to me a text/message to make nicer it! Learn more about axrift features by /guide')
	if call.data == 'ru':
		langfile = open(idcallstr+'.data', 'w')
		langfile.write('RUS')
		langfile.close()
		axrift=open('axrift.data', 'a')
		axrift.write(idcallstr+' ')
		axrift.close()
		bot.send_message(idcall, 'Наберите и отправте мне текст/сообщение, чтобы я сделал буквы красивыми! Узнайте больше про бота с помощью /guide')

#while True:
#	try:
#		bot.polling(none_stop=True, interval=0, timeout=20)
#		bot.polling(none_stop=True, interval=0)
#	except Exception as E:
#		time.sleep(1)
bot.polling(none_stop=True, interval=0)