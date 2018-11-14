import requests, re
from bs4 import BeautifulSoup
from googlesearch import search
urls = []
search_results = search("emails")
for result in search_results:
    urls.append(result)
print(urls)
emails = []
numbers = []
visited_urls = []
mailsrch = re.compile(r'[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4}')
telsrch = re.compile(r'(\(\d{3}\)\s*\d{3}-\d{4})')
tellsrch = re.compile(r'(\([0-9]+\) [0-9]+-[0-9]+)')
urlsrch = re.compile(r'(?P<url>https?://[^\s]+)')
f = open('emails.txt','w')
t = open('numbers.txt','w')
print('1)Быстрый(1мин),2)Средний(3мин),3)Долгий(25мин)')
s = int(input())
k = 1000
if s == 1:
    k = 100
if s == 2:
    k = 1000
if s == 3:
    k = 5000
for i in range(k):
    try:
        data = requests.get(urls[0])
    except:
        urls.remove(urls[0])
        continue
    soup = BeautifulSoup(data.text,'html.parser')
    for a in soup.find_all('a',href=True):
        if re.search("(?P<url>https?://[^\s]+)", a['href']):
            if re.search("(?P<url>https?://[^\s]+)", a['href']).group("url") not in urls and re.search("(?P<url>https?://[^\s]+)", a['href']).group("url") not in visited_urls:
                urls.append(re.search("(?P<url>https?://[^\s]+)", a['href']).group("url"))
    emails.extend(mailsrch.findall(data.text))
    emails = list(set(emails))
    numbers.extend(telsrch.findall(data.text))
    numbers.extend(tellsrch.findall(data.text))
    numbers = list(set(numbers))
    visited_urls.append(urls[0])
    urls.remove(urls[0])
    print(urls)
    print(emails)
    print(numbers)
mails = []
for m in emails:
    if '.ru' in m or '.com' in m or '.net' in m:
        mails.append(m)
f.write('\n'.join(mails))
f.close()
ks = 0
phones = []
while ks < len(numbers):
    if len(numbers[ks]) > 12:
        phones.append('8 ' + numbers[ks])
    ks += 1
t.write('\n'.join(phones))
t.close()