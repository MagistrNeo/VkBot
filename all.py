import validators
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.exceptions import VkApiError
import time
import re
import threading
from itertools import islice
n1,n2,n3,n4 = 2000000003,2000000005,2000000006,2000000008
admins = [794312655,838744775,814161744,147438490]
lim = {n1:11,n2:6,n3:4,n4:21}
def filer(id:str,path:str) -> bool:
  with open(path) as f:
    clr = f.read()
  if id in clr: return True
  else: return False
alp = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz0123456789') #Множество для проверки в комментариях
def main2(event) -> None:
  if event.type == VkBotEventType.MESSAGE_NEW:
    q = event.obj.message['from_id']
    #Получаю id чата
    z = event.obj.message['peer_id']
    #Выбираю экземпляр класса
    cl = ql[z]
    x = event.obj.message['text']
    q = event.obj.message['from_id']
    a = vk.users.get(user_id=q)[0]
    i1,i2 = a['first_name'],a['last_name']
    namesurname = f'{i1} {i2}'
    y = event.obj.message['conversation_message_id']
    if cl.cond2(x):
      if q not in cl.limit and session.users.get(user_ids=q)[0]['is_closed'] == False:
        #Открываю файл, чтобы достать вип ссылки
        with open(cl.path,'r') as wl:
          vip = wl.read()
          if cl.sort1(vip,y, q, namesurname) == []:
            del cl.vipslovar[q]
            #Открываю файл, чтобы достать обычные ссылки
            with open(cl.path2) as f:
              A = f.read().split()[::-1]
              A = sorted(set(A), key=A.index)
              cl.perevod(q) #Засекаю время и смотрю на флаг
              if cl.slovar[q]:
                cl.sort2(A,y, q, namesurname)
                cl.ts[q] = time.time()
                #Смотрю какие ссылки человек может пропустить
              elif cl.slovar[q] == False:
                pl = cl.sort3(cl.Ax[q],y,q,namesurname)
                cl.ts[q] = time.time()
                #Добавляю ссылку в файл
                if len(pl) == 0: 
                  del cl.slovar[q], cl.ts[q]
                  #Баннер для рекламы
                  #vk.messages.send(peer_id=z, message = namesurname + ', ваша ссылка успешно добавлена.\n\nДля самых быстрых предлагаем услугу 🚀ТУРБО-ВИП🚀 - 200+ лайков за день\n\nПо всем вопросам обращайтесь к админу\n👇\nhttps://vk.com/dianamaysky', attachment = attachment, expire_ttl=300, random_id=0,keyboard=cl.keyboard.get_keyboard())
                  vk.messages.send(peer_id=z, message = namesurname + ', ваша ссылка успешно добавлена\n🚀 У нас можно заказать:\n ✨Услугу вип;\n ✨Бот под ключ;\n ✨Оформление сообщества;\n ✨Создание сайта.\n\nПо всем вопросам обращайтесь к админу\n👇\nhttps://vk.com/dianamaysky',expire_ttl=300, random_id=0,keyboard=cl.keyboard.get_keyboard())
                  #vk.messages.send(peer_id=z, message = namesurname + ', ваша ссылка успешно добавлена.\n\n Мы проводим АКЦИЮ:\nТолько сегодня скидка 20% на услугу 👑ВИП👑\n\nПо всем вопросам обращайтесь к админу\n👇\nhttps://vk.com/dianamaysky', attachment = attachment, expire_ttl=300, random_id=0,keyboard=cl.keyboard.get_keyboard())
                  cl.limit[q] = lim[z]
                  cl.limit={i:i2-1 for i,i2 in cl.limit.items() if i2 != 1}
                  with open(cl.path2,'a') as wr:
                    if cl.ab<6:
                      wr.write(' ' + x)
                      cl.ab+=1
                    else:
                      wr.write('\n'+x)
                      cl.ab = 1
      elif session.users.get(user_ids=q)[0]['is_closed']:
          vk.messages.delete(conversation_message_ids = y,peer_id = z, delete_for_all=1)
          vk.messages.send(peer_id=z, message = namesurname + ', запрещено публиковать ссылку на приватный профиль.',random_id=0,expire_ttl = 300,keyboard=cl.keyboard.get_keyboard())        
      else:
          if z == n3: message = ' ещё НЕ прошло 3 чужих ссылок. Дождитесь.'
          elif z == n1: message = ' ещё НЕ прошло 10 чужих ссылок. Дождитесь.'
          elif z == n4: message = ' ещё НЕ прошло 20 чужих ссылок. Дождитесь.'
          else: message = ' ещё НЕ прошло 5 чужих ссылок. Дождитесь.'
          try: vk.messages.delete(conversation_message_ids = y,peer_id = z, delete_for_all=1)
          except: pass
          vk.messages.send(peer_id=z, message =  '⚠ ' +namesurname + message, random_id=0,expire_ttl = 300,keyboard=cl.keyboard.get_keyboard())
    else:
      cl.cond(x,y, q, namesurname)
def main() -> None:
  for event in longpoll.listen():
    threading.Thread(target=main2,args=(event,)).start()

class like:
  def __init__(self):
    self.mess1,self.mess2,self.mess3 = 'пожалуйста, ЛАЙК на обязательные ссылки 𝓑𝓤𝞟:', 'мы проставляем лайки по 10 последним ссылкам чата','вы пропустили посты'
    self.path,self.path2,self.path3 = 'vipsforlikes.txt','e.txt','Ludil.txt'
    self.keyboard = VkKeyboard(one_time=False)
    self.keyboard.add_button("❤️ПРАВИЛА ЧАТА❤️", VkKeyboardColor.PRIMARY)
    self.keyboard.add_line()
    self.keyboard.add_openlink_button('КОММЕНТАРИИ 3|3','https://vk.me/join/AZQ1dyv6QACC8C5Bv/yK7mou')
    self.keyboard.add_openlink_button('ПОДПИСКА 5|5','https://vk.me/join/AJQ1d3LBaClcmgZHeyQB5x_m')
    self.keyboard.add_line()
    self.keyboard.add_openlink_button('ЛАЙКИ 20|20','https://vk.me/join/AZQ1dwaqQwwXhPUnUwQ6Y50Z')
    self.keyboard.add_line()
    self.keyboard.add_button("✨УСЛУГА VIP✨", VkKeyboardColor.NEGATIVE)
    self.keyboard.add_line()
    self.keyboard.add_button("🚀ТУРБО-VIP🚀", VkKeyboardColor.POSITIVE)
    #self.keyboard.add_line()
    #self.keyboard.add_button("ТЕЛЕГРАМ ПОДПИСКА 3|3", VkKeyboardColor.POSITIVE)
    self.limit,self.slovar,self.ts,self.vipslovar,self.posts,self.Ax,self.viptime = dict(),dict(),dict(),dict(),dict(),dict(),dict()
    self.ab = 1
	
  def check(self,i):
    try: session.likes.getList(owner_id=int(i[i.index('wall')+4:i.find('_',i.index('wall')+4)]),item_id =int(re.findall(r'\d+',i[i.find('wall'):])[1]),type='post')
    except: return False
    else: return True

  def sorting(self,dicton,mes,y,namesurname):
    if any(dicton):
      try: vk.messages.delete(conversation_message_ids = y,peer_id = n1, delete_for_all=1)
      except VkApiError as e: 
        if 'found' in str(e): 
          raise KeyboardInterrupt
      dicton = ''.join('. '.join(str(i) for i in j) + '\n' for j in enumerate(dicton,start = 1))
      vk.messages.send(peer_id=n1, message = f'{namesurname},\n{mes}\n\n{dicton}\n\n⌛ На выполнение: 6 мин после выполнения публикуйте ссылку ПОВТОРНО\n\n=======================\n\n🎯По услуге 𝓑𝓤𝞟, или хотите запустить бота Вконтакте или Телеграм пишите админу: https://vk.com/dianamaysky',expire_ttl=300, random_id=0,keyboard=self.keyboard.get_keyboard())
    elif mes == self.mess2:
      try: vk.messages.delete(conversation_message_ids = y,peer_id = n1, delete_for_all=1)
      except: pass
      vk.messages.send(peer_id=n1, message = f'{namesurname}, вы прошли все ссылки. Размещайте свою ссылку повторно.',expire_ttl = 300, random_id=0,keyboard=self.keyboard.get_keyboard())

  def sort1(self,string:list, y, q, namesurname) -> list:
    string = eval(string).values()
    self.vipslovar[q] = list(filter(lambda i:(session.likes.isLiked(user_id=q,item_id=int(re.findall(r'\d+',i[i.find('wall'):])[1]),type='post',owner_id=int(i[i.index('wall')+4:].split('_')[0]))['liked'] == 0),string))
    self.sorting(self.vipslovar[q],self.mess1,y,namesurname)
    return self.vipslovar[q]

  def sort2(self,string:list, y, q, namesurname) -> list:
    self.Ax[q] = list(islice(filter(lambda i:(self.check(i) and session.likes.isLiked(user_id=q,item_id=int(re.findall(r'\d+',i[i.find('wall'):])[1]),type='post',owner_id=int(i[i.index('wall')+4:].split('_')[0]))['liked'] == 0),string),10))
    self.sorting(self.Ax[q],self.mess2,y,namesurname)
    self.slovar[q]=False

  def sort3(self,string:list, y, q, namesurname) -> list:
    self.posts[q] = list(filter(lambda i:(session.likes.isLiked(user_id=q,item_id=int(re.findall(r'\d+',i[i.find('wall'):])[1]),type='post',owner_id=int(i[i.index('wall')+4:].split('_')[0]))['liked'] == 0),string))
    self.sorting(self.posts[q],self.mess3,y,namesurname)
    return self.posts[q]


  def perevod(self,q) -> bool:
    self.slovar[q] = True if q not in self.slovar else self.slovar[q]
    if q in self.ts and time.time() - self.ts[q] > 360: self.slovar[q] = True

  def cond(self,x, y, q,namesurname):
    if len(x.split()) == 2 and x.split()[0].lower() == 'з' and validators.url(x.split()[1]) and'vk.com' in x.split()[1] and 'wall' in x.split()[1] and filer(str(q),self.path3):
      try: vk.messages.delete(conversation_message_ids = y,peer_id = n1, delete_for_all=1)
      except VkApiError as e: 
        if 'found' in str(e): 
          raise KeyboardInterrupt
      if q in admins or q not in self.viptime or time.time() - self.viptime[q] > 7200:
        with open(self.path,'r') as f:
          vip = eval(f.read())
        vip.update({q:x.split()[1]})
        self.viptime[q] = time.time()
        with open(self.path,'w') as f:
          f.write(str(vip))
        vk.messages.send(peer_id=n1, message = namesurname + ', ваша ссылка успешно добавлена!',random_id=0,expire_ttl = 300,keyboard=self.keyboard.get_keyboard())
      else:
        vk.messages.send(peer_id=n1, message = namesurname + ', Ещё не прошло 2 часа!',random_id=0,expire_ttl = 300,keyboard=self.keyboard.get_keyboard())
    elif self.check(x) == False and validators.url(x):
        try: vk.messages.delete(conversation_message_ids = y,peer_id = n1, delete_for_all=1)
        except: pass
        vk.messages.send(peer_id=n1, message = '⚠ ' + namesurname + ', запрещено публиковать ссылку на несуществующий пост!',random_id=0,expire_ttl = 300,keyboard=self.keyboard.get_keyboard())

    elif len(x.split()) == 1 and x.split()[0].lower() == 'у' and filer(str(q),self.path):
      try: vk.messages.delete(conversation_message_ids = y,peer_id = n1, delete_for_all=1)
      except VkApiError as e: 
        if 'found' in str(e): 
          raise KeyboardInterrupt
      with open(self.path,'r') as f:
        vip = eval(f.read())
        del vip[q]
        with open(self.path,'w') as f:
          f.write(str(vip))
      vk.messages.send(peer_id=n1, message = namesurname + ', ваша ссылка успешно удалена!',random_id=0,expire_ttl = 300,keyboard=self.keyboard.get_keyboard())
    elif 'ПРАВИЛА ЧАТА' in x:
      try: vk.messages.delete(conversation_message_ids = y,peer_id = n1, delete_for_all=1)
      except: pass
      vk.messages.send(peer_id = n1, message =
                        'Вы в ❤️ЛАЙК-ЧАТЕ❤️ \n'
                        '\n'
                        'Здесь мы друг другу, ставим лайки на посты.\n'
                        'Участие в ленте чата - БЕСПЛАТНОЕ.\n'
                        '\n'
                        'Работаем 10 через 10 + отработка ВИП.\n'
                        'Взамен мы просим, поставить Лайки на обязательные посты и посты-ВИП.\n'
                        '\n'
                        'Чем больше лайков в постах, тем больше внимание и активность, интерес пользователей продвигает посты Вашей группы в умной ленте ВК и увеличивает рейтинг \n'
                        '\n'
                        '👇🏻👇🏻👇\n'
                        '\n'
                        '❗️ПРАВИЛА❗️\n'
                        '\n'
                        'В чате работает БОТ и отвечает за все процессы\n'
                        '\n'
      'Разрешается публиковать только ссылку на ПОСТ, ссылки со вложениями удаляются.\n'
      '\n'
      '✅Публиковать свою ссылку можно один раз через 10 чужих ссылок и далее ставить лайк на каждый пост из десяти, что будет выше Вашей ссылки. После этого ссылку надо разместить ПОВТОРНО.\n'
      '\n'
      '❗Запрещается размещать свои ссылки и выходить из чата. Также запрещается размещать свои ссылки на приватные аккаунты и закрытые группы.\n'
      '\n'
      '✅Нельзя размещать ссылки на запрещенный контент в соответствии с пунктом 6.3.4 "Правил пользования сайтом ВКонтакте".'
        , random_id=0,expire_ttl = 300,keyboard=self.keyboard.get_keyboard())
    elif 'УСЛУГА VIP' in x:
        print(namesurname)
        try: vk.messages.delete(conversation_message_ids = y,peer_id = n1, delete_for_all=1)
        except: pass
        vk.messages.send(peer_id = n1, message = '✨УСЛУГА VIP✨\n\n🎯Ссылка закрепляется в чате\n\n🎯Взамен никого проходить не надо\n\n 🎯Ссылку можно менять\n\n'
        '🎯Неделя - 350 рублей\n\n🎯Месяц - 1100 рублей\n\n🎯По всем вопросам обращайтесь к админу\n👇\n https://vk.com/dianamaysky',expire_ttl=24*60*60,random_id=0, keyboard=self.keyboard.get_keyboard())
    elif 'ТУРБО-VIP' in x:
        print(namesurname)
        try: vk.messages.delete(conversation_message_ids = y,peer_id = n1, delete_for_all=1)
        except: pass
        vk.messages.send(peer_id = n1, message = '🚀ТУРБО-ВИП🚀 200+ лайков в день\n\n🎯Ссылка закрепляется в чате\n\n🎯Взамен никого проходить не надо\n\n 🎯Ссылку можно менять\n\n'
        '🎯День - 400 рублей\n\n🎯По всем вопросам обращайтесь к админу\n👇\n https://vk.com/dianamaysky',expire_ttl=24*60*60,random_id=0, keyboard=self.keyboard.get_keyboard())
    elif 'ТЕЛЕГРАМ' in x:
      try: vk.messages.delete(conversation_message_ids = y,peer_id = n1, delete_for_all=1)
      except: pass
      vk.messages.send(peer_id = n1, message = 'Взаимные вступления на каналы 3|3 \n👇\n https://ok.me/88CH1',expire_ttl=300,random_id=0, keyboard=self.keyboard.get_keyboard())
    else:
      if q not in admins:
        try:
            vk.messages.delete(conversation_message_ids = y,peer_id = n1, delete_for_all=1)
            vk.messages.send(peer_id=n1, message = '⚠ ' + namesurname + ', разрешается публиковать только ссылку на 𝝥𝐎𝐂𝐓.'
        ,random_id=0,expire_ttl = 300, keyboard=self.keyboard.get_keyboard())
        except: pass

  def cond2(self, x) -> bool:
    if validators.url(x) and'vk.com' in x and 'wall' in x: return True
    else: return False

class fol:
  def __init__(self):
    self.path,self.path2,self.mess1,self.mess2,self.mess3 = 'vipsforpodpiska.txt','w.txt','пожалуйста, подписка на ссылки 𝓑𝓤𝞟','пожалуйста, подпишитесь на группы','вы пропустили группы'
    self.limit,self.slovar,self.ts,self.vipslovar,self.posts,self.Ax,self.viptime = dict(),dict(),dict(),dict(),dict(),dict(),dict()
    self.keyboard = VkKeyboard(one_time=False)
    self.keyboard.add_button("❤️ПРАВИЛА ЧАТА❤️", VkKeyboardColor.PRIMARY)
    self.keyboard.add_line()
    self.keyboard.add_openlink_button('ЛАЙКИ 10|10','https://vk.me/join/u2oEZSUs8sfLeMy79aqTDzta/IaGSc0Ihb0=')
    self.keyboard.add_openlink_button('КОММЕНТАРИИ 3|3','https://vk.me/join/AZQ1dyv6QACC8C5Bv/yK7mou')
    self.keyboard.add_line()
    self.keyboard.add_openlink_button('ЛАЙКИ 20|20','https://vk.me/join/AZQ1dwaqQwwXhPUnUwQ6Y50Z')
    self.keyboard.add_line() 
    self.keyboard.add_button("✨УСЛУГА VIP✨", VkKeyboardColor.NEGATIVE)
    #self.keyboard.add_line()
    #self.keyboard.add_button("ТЕЛЕГРАМ ПОДПИСКА 3|3", VkKeyboardColor.POSITIVE)
    self.ab = 1


  def sorting(self,dicton,mes, y,namesurname):
    if any(dicton):
      try: vk.messages.delete(conversation_message_ids = y,peer_id = n2, delete_for_all=1)
      except VkApiError as e: 
        if 'found' in str(e): 
          raise KeyboardInterrupt
      dicton = ''.join(['. '.join(str(i) for i in j)+'\n'  for j in enumerate(dicton,start = 1)])
      vk.messages.send(peer_id=n2, message = f'{namesurname},\n{mes}\n\n{dicton}\n\n⌛ На выполнение: 6 мин после выполнения публикуйте ссылку ПОВТОРНО\n\n=======================\n\n🎯По услуге 𝓑𝓤𝞟, или хотите запустить бота Вконтакте или Телеграм пишите админу: https://vk.com/dianamaysky',expire_ttl=300, random_id=0,keyboard=self.keyboard.get_keyboard())
    elif mes == self.mess2:
      try: vk.messages.delete(conversation_message_ids = y,peer_id = n2, delete_for_all=1)
      except: pass
      vk.messages.send(peer_id=n2, message = f'{namesurname}, вы прошли все ссылки. Размещайте свою ссылку повторно.',expire_ttl = 300, random_id=0,keyboard=self.keyboard.get_keyboard())
  def sort1(self,string:list,y, q,namesurname) -> list:
    string = string.split()
    self.vipslovar[q] = list(filter(lambda i:(session.groups.isMember(user_id=q,group_id = i[i.find('@club')+5:]) == 0),string))
    self.sorting(self.vipslovar[q],self.mess1,y,namesurname)
    return self.vipslovar[q]

  def sort2(self,string:list, y, q, namesurname) -> list:
    self.Ax[q] = list(islice(('@club' + str(session.groups.getById(group_id=i[i.find('vk.com/')+7:])[0]['id']) for i in string if self.check(i) and session.groups.isMember(user_id=q,group_id = i[i.find('vk.com/')+7:]) == 0),5))
    self.sorting(self.Ax[q],self.mess2,y,namesurname)
    self.slovar[q]=False

  def sort3(self,string:list, y, q, namesurname) -> list:
    self.posts[q] = list(filter(lambda i:(session.groups.isMember(user_id=q,group_id = i[i.find('@club')+5:]) == 0),string))
    self.sorting(self.posts[q],self.mess3,y,namesurname)
    return self.posts[q]

  def perevod(self,q) -> bool:
    self.slovar[q] = True if q not in self.slovar else self.slovar[q]
    if q in self.ts and time.time() - self.ts[q] > 360: self.slovar[q] = True
    self.posts[q] = []

  def cond(self, x,y, q,namesurname):
    if x == '':
      try: 
        vk.messages.delete(conversation_message_ids = y,peer_id = n2, delete_for_all=1)
        vk.messages.send(peer_id=n2, message = '⚠ ' + namesurname + ', запрещено публиковать ссылки со вложениями.',random_id=0,expire_ttl = 300,keyboard=self.keyboard.get_keyboard())
      except: pass
    elif (session.users.get(user_ids=q)[0]['is_closed'] or fol.check(x) == False) and validators.url(x):
        try: vk.messages.delete(conversation_message_ids = y,peer_id = n2, delete_for_all=1)
        except: pass
        vk.messages.send(peer_id=n2, message = '⚠ ' + namesurname + ', запрещено публиковать ссылку на личную страницу, приватную группу и группу c закрытым количеством подписчиков.',random_id=0,expire_ttl = 300,keyboard=self.keyboard.get_keyboard())
    elif 'ПРАВИЛА ЧАТА' in x:
        try: vk.messages.delete(conversation_message_ids = y,peer_id = n2, delete_for_all=1)
        except: pass
        vk.messages.send(peer_id = n2, message =
                          'Вы в чате 🚀ВЗАИМНЫЕ ВСТУПЛЕНИЯ 5|5🚀\n'
                          '\n'
                          'Здесь мы вступаем друг другу в группы.\n\n'
                          'Участие в ленте чата БЕСПЛАТНОЕ\n'
                          '\n'
                          'Работаем 5 через 5 + отработка 𝓑𝓤𝞟.\n\n'
                          'Взамен мы просим, подписаться на обязательные группы и группы-𝓑𝓤𝞟.\n'
                          '\n'
                          'Чем больше подписчиков в группе, тем больше интерес и активность пользователей.\nЭто помогает продвинуть вашу группу в ленте новостей и увеличить рейтинг \n'
                          '\n'
                          '👇🏻👇🏻👇\n'
                          '\n'
                          '❗️ПРАВИЛА❗️\n'
                          '\n'
                          'В чате работает БОТ и отвечает за все процессы\n'
                          '\n'
        '✅Разрешается публиковать только ссылку на ГРУППУ, ссылки со вложениями удаляются.\n'
        '\n'
        '✅Публиковать свою ссылку можно один раз через 5 чужих ссылок и далее подписываться на каждую группу из пяти, что будет выше вашей ссылки.\nПосле этого ссылку надо разместить ПОВТОРНО.\n'
        '\n'
        '❗Запрещается размещать свою ссылку и выходить из группы,за отписки бан.\n\n❗Запрещается размещать ссылки на приватные группы и группы с закрытым количеством подписчиком.\n'
        '\n'
        '✅Нельзя размещать ссылки на запрещенный контент в соответствии с пунктом 6.3.4 "Правил пользования сайтом ВКонтакте', random_id=0,expire_ttl = 300,keyboard=self.keyboard.get_keyboard())
    elif 'УСЛУГА VIP' in x:
        print(namesurname)
        try: vk.messages.delete(conversation_message_ids = y,peer_id = n2, delete_for_all=1)
        except: pass
        vk.messages.send(peer_id = n2, message = '✨УСЛУГА VIP✨\n\n🎯Ссылка закрепляется в чате\n\n 🎯Взамен никого проходить не надо\n\n 🎯Ссылку можно менять\n\n'
        '🎯Неделя - 400 рублей\n\n 🎯По всем вопросам обращайтесь к админу\n👇\n https://vk.com/dianamaysky',expire_ttl=24*60*60,random_id=0, keyboard=self.keyboard.get_keyboard())
    elif 'ТЕЛЕГРАМ' in x:
      try: vk.messages.delete(conversation_message_ids = y,peer_id = n2, delete_for_all=1)
      except: pass
      vk.messages.send(peer_id = n2, message = 'Взаимные вступления на каналы 3|3 \n👇\n https://ok.me/88CH1',expire_ttl=300,random_id=0, keyboard=self.keyboard.get_keyboard())
    else:
      if q not in admins:
        try:
            vk.messages.delete(conversation_message_ids = y,peer_id = n2, delete_for_all=1)
            vk.messages.send(peer_id=n2, message = f'⚠ {namesurname}, разрешается размещать только ссылку на ГРУППУ! Исправьтесь!'
        ,random_id=0,expire_ttl = 300, keyboard=self.keyboard.get_keyboard())
        except:pass

  def check(self,link):
    try:
        session.groups.getMembers(group_id = link[link.find('vk.com/')+7:])
    except Exception:
        return False
    else:
        return True

  def cond2(self, x) -> bool:
    if validators.url(x) and'vk.com' in x and 'wall' not in x and fol.check(x): return True
    else: return False

class com:
  def __init__(self):
    self.path,self.path2,self.path3 = 'vipsforcomments.txt','e3.txt','Ludic.txt'
    self.mess1,self.mess2,self.mess3 = 'напишите комментарии на посты-𝓑𝓤𝞟. НЕ МЕНЕЕ 5 слов, не считая эмодзи, разделяя слова пробелом','напишите комментарии на обязательные посты. НЕ МЕНЕЕ 5 слов, не считая эмодзи, разделяя слова пробелом.','вы пропустили посты, НЕ МЕНЕЕ 5 слов, не считая эмодзи, разделяя слова пробелом.'
    self.limit,self.slovar,self.ts,self.vipslovar,self.posts,self.Ax,self.viptime = dict(),dict(),dict(),dict(),dict(),dict(),dict()
    self.keyboard = VkKeyboard(one_time=False)
    self.keyboard.add_button("❤️ПРАВИЛА ЧАТА❤️", VkKeyboardColor.PRIMARY)
    self.keyboard.add_line()
    self.keyboard.add_openlink_button('ЛАЙКИ 10|10','https://vk.me/join/u2oEZSUs8sfLeMy79aqTDzta/IaGSc0Ihb0=')
    self.keyboard.add_openlink_button('ПОДПИСКА 5|5','https://vk.me/join/AJQ1d3LBaClcmgZHeyQB5x_m')
    self.keyboard.add_line()
    self.keyboard.add_openlink_button('ЛАЙКИ 20|20','https://vk.me/join/AZQ1dwaqQwwXhPUnUwQ6Y50Z')
    self.keyboard.add_line()
    self.keyboard.add_button("✨УСЛУГА VIP✨", VkKeyboardColor.NEGATIVE)
    #self.keyboard.add_line()
    #self.keyboard.add_button("ТЕЛЕГРАМ ПОДПИСКА 3|3", VkKeyboardColor.POSITIVE)
    self.ab = 1

  def check(self,i):
    try: session.wall.getComments(owner_id=int(i[i.index('wall')+4:i.find('_',i.index('wall')+4)]),post_id =int(re.findall(r'\d+',i[i.find('wall'):])[1]),count=1)
    except: return False
    else: return True

  def sorting(self,string,dicton,mes,y,namesurname,q):
    for i in string:
      n = session.wall.getComments(owner_id=int(i[i.index('wall')+4:i.find('_',i.index('wall')+4)]),post_id =int(re.findall(r'\d+',i[i.find('wall'):])[1]),count=100)['items']
      if str(q) not in str(n): dicton.append(i)
      elif list(filter(lambda j:(len([j2 for j2 in (j['text'].lower().split()) if set(j2) & alp != set()])>4 and str(q) in str(j)),n)) == []:
          dicton.append(i)
    if any(dicton):
      try: vk.messages.delete(conversation_message_ids = y,peer_id = n3, delete_for_all=1)
      except VkApiError as e: 
        if 'found' in str(e): 
          raise KeyboardInterrupt
      dicton = ''.join('. '.join(str(i) for i in j) + '\n' for j in enumerate(dicton,start = 1))
      vk.messages.send(peer_id=n3, message = f'{namesurname},\n{mes}\n\n{dicton}\n\n⌛ На выполнение: 7 мин после выполнения публикуйте ссылку ПОВТОРНО\n\n=======================\n\n🎯По услуге 𝓑𝓤𝞟, или хотите запустить бота Вконтакте или Телеграм пишите админу: https://vk.com/dianamaysky',expire_ttl=300, random_id=0,keyboard=self.keyboard.get_keyboard())

  def sort1(self,string:list, y, q, namesurname) -> list:
    string = eval(string).values()
    self.vipslovar[q] = []
    self.sorting(string,self.vipslovar[q],self.mess1,y,namesurname,q)
    return self.vipslovar[q]

  def sort2(self,string:list, y, q, namesurname) -> list:
    self.Ax[q] = []
    for i in string:
      try:
        if len(self.Ax[q]) > 2: break
        elif self.check(i):
          n = session.wall.getComments(owner_id=int(i[i.index('wall')+4:i.find('_',i.index('wall')+4)]),post_id =int(re.findall(r'\d+',i[i.find('wall'):])[1]),count=100)['items']
          if str(q) not in str(n): self.Ax[q].append(i)
          elif list(filter(lambda j:(len([j2 for j2 in (j['text'].lower().split()) if set(j2) & alp != set()])>4 and str(q) in str(j)),n)) == []:
              self.Ax[q].append(i)
      except: pass
    if any(self.Ax[q]):
      try: vk.messages.delete(conversation_message_ids = y,peer_id = n3, delete_for_all=1)
      except: pass
      s = ''.join('. '.join(str(i) for i in j) + '\n' for j in enumerate(self.Ax[q],start = 1))
      vk.messages.send(peer_id=n3, message = f'{namesurname},\n{self.mess2}\n\n{s}\n\n⌛ На выполнение: 7 мин после выполнения публикуйте ссылку ПОВТОРНО\n\n=======================\n\n🎯По услуге 𝓑𝓤𝞟, или хотите запустить в своём чате такого же БОТА пишите админу: https://vk.com/dianamaysky',expire_ttl=300, random_id=0,keyboard=self.keyboard.get_keyboard())
    self.slovar[q]=False

  def sort3(self,string:list, y, q, namesurname) -> list:
    self.posts[q] = []
    print(self.Ax[q])
    self.sorting(self.Ax[q],self.posts[q],self.mess3,y,namesurname,q)
    return self.posts[q]

  def perevod(self,q) -> bool:
    self.slovar[q] = True if q not in self.slovar else self.slovar[q]
    if q in self.ts and time.time() - self.ts[q] > 420: self.slovar[q] = True
    self.posts[q] = []

  def cond(self,x, y, q,namesurname):
    if len(x.split()) == 2 and x.split()[0].lower() == 'з' and validators.url(x.split()[1]) and'vk.com' in x.split()[1] and 'wall' in x.split()[1] and filer(str(q),self.path3):
      try: vk.messages.delete(conversation_message_ids = y,peer_id = n3, delete_for_all=1)
      except VkApiError as e: 
        if 'found' in str(e): 
          raise KeyboardInterrupt
      if q in admins or q not in self.viptime or time.time() - self.viptime[q] > 7200:
        with open(self.path,'r') as f:
          vip = eval(f.read())
        vip.update({q:x.split()[1]})
        self.viptime[q] = time.time()
        with open(self.path,'w') as f:
          f.write(str(vip))
        vk.messages.send(peer_id=n3, message = namesurname + ', ваша ссылка успешно добавлена!',random_id=0,expire_ttl = 300,keyboard=self.keyboard.get_keyboard())
      else:
        vk.messages.send(peer_id=n3, message = namesurname + ', Ещё не прошло 2 часа!',random_id=0,expire_ttl = 300,keyboard=self.keyboard.get_keyboard())

    elif len(x.split()) == 1 and x.split()[0].lower() == 'у' and filer(str(q),self.path):
      try: vk.messages.delete(conversation_message_ids = y,peer_id = n3, delete_for_all=1)
      except VkApiError as e: 
        if 'found' in str(e): 
          raise KeyboardInterrupt
      with open(self.path,'r') as f:
        vip = eval(f.read())
        del vip[q]
        with open(self.path,'w') as f:
          f.write(str(vip))
      vk.messages.send(peer_id=n3, message = namesurname + ', ваша ссылка успешно удалена!',random_id=0,expire_ttl = 300,keyboard=self.keyboard.get_keyboard())

    elif 'ПРАВИЛА ЧАТА' in x:
        try: vk.messages.delete(conversation_message_ids = y,peer_id = n3, delete_for_all=1)
        except: pass
        vk.messages.send(peer_id = n3, message =
                          'Вы в чате 🚀КОММЕНТАРИЕВ 3|3🚀\n'
                          '\n'
                          'Здесь мы пишем комментарии на посты друг друга.\n\n'
                          'Участие в ленте чата БЕСПЛАТНОЕ\n'
                          '\n'
                          'Работаем 3 через 3 + отработка 𝓑𝓤𝞟.\n\n'
                          'Взамен необходимо написать комментарии на обязательные посты и посты-𝓑𝓤𝞟. Затем разместить свою ссылку ПОВТОРНО.\n'
                          '\n'
                          'Комментарии к посту показывают интерес пользователей и помогают продвинуть группу в ленте новостей.\n'
                          '\n'
                          '👇🏻👇🏻👇\n'
                          '\n'
                          '❗️ПРАВИЛА❗️\n'
                          '\n'
                          'В чате работает БОТ и отвечает за все процессы\n'
                          '\n'
        '✅Разрешается публиковать только ссылку на ПОСТ.\n'
        '\n'
        '✅Комментарий должен включать НЕ МЕНЕЕ 5 СЛОВ, не считая эмодзи, разделяя слова ПРОБЕЛОМ.\n'
        '\n'
        '✅Публиковать свою ссылку можно один раз через 3 чужие ссылки и далее писать комментарий на каждый пост из трёх, что будет выше вашей ссылки.\n\nПосле этого ссылку надо разместить ПОВТОРНО.\n'
        '\n'
        '✅Если приходят посты-𝓑𝓤𝞟, то комментарии на них надо написать в первую очередь. Затем разместить свою ссылку ПОВТОРНО.\n'
        '\n'
        '✅Нельзя размещать ссылки на запрещенный контент в соответствии с пунктом 6.3.4 "Правил пользования сайтом ВКонтакте', random_id=0,expire_ttl = 300,keyboard=self.keyboard.get_keyboard())
    elif 'УСЛУГА VIP' in x:
        print(namesurname)
        try:vk.messages.delete(conversation_message_ids = y,peer_id = n3, delete_for_all=1)
        except:pass
        vk.messages.send(peer_id = n3, message = '✨УСЛУГА VIP✨\n\n🎯Ссылка закрепляется в чате\n\n 🎯Взамен никого проходить не надо\n\n 🎯Ссылку можно менять\n\n'
        '🎯День - 250 рублей\n\n 🎯Неделя - 450 рублей\n\n 🎯Месяц - 1300 рублей\n\n 🎯По всем вопросам обращайтесь к админу\n👇\n https://vk.com/dianamaysky',expire_ttl=24*60*60,random_id=0, keyboard=self.keyboard.get_keyboard())
    elif 'ТЕЛЕГРАМ' in x:
      try: vk.messages.delete(conversation_message_ids = y,peer_id = n3, delete_for_all=1)
      except: pass
      vk.messages.send(peer_id = n3, message = 'Взаимные вступления на каналы 3|3 \n👇\n https://ok.me/88CH1',expire_ttl=300,random_id=0, keyboard=self.keyboard.get_keyboard())
    elif self.check(x) == False and self.cond2(x):
        try:
            vk.messages.delete(conversation_message_ids = y,peer_id = n3, delete_for_all=1)
            vk.messages.send(peer_id=n3, message = '⚠ ' + namesurname + ', разрешается публиковать только ссылки незакрытые для КОММЕНТирования. Исправьтесь!',random_id=0,expire_ttl = 300, keyboard=self.keyboard.get_keyboard())
        except: pass
    else:
      if q not in admins:
        try:
            vk.messages.delete(conversation_message_ids = y,peer_id = n3, delete_for_all=1)
            vk.messages.send(peer_id=n3, message = '⚠ ' + namesurname + ', разрешается публиковать только ссылку на 𝝥𝐎𝐂𝐓.',random_id=0,expire_ttl = 300, keyboard=self.keyboard.get_keyboard())
        except: pass
  def cond2(self, x) -> bool:
    if validators.url(x) and'vk.com' in x and 'wall' in x and self.check(x): return True
    else: return False

class like15:
  def __init__(self):
    self.mess1,self.mess2,self.mess3 = 'пожалуйста, ЛАЙК на обязательные ссылки 𝓑𝓤𝞟:', 'мы проставляем лайки по 20 последним ссылкам чата','вы пропустили посты'
    self.path,self.path2,self.path3 = 'vipsforlikes15.txt','e15.txt','Ludil15.txt'
    self.keyboard = VkKeyboard(one_time=False)
    self.keyboard.add_button("❤️ПРАВИЛА ЧАТА❤️", VkKeyboardColor.PRIMARY)
    self.keyboard.add_line()
    self.keyboard.add_openlink_button('КОММЕНТАРИИ 3|3','https://vk.me/join/AZQ1dyv6QACC8C5Bv/yK7mou')
    self.keyboard.add_openlink_button('ПОДПИСКА 5|5','https://vk.me/join/AJQ1d3LBaClcmgZHeyQB5x_m')
    self.keyboard.add_line()
    self.keyboard.add_openlink_button('ЛАЙКИ 10|10','https://vk.me/join/u2oEZSUs8sfLeMy79aqTDzta/IaGSc0Ihb0=')
    self.keyboard.add_line()
    self.keyboard.add_button("✨УСЛУГА VIP✨", VkKeyboardColor.NEGATIVE)
    self.keyboard.add_line()
    self.keyboard.add_button("🚀ТУРБО-VIP🚀", VkKeyboardColor.POSITIVE)
    #self.keyboard.add_line()
    #self.keyboard.add_button("ТЕЛЕГРАМ ПОДПИСКА 3|3", VkKeyboardColor.POSITIVE)
    self.limit,self.slovar,self.ts,self.vipslovar,self.posts,self.Ax,self.viptime = dict(),dict(),dict(),dict(),dict(),dict(),dict()
    self.ab = 1
	
  def check(self,i):
    try: session.likes.getList(owner_id=int(i[i.index('wall')+4:i.find('_',i.index('wall')+4)]),item_id =int(re.findall(r'\d+',i[i.find('wall'):])[1]),type='post')
    except: return False
    else: return True

  def sorting(self,dicton,mes,y,namesurname):
    if any(dicton):
      try: vk.messages.delete(conversation_message_ids = y,peer_id = n4, delete_for_all=1)
      except VkApiError as e: 
        if 'found' in str(e): 
          raise KeyboardInterrupt
      dicton = ''.join('. '.join(str(i) for i in j) + '\n' for j in enumerate(dicton,start = 1))
      vk.messages.send(peer_id=n4, message = f'{namesurname},\n{mes}\n\n{dicton}\n\n⌛ На выполнение: 6 мин после выполнения публикуйте ссылку ПОВТОРНО\n\n=======================\n\n🎯По услуге 𝓑𝓤𝞟, или хотите запустить бота Вконтакте или Телеграм пишите админу: https://vk.com/dianamaysky',expire_ttl=300, random_id=0,keyboard=self.keyboard.get_keyboard())
    elif mes == self.mess2:
      try: vk.messages.delete(conversation_message_ids = y,peer_id = n4, delete_for_all=1)
      except: pass
      vk.messages.send(peer_id=n4, message = f'{namesurname}, вы прошли все ссылки. Размещайте свою ссылку повторно.',expire_ttl = 300, random_id=0,keyboard=self.keyboard.get_keyboard())

  def sort1(self,string:list, y, q, namesurname) -> list:
    string = eval(string).values()
    self.vipslovar[q] = list(filter(lambda i:(session.likes.isLiked(user_id=q,item_id=int(re.findall(r'\d+',i[i.find('wall'):])[1]),type='post',owner_id=int(i[i.index('wall')+4:].split('_')[0]))['liked'] == 0),string))
    self.sorting(self.vipslovar[q],self.mess1,y,namesurname)
    return self.vipslovar[q]

  def sort2(self,string:list, y, q, namesurname) -> list:
    self.Ax[q] = list(islice(filter(lambda i:(self.check(i) and session.likes.isLiked(user_id=q,item_id=int(re.findall(r'\d+',i[i.find('wall'):])[1]),type='post',owner_id=int(i[i.index('wall')+4:].split('_')[0]))['liked'] == 0),string),20))
    self.sorting(self.Ax[q],self.mess2,y,namesurname)
    self.slovar[q]=False

  def sort3(self,string:list, y, q, namesurname) -> list:
    self.posts[q] = list(filter(lambda i:(session.likes.isLiked(user_id=q,item_id=int(re.findall(r'\d+',i[i.find('wall'):])[1]),type='post',owner_id=int(i[i.index('wall')+4:].split('_')[0]))['liked'] == 0),string))
    self.sorting(self.posts[q],self.mess3,y,namesurname)
    return self.posts[q]


  def perevod(self,q) -> bool:
    self.slovar[q] = True if q not in self.slovar else self.slovar[q]
    if q in self.ts and time.time() - self.ts[q] > 360: self.slovar[q] = True

  def cond(self,x, y, q,namesurname):
    if len(x.split()) == 2 and x.split()[0].lower() == 'з' and validators.url(x.split()[1]) and'vk.com' in x.split()[1] and 'wall' in x.split()[1] and filer(str(q),self.path3):
      try: vk.messages.delete(conversation_message_ids = y,peer_id = n4, delete_for_all=1)
      except VkApiError as e: 
        if 'found' in str(e): 
          raise KeyboardInterrupt
      if q in admins or q not in self.viptime or time.time() - self.viptime[q] > 7200:
        with open(self.path,'r') as f:
          vip = eval(f.read())
        vip.update({q:x.split()[1]})
        self.viptime[q] = time.time()
        with open(self.path,'w') as f:
          f.write(str(vip))
        vk.messages.send(peer_id=n4, message = namesurname + ', ваша ссылка успешно добавлена!',random_id=0,expire_ttl = 300,keyboard=self.keyboard.get_keyboard())
      else:
        vk.messages.send(peer_id=n4, message = namesurname + ', Ещё не прошло 2 часа!',random_id=0,expire_ttl = 300,keyboard=self.keyboard.get_keyboard())
    elif self.check(x) == False and validators.url(x):
        try: vk.messages.delete(conversation_message_ids = y,peer_id = n4, delete_for_all=1)
        except: pass
        vk.messages.send(peer_id=n4, message = '⚠ ' + namesurname + ', запрещено публиковать ссылку на несуществующий пост!',random_id=0,expire_ttl = 300,keyboard=self.keyboard.get_keyboard())

    elif len(x.split()) == 1 and x.split()[0].lower() == 'у' and filer(str(q),self.path):
      try: vk.messages.delete(conversation_message_ids = y,peer_id = n4, delete_for_all=1)
      except VkApiError as e: 
        if 'found' in str(e): 
          raise KeyboardInterrupt
      with open(self.path,'r') as f:
        vip = eval(f.read())
        del vip[q]
        with open(self.path,'w') as f:
          f.write(str(vip))
      vk.messages.send(peer_id=n4, message = namesurname + ', ваша ссылка успешно удалена!',random_id=0,expire_ttl = 300,keyboard=self.keyboard.get_keyboard())
    elif 'ПРАВИЛА ЧАТА' in x:
      try: vk.messages.delete(conversation_message_ids = y,peer_id = n4, delete_for_all=1)
      except: pass
      vk.messages.send(peer_id = n4, message =
                        'Вы в ❤️ЛАЙК-ЧАТЕ❤️ \n'
                        '\n'
                        'Здесь мы друг другу, ставим лайки на посты.\n'
                        'Участие в ленте чата - БЕСПЛАТНОЕ.\n'
                        '\n'
                        'Работаем 20 через 20 + отработка ВИП.\n'
                        'Взамен мы просим, поставить Лайки на обязательные посты и посты-ВИП.\n'
                        '\n'
                        'Чем больше лайков в постах, тем больше внимание и активность, интерес пользователей продвигает посты Вашей группы в умной ленте ВК и увеличивает рейтинг \n'
                        '\n'
                        '👇🏻👇🏻👇\n'
                        '\n'
                        '❗️ПРАВИЛА❗️\n'
                        '\n'
                        'В чате работает БОТ и отвечает за все процессы\n'
                        '\n'
      'Разрешается публиковать только ссылку на ПОСТ, ссылки со вложениями удаляются.\n'
      '\n'
      '✅Публиковать свою ссылку можно один раз через 20 чужих ссылок и далее ставить лайк на каждый пост из двадцати, что будет выше Вашей ссылки. После этого ссылку надо разместить ПОВТОРНО.\n'
      '\n'
      '❗Запрещается размещать свои ссылки и выходить из чата. Также запрещается размещать свои ссылки на приватные аккаунты и закрытые группы.\n'
      '\n'
      '✅Нельзя размещать ссылки на запрещенный контент в соответствии с пунктом 6.3.4 "Правил пользования сайтом ВКонтакте".'
        , random_id=0,expire_ttl = 300,keyboard=self.keyboard.get_keyboard())
    elif 'УСЛУГА VIP' in x:
        print(namesurname)
        try: vk.messages.delete(conversation_message_ids = y,peer_id = n4, delete_for_all=1)
        except: pass
        vk.messages.send(peer_id = n4, message = '✨УСЛУГА VIP✨\n\n🎯Ссылка закрепляется в чате\n\n🎯Взамен никого проходить не надо\n\n🎯Ссылку можно менять\n\n'
        '🎯Неделя - 350 рублей\n\n🎯Месяц - 1100 рублей\n\n🎯По всем вопросам обращайтесь к админу\n👇\n https://vk.com/dianamaysky',expire_ttl=24*60*60,random_id=0, keyboard=self.keyboard.get_keyboard())
    elif 'ТУРБО-VIP' in x:
        print(namesurname)
        try: vk.messages.delete(conversation_message_ids = y,peer_id = n4, delete_for_all=1)
        except: pass
        vk.messages.send(peer_id = n4, message = '🚀ТУРБО-VIP🚀 200+ лайков в день\n\n🎯Ссылка закрепляется в чате\n\n🎯Взамен никого проходить не надо\n\n 🎯Ссылку можно менять\n\n'
        '🎯День - 400 рублей\n\n🎯По всем вопросам обращайтесь к админу\n👇\n https://vk.com/dianamaysky',expire_ttl=24*60*60,random_id=0, keyboard=self.keyboard.get_keyboard())
    else:
      if q not in admins:
        try:
            vk.messages.delete(conversation_message_ids = y,peer_id = n4, delete_for_all=1)
            vk.messages.send(peer_id=n4, message = '⚠ ' + namesurname + ', разрешается публиковать только ссылку на 𝝥𝐎𝐂𝐓.'
        ,random_id=0,expire_ttl = 300, keyboard=self.keyboard.get_keyboard())
        except: pass

  def cond2(self, x) -> bool:
    if validators.url(x) and'vk.com' in x and 'wall' in x: return True
    else: return False
    
#Беру необходимые экземпляры класса
like,fol,com,like15 = like(),fol(),com(),like15()
ql = {n1:like,n2:fol,n3:com,n4:like15}

if __name__ == '__main__':
#Необходимые ключи
  nomer =  #ключ 1
  vk_session = vk_api.VkApi(
          token = nomer)
  vk = vk_session.get_api()
  session2 = vk_api.VkApi(token=) #ключ 2
  longpoll = VkBotLongPoll(vk_session,  '212869892')
  session = session2.get_api()
  
  upload = vk_api.VkUpload(vk_session)
  photo = upload.photo_messages('pi.png')
  photo_data = photo[0]
  owner_id = photo_data['owner_id']
  photo_id = photo_data['id']
  access_key = photo_data['access_key']
  attachment = f'photo{owner_id}_{photo_id}_{access_key}'
  
#Запуск главной функции
  main()