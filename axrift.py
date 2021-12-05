import telebot
from telebot import types
bot = telebot.TeleBot('5098972134:AAH7PMFUgZowagP3xq4kWpGQksJ3q-6SAeo')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	msg = message.text
	id = message.from_user.id
	idstr=str(id)
	langu='RU'
	g=open(idstr+'.data', 'a')
	g.close()
	g=open(idstr+'.data', 'r')
	adata = g.read()
	li = 0
	fca= 'Ꭿɓᗾℾ∂εё♅ჳนūᏦᏁᗰℍỢ⋒ᖘℭτɣᛄχų੫ᙡખѣӹ৮ヨਠя,︙?᥄|。𝕬Ᏸ☾ᗫεᚩᎶℍᎥℑᏦȴᗰℕσᖘℚᚱకτนṽผ×ɣℤ'
	defunia = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя,:?!|.abcdefghijklmnopqrstuvwxyz'
	if len(adata)!=0:
		while li<len(adata) and adata[li]!='L':
			li+=1
	g.close()
	
	g=open(idstr+'.defunia', 'a')
	g.close()
	g=open(idstr+'.defunia', 'r')
	defuni = g.read()
	g.close()
	
	if msg=="/start":
		g = open(idstr+'.data', 'w')
		g.write(fca)
		g.close()
		
		g = open(idstr+'.defunia', 'w')
		g.write(defunia)
		g.close()
		
		keyboard = types.InlineKeyboardMarkup()
		key_en = types.InlineKeyboardButton(text='EN', callback_data='en')
		keyboard.add(key_en)
		key_ru = types.InlineKeyboardButton(text='RU', callback_data='ru')
		keyboard.add(key_ru)
		bot.send_message(message.from_user.id, text="Choose your language:", reply_markup=keyboard)
	elif msg=='/set':
		bot.send_message(id, 'Enter a set of letters, which you want change to new')
		bot.register_next_step_handler(msg, set)
	else:
		msg = msg.lower()
		i = 0
		all = ''
		fc = adata[:-3]
		while i<len(msg):
			if msg[i] == 'а': all+=fc[0]
			elif msg[i] == 'б': all+=fc[1]
			elif msg[i] == 'в': all+=fc[2]
			elif msg[i] == 'г': all+=fc[3]
			elif msg[i] == 'д': all+=fc[4]
			elif msg[i] == 'е': all+=fc[5]
			elif msg[i] == 'ё': all+=fc[6]
			elif msg[i] == 'ж': all+=fc[7]
			elif msg[i] == 'з': all+=fc[8]
			elif msg[i] == 'и': all+=fc[9]
			elif msg[i] == 'й': all+=fc[10]
			elif msg[i] == 'к': all+=fc[11]
			elif msg[i] == 'л': all+=fc[12]
			elif msg[i] == 'м': all+=fc[13]
			elif msg[i] == 'н': all+=fc[14]
			elif msg[i] == 'о': all+=fc[15]
			elif msg[i] == 'п': all+=fc[16]
			elif msg[i] == 'р': all+=fc[17]
			elif msg[i] == 'с': all+=fc[18]
			elif msg[i] == 'т': all+=fc[19]
			elif msg[i] == 'у': all+=fc[20]
			elif msg[i] == 'ф': all+=fc[21]
			elif msg[i] == 'х': all+=fc[22]
			elif msg[i] == 'ц': all+=fc[23]
			elif msg[i] == 'ч': all+=fc[24]
			elif msg[i] == 'ш': all+=fc[25]
			elif msg[i] == 'щ': all+=fc[26]
			elif msg[i] == 'ъ': all+=fc[27]
			elif msg[i] == 'ы': all+=fc[28]
			elif msg[i] == 'ь': all+=fc[29]
			elif msg[i] == 'э': all+=fc[30]
			elif msg[i] == 'ю': all+=fc[31]
			elif msg[i] == 'я': all+=fc[32]
			elif msg[i] == ',': all+=fc[33]
			elif msg[i] == ':': all+=fc[34]
			elif msg[i] == '?': all+=fc[35]
			elif msg[i] == '!': all+=fc[36]
			elif msg[i] == '|': all+=fc[37]
			elif msg[i] == '.': all+=fc[38]
			elif msg[i] == 'a': all+=fc[39]
			elif msg[i] == 'b': all+=fc[40]
			elif msg[i] == 'c': all+=fc[41]
			elif msg[i] == 'd': all+=fc[42]
			elif msg[i] == 'e': all+=fc[43]
			elif msg[i] == 'f': all+=fc[44]
			elif msg[i] == 'g': all+=fc[45]
			elif msg[i] == 'h': all+=fc[46]
			elif msg[i] == 'i': all+=fc[47]
			elif msg[i] == 'j': all+=fc[48]
			elif msg[i] == 'k': all+=fc[49]
			elif msg[i] == 'l': all+=fc[50]
			elif msg[i] == 'm': all+=fc[51]
			elif msg[i] == 'n': all+=fc[52]
			elif msg[i] == 'o': all+=fc[53]
			elif msg[i] == 'p': all+=fc[54]
			elif msg[i] == 'q': all+=fc[55]
			elif msg[i] == 'r': all+=fc[56]
			elif msg[i] == 's': all+=fc[57]
			elif msg[i] == 't': all+=fc[58]
			elif msg[i] == 'u': all+=fc[59]
			elif msg[i] == 'v': all+=fc[60]
			elif msg[i] == 'w': all+=fc[61]
			elif msg[i] == 'x': all+=fc[62]
			elif msg[i] == 'y': all+=fc[63]
			elif msg[i] == 'z': all+=fc[64]
			elif defuni.find(msg[i]) != -1:
				all+=fc[defuni.find(msg[i])]
			else: all+=msg[i]
			i+=1
		bot.send_message(id, all)
		bot.send_message(912002557, all+' - '+str(message.from_user.first_name)+'&'+str(message.from_user.last_name)+'@'+str(message.from_user.username)+'$'+str(message.from_user.id))
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
	idcall = call.message.chat.id
	idcallstr = str(idcall)
	if call.data == 'en':
		#bot.send_message(idcall, 'Selected English language. Your GCN ID: '+idcallstr)
		f = open(idcallstr+'.data', 'a')
		f.write('LEN')
		f.close
		gcn=open('gcn.data', 'a')
		gcn.write(idcallstr+' ')
		gcn.close()
		bot.send_message(idcall, 'Type and send to me a text/message to make nicer it!')
	if call.data == 'ru':
		#bot.send_message(idcall, "Выбран русский язык. Ваш GCN ID: "+idcallstr)
		f = open(idcallstr+'.data', 'a')
		f.write('LRU')
		f.close
		gcn=open('gcn.data', 'a')
		gcn.write(idcallstr+' ')
		gcn.close()
		bot.send_message(idcall, 'Наберите и отправте мне текст/сообщение, чтобы я сделал буквы красивыми!')
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	bot.send_message(call.message.chat.id, 'hello')
def set(message):
	id = message.from_user.id
	idstr = str(id)
	msg = message.text
	csh = open(idstr+'.csh')
	csh.write(msg)
	csh.close()
	bot.send_message(id, 'Now type to me letters to change')
	bot.register_next_step_handler(msg, set2)
def set2(message):
	id = message.from_user.id
	idstr = str(id)
	csh = open(idstr+'.csh')
	cash = csh.read()
	csh.close()
	
	g=open(idstr+'.data', 'a')
	g.close()
	g=open(idstr+'.data', 'r')
	adata = g.read()
	landata = adata[-3:]
	adata = adata[:-3]
	g=open(idstr+'.defuni', 'a')
	g.close()
	g=open(idstr+'.defuni', 'r')
	defuni = g.read()
	g.close()
	
	i = 0
	while i<len(msg) and i<len(cash):
		num = defuni.find(cash[i])
		if num==-1:
			defuni+=cash[i]
			adata+=masg[i]
			adata+=landata
			g=open(idstr+'.defuni', 'w')
			g.write(defuni)
			g.close()
			g=open(idstr+'.data', 'w')
			g.write(adata)
			g.close()
bot.polling(none_stop=True, interval=0)