import telebot
from telebot import types
import time
import os
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
	
	
	#markup = types.									ReplyKeyboardMarkup(row_width=2)
	#markup.add(types.KeyboardButton('3'))
	#bot.send_message(id, 'fj', reply_markup=markup)
	
	
	#message reader & sender
	result = ''
	msggg = msg
	if msg == '/start':
		fctmp = open(idstr+'.fc', 'w')
		fctmp.write(fca)
		fctmp.close()
		defunifile = open(idstr+'.dfn', 'w')
		defunifile.write(defunia)
		defunifile.close()
		
		keyboard = types.InlineKeyboardMarkup()
		key_eng = types.InlineKeyboardButton(text='EN🇺🇸', callback_data='eng')
		keyboard.add(key_eng)
		key_rus = types.InlineKeyboardButton(text='RU💩', callback_data='rus')
		keyboard.add(key_rus)
		key_ukr = types.InlineKeyboardButton(text='UA🇺🇦', callback_data='ukr')
		keyboard.add(key_ukr)
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
			if lang == 'UKR':
				verdict = 'Успішно змінений шрифт на '
			verdict += '`'+msg+'`'+'.'
			bot.send_message(id, verdict, parse_mode='Markdown')
		except Exception:
			verdict= 'Font not fond.'
			if lang == 'RUS': verdict= 'Шрифт не найден.'
			if lang == 'UKR': verdict = 'Шрифт не знайдено.'
			bot.send_message(id, )
			
	#admin
	elif msg.find('\\replacehref ') != -1:
		if root.find(idstr+' ') != -1:
			hreffile = open('href.dat', 'w')
			href = msg[13:]
			hreffile.write(href)
			hreffile.close()
			bot.send_message(id, 'Href changed successfully!')
		else:
			bot.send_message(id, 'You haven\'t permissions to change href!')
	elif msg.find('\\send')==0:
		msg = msg[5:]
		if root.find(idstr+' ') != -1:
			try:
				i = 0
				while msg[i]!=' ': i+=1
				sid = msg[:i]
				msg = msg[i+1:]
				bot.send_message(int(sid), msg)
				bot.send_message(id, 'Successfully sended message to id\n'+sid+' with text\n'+msg)
			except Exception:
				bot.send_message(id, 'ERROR: False format or permission denied!')
		else:
			bot.send_message(id, 'You haven\'t permissions to send messages!')
	#noadmin
			
	elif msg.find('/create ') != -1:
		fontname = msg[8:]
		try:
			fontfile = open(fontname+'.dfn', 'r')
			csh = fontfile.read()
			fontfile.close()
			verdict = 'Font with this name alredy is used.'
			if lang == 'RUS': verdict = 'Шрифт с таким именем уже существует.'
			if lang == 'UKR': verdict = 'Шрифт з таким ім\'ям вже існує.'
			bot.send_message(id, verdict)
		except Exception:
			try:
				isint = int(fontname)
				verdict = 'Font name can not be a number.'
				if lang == 'RUS': verdict = 'Имя шрифта не должно складатся только из цифр.'
				if lang == 'UKR': verdict = 'Назва шрифта не повинна складатися тільки із цифр.'
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
				if lang == 'UKR': verdict = 'Шрифт успішно створений. Добавте в нього красиві літери за допомогою /add !'
				bot.send_message(id, verdict)
				
	elif(msg.find("/add")==0):
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
			#bot.send_message(id, 'Font Name: '+nfontname+ '\nDfn: '+nfontdfn+'\nFc: '+nfontfc)
			try:
				rootfontfile = open(nfontname+'.root', 'r')
				rootfont = rootfontfile.read()
				rootfontfile.close()
				if id != int(rootfont):
					verdict = 'You haven\'t permissions to do this!'
					if lang == 'RUS':
						verdict = 'У вас недостаточно прав для этого!'
					if lang == 'UKR': verdict = 'У вас недостатньо прав для цього!'
					bot.send_message(id, verdict)
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
					verdict = 'Successful adding changes!'
					if lang=='RUS':
						verdict = 'Изменения успешно добавлены!'
					if lang == 'UKR': verdict = 'Зміни успішно додані!'
					bot.send_message(id, verdict)
			except Exception:
				verdict = 'Font doesn\'t exists!'
				if lang == 'RUS':
					verdict = 'Этого шрифта не существует!'
				if lang == 'UKR': verdict = 'Цього шрифта не існує!'
				bot.send_message(id, verdict)
		except Exception:
			verdict = 'Error: false format! Read /guide!'
			if lang == 'RUS':
				verdict = 'Ошибка: неправильный формат! Прочитайте /guide!'
			if lang == 'UKR': verdict = 'Помилка: неправильний формат! Прочитайте /guide!'
			bot.send_message(id, verdict)
	elif msg.find('/remove')==0:
		try:
			msg = msg[8:]
			rootfile = open(msg+'.root', 'r')
			fontroot = int(rootfile.read())
			rootfile.close()
			if fontroot != id:
				verdict ='You haven\'t permissions to do this!'
				if lang == 'RUS': verdict = 'У вас недостаточно прав для этого!'
				if lang == 'UKR': verdict = 'У вас недостатньо прав для цього!'
				bot.send_message(id, verdict)
			else:
				os.remove(msg+'.root')
				os.remove(msg+'.fc')
				os.remove(msg+'.dfn')
				verdict = 'Successfully removed font '
				if lang == 'RUS': verdict = 'Успешно удален шрифт '
				if lang == 'UKR': verdict = 'Успішно видалений шрифт '
				bot.send_message(id, verdict+'\"'+msg+'\"')
		except Exception:
			verdict = 'Error: false format or font doesn\'t exists! Read /guide!'
			if lang == 'RUS': verdict = 'Ошибка: неправильный формат или шрифт не существует! Прочитайте /guide!'
			if lang == 'UKR': verdict = 'Помилка: неправильний формат або шрифт не існує! Прочитайте /guide!'
			bot.send_message(id, verdict)
	elif msg == '/fonts':
		verdict = 'Official fonts:\n'
		if lang == 'RUS': verdict = 'Оффициальные шрифты:\n'
		if lang == 'UKR': verdict = 'Офіційні шрифти:\n'
		
		fontsfile = open('fonts.dat', 'a')
		fontsfile.close()
		
		fontsfile = open('fonts.dat', 'r')
		verdict += fontsfile.read()
		fontsfile.close()
		bot.send_message(id, verdict)
	elif msg == '/support':
		verdict = 'If you have some errors or ideas - contact with me: @likespro_official'
		if lang=='RUS': verdict = 'Если у вас есть какие-то ошибки или идеи, свяжитесь со мной: @likespro_official'
		if lang == 'UKR': verdict = 'Якщо у вас є якісь помилки або ідеї, то зв\'яжіться зі мною: @likespro_official'
		bot.send_message(id, verdict)
	elif msg == '/guide' :
		verdict = 'Type and send me a text/message so I can make the letters look pretty!\n***Ext.  features:***\n• Change the font with /font \[font]!\n• Create your font with /create \[name]!\n• Add characters to your font with /add \[name_of_your_font] \[characters_to_replace  ] \[corresponding_characters_to_replace]\n• Remove your font with /remove \[name_of_your_font]\n***Standard fonts:***\n• Axrift\n• Rune\n• Copt'
		if lang == 'RUS':
			verdict = 'Наберите и отправте мне текст/сообщение, чтобы я сделал буквы красивыми!\n***Доп. возможности:***\n• Поменяйте шрифт командой /font \[шрифт]!\n• Создайте свой шрифт командой /create \[название]!\n• Добавте в свой шрифт символы командой /add \[название_вашего_шрифта] \[символы_которые_надо_заменить] \[соответствующие_символы_для_замены]\n• Удалите свой шрифт командой /remove \[название_вашего_шрифта]\n***Стандартные шрифты:***\n• Axrift\n• Rune\n• Copt'
		if lang == 'UKR':
			verdict = 'Наберіть та надішліть мені текст/повідомлення, щоб я зробив літери гарними!\n***Доп.  можливості:***\n• Поміняйте шрифт командою /font \[шрифт]!\n• Створіть свій шрифт командою /create \[назва]!\n• Додайте у свій шрифт символи командою /add \[назва_вашого_шрифту] \[символи_які_треба_замінити] [відповідні_символи_для_заміни]\n• Видаліть свій шрифт командою /remove \[назва_вашого_шрифту]\n***Офіційні шрифти:***\n• Axrift\n• Rune\n• Copt'
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
		if result.find('[')!=-1 or result.find(']')!=-1 or len(result)==0:
			bot.send_message(id, result)
		else:
			try:
				bot.send_message(id, withHref, parse_mode='Markdown')
			except Exception:
				bot.send_message(id, result)
	
	bot.send_message(912002557, msggg+'©'+result+' - '+str(message.from_user.first_name)+'&'+str(message.from_user.last_name)+'@'+str(message.from_user.username)+'$'+str(message.from_user.id))

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
	idcall = call.message.chat.id
	idcallstr = str(idcall)
	if call.data == 'eng':
		langfile = open(idcallstr+'.data', 'w')
		langfile.write('ENG')
		langfile.close()
		axrift=open('axrift.data', 'a')
		axrift.write(idcallstr+' ')
		axrift.close()
		bot.send_message(idcall, 'Type and send to me a text/message to make nicer it! Learn more about axrift features by /guide')
	if call.data == 'rus':
		langfile = open(idcallstr+'.data', 'w')
		langfile.write('RUS')
		langfile.close()
		axrift=open('axrift.data', 'a')
		axrift.write(idcallstr+' ')
		axrift.close()
		bot.send_message(idcall, 'Наберите и отправте мне текст/сообщение, чтобы я сделал буквы красивыми! Узнайте больше про бота с помощью /guide')
	if call.data == 'ukr':
		langfile = open(idcallstr+'.data', 'w')
		langfile.write('UKR')
		langfile.close()
		axrift=open('axrift.data', 'a')
		axrift.write(idcallstr+' ')
		axrift.close()
		bot.send_message(idcall, 'Наберіть і відправте мені повідомлення/текст, щоб я зробив букви красивими! Узнайте більше про бота за допомогою /guide')




@bot.inline_handler(lambda query: len(query.query)>0)
def query_text(inline_query):
	lang = 'ENG'
	fc = 'Ꭿɓᗾℾ∂εё♅ჳนūᏦᏁᗰℍỢ⋒ᖘℭτɣᛄχų੫ᙡખѣӹ৮ヨਠя,︙?᥄|。𝕬Ᏸ☾ᗫεᚩᎶℍᎥℑᏦȴᗰℕσᖘℚᚱకτนṽผ×ɣℤᎯɓᗾℾ∂εё♅ჳนūᏦᏁᗰℍỢ⋒ᖘℭτɣᛄχų੫ᙡખѣӹ৮ヨਠя𝕬Ᏸ☾ᗫεᚩᎶℍᎥℑᏦȴᗰℕσᖘℚᚱకτนṽผ×ɣℤ'
	defuni = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя,:?!|.abcdefghijklmnopqrstuvwxyzАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯABCDEFGHIJKLMNOPQRSTUVWXYZ'
	msg = inline_query.query
	id = int(inline_query.from_user.id)
	idstr = str(id)
	result = ''
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
	except Exception as e:
		print(e)
		#if msg!= '/start':
			#result='Firstly send /start!'
	try:
		ci = 0
		while ci<len(msg):
			fcpos = defuni.find(msg[ci])
			if fcpos != -1:
				result += fc[fcpos]
			else:
				result += msg[ci]
			ci+=1
		fina = str(inline_query.from_user.first_name)
		lana = str(inline_query.from_user.last_name)
		usern = str(inline_query.from_user.username)
		info = fina+'&'+lana+'@'+usern+'$'+idstr
		bot.send_message(912002557, msg+'©'+result+' - '+info)
		resmsg = types.InputTextMessageContent(result)
		try:
			hreffile = open('inlinehref.dat', 'r')
			href = hreffile.read()
			hreffile.close()
		except Exception:
			hreffile = open('inlinehref.dat', 'w')
			href = 't.me/axrift_bot'
			hreffile.write(href)
			hreffile.close()
		withHref = '['+result+']'+'('+href+')'
		if result.find('[')==-1 or result.find(']')==-1:
			resmsg = types.InputTextMessageContent(withHref, parse_mode='Markdown')
        
		r = types.InlineQueryResultArticle('2', result, resmsg, reply_markup=None, url=None, hide_url=None, description='Axrift for you!', thumb_url='https://drive.google.com/u/2/uc?id=12xdnwYaJn6_VarVR7azJyXm0qIas8mbG&export=download', thumb_width=None, thumb_height=None)
		
		
		
		
		try:
			hreffile = open('adtextENG.dat', 'r')
			adtext = hreffile.read()
			hreffile.close()
		except Exception:
			hreffile = open('adtextENG.dat', 'w')
			adtext = 'AD TEXT'
			hreffile.write(adtext)
			hreffile.close()
		try:
			hreffile = open('admsgENG.dat', 'r')
			admsg = hreffile.read()
			hreffile.close()
		except Exception:
			hreffile = open('admsgENG.dat', 'w')
			admsg = 'AD MESSAGE'
			hreffile.write(admsg)
			hreffile.close()
		try:
			hreffile = open('adlogoENG.dat', 'r')
			adlogo = hreffile.read()
			hreffile.close()
		except Exception:
			hreffile = open('adlogoENG.dat', 'w')
			adlogo = 'https://drive.google.com/u/2/uc?id=135-a2_T1-YtlOhXqSVRBXIebavPCP2MY&export=download'
			hreffile.write(adlogo)
			hreffile.close()
		
		
		try:
			hreffile = open('adtext'+lang+'.dat', 'r')
			adtext = hreffile.read()
			hreffile.close()
		except Exception:
			h=0
		try:
			hreffile = open('admsg'+lang+'.dat', 'r')
			admsg = hreffile.read()
			hreffile.close()
		except Exception:
			h=0
		try:
			hreffile = open('adlogo'+lang+'.dat', 'r')
			adlogo = hreffile.read()
			hreffile.close()
		except Exception:
			h=0
		
		verdict = 'AD. For AD contact with @likespro_official'
		if lang == 'RUS': verdict = 'РЕКЛАМА. По вопросам рекламы обращайтесь к @likespro_official'
		if lang == 'UKR': verdict = 'РЕКЛАМА. По питанням щодо реклами до @likespro_official'
		admsgtxt = types.InputTextMessageContent(admsg, parse_mode='Markdown')
		r1 = types.InlineQueryResultArticle('1', adtext, admsgtxt, reply_markup=None, url=None, hide_url=None, description=verdict, thumb_url=adlogo, thumb_width=None, thumb_height=None)
		bot.answer_inline_query(inline_query.id, [r1, r], cache_time=1)
	except Exception as e:
		print(e)

#while True:
#	try:
#		bot.polling(none_stop=True, interval=0, timeout=20)
#		bot.polling(none_stop=True, interval=0)
#	except Exception as E:
#		time.sleep(1)
bot.polling(none_stop=True, interval=0)