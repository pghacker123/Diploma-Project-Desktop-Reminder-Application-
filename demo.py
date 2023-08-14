
import time

from bs4 import BeautifulSoup
from plyer import notification


with open('dict1.xml','r', encoding='utf-8') as f: 
    xml_data = f.read()
sp = BeautifulSoup(xml_data,"xml")
word_list = sp.find_all('item')
word_list = word_list[1:0]  # give us news from 0 to 10

for word in word_list:
        notification.notify(
            title="Notification Reminder With Word",
            message =word.title.text,
            app_icon="p2.ico",
            timeout = 20)

time.sleep(10)