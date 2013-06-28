import json
import urllib2
import base64
import os
import glob
from configobj import ConfigObj
import logging
import time
import traceback
import sys
import re

zendesk_config = ConfigObj('config.txt')

sitename = zendesk_config.get('sitename')
username = zendesk_config.get('username')
password = zendesk_config.get('password')


articles = open('articles.txt')
logging.basicConfig(filename="move.log", level=logging.INFO)

def move_article(article_id,forum_id):
 
  #   print filecontent
    data = {"topic": {"forum_id": forum_id}}
    jsondata = json.dumps(data)
    current_page_edit_url = sitename + '/api/v2/topics/' + str(article_id) + '.json'
  #  print current_page_edit_url
  #  logging.info("moving " + current_page_edit_url)

    req = urllib2.Request(url=current_page_edit_url, data = jsondata, headers={'Content-Type': 'application/json'})
    base64string = base64.encodestring('%s:%s' % (username,password)).replace('\n','')
    req.add_header("Authorization","Basic %s" % base64string)
    req.get_method = lambda: 'PUT'
    
    try:
	result = urllib2.urlopen(req)
    except Exception, err:
    	print traceback.format_exc()


#http://ctf.help.collab.net/entries/23504762-Work-with-Gerrit
#http://ctf.help.collab.net/forums/21963311-GIT-Integration


forum_url = raw_input("Enter the URL of the Forum to move the links in articles.txt :  [Give Full URL of the Forum] \n")
forum = re.findall("[0-9]+",forum_url)
forum_id = str(forum[0])

for article in articles:
    article_id = re.findall("[0-9]+",article) 
    move_article(str(article_id[0]),forum_id)
    print "moved article " + str(article_id[0]) + " to Forum " + str(forum_id)
    logging.info("moved article " + str(article_id[0]) + " to Forum " + str(forum_id))





time.sleep(1)
