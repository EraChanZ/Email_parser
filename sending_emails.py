import smtplib
from email.mime.text import MIMEText
from email.header import Header
from emails import kek
import time
# Настройки
mail_sender = 'mail'
final_arr = []
for l in kek:
    if '.ru' in l or '.com' in l:
        final_arr.append(l)
mail_receiver = final_arr
print(len(mail_receiver))
username = 'mail'
password = 'pass'
server = smtplib.SMTP('smtp.yandex.ru:587')

# Формируем тело письма
subject = u'Привет от Программиста '
body = u'''Привет, я программист Вова, сразу хочу принести свои извинения за данное спам-письмо. 
Я просто пропарсил 1000 страничек в интернете и получил ваши e-mail адреса.\n
 Могу создать создать сайт с нуля(Без дизайна), на базе Django. Обладаю языками Python , JavaScript. Увлекаюсь анализом данных и нейросетями.\n
  Интересуюсь парсингом , как раз с помощью которого нашёл вашу почту. То есть, что делает это программа:\n 1. Заходит на заданный стартовый сайт 
  , ищет там все ссылки на другие сайты (С помощью библиотеки BeautifulSoup4),\n почты(С помощью регулярных выражений (Библиотека re)) и \n
   номера телефонов таким же способом, а дальше смотрит html-коды всех сайтов которые нашел и повторяет все те же действия . \n
    Далее с помощью другой программы и библиотеки smtplib сделал рассылку на все найденные почты. \n 
    Программу нигде не брал , все написал своими ручками . Просто мне сейчас очень важно практиковать свои программерские навыки , 
    вот и придумываю различные штуки и реализую их.\n  Мне кстати 14 лет) Если у вас найдётся какая-либо работёнка - не стесняйтесь 
    (От веба , до алгоритмов). Также пишу олимпиады по информатике для 11 классов (хотя в 9).\n Я не в коем случае не хвастун , 
    просто очень интересует программирование ,и я уверен что буду связывать свою будущую работу с этим направлением .'''
msg = MIMEText(body, 'plain', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')

# Отпавляем письмо

server.starttls()
server.ehlo()
server.login(username, password)
for offset in range(0,len(mail_receiver),5):
        server.sendmail(mail_sender, mail_receiver[offset:offset+5], msg.as_string())
        time.sleep(10)
        print('succes')
server.quit()
