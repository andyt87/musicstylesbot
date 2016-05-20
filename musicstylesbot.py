import telepot
import time
from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen, HTTPError

base_url='http://www.last.fm/music/' #we are using last.fm style tags

def handle(msg):
	chat_id=msg['chat']['id']
	band=msg['text'].encode("UTF-8")	
	print 'band name: %s' % band
	
	if band != '/start':
		m = []
		url=base_url+band.replace(' ','+')

		try:
			html_doc = urlopen(url).read()
			soup = BeautifulSoup(html_doc)
			result = soup.findAll('li', {'class': 'tag'})
			for tag in result:
				m.append(tag.text)
			style = ', '.join(m)
			if style:
				print '%s' % style
				bot.sendMessage(chat_id, style)
			else:
				bot.sendMessage(chat_id, "i don't know :)")

		except HTTPError:
			bot.sendMessage(chat_id, "not found")

bot=telepot.Bot('****') #your telegram bot token must be here
bot.message_loop(handle)

if __name__ == '__main__':
	while 1:
		time.sleep(5)