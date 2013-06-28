Script to Mass move the articles in zendesk.com instance
from one forum to another forum.



Required Software:

python-configobj

Install this using the following command in ubuntu/debian

sudo apt-get install python-configobj




How to execute:


1.
Edit the config.txt
add the following stuff

1. Zendesk site URL
2. USername
3. Password

2.
Copy the URLs of the articles you want to move and
paste them in the articles.txt

You can use the addon for firefox 
https://addons.mozilla.org/en-us/firefox/addon/copy-urls-expert/

This will help you to select some content and copy the links in the content to clipboard.

Then, you can paste the URLs in the articles.txt

3.
run the script as
python move-zenesk-article.py

This will ask for the forum you want to move the articles to.

Give the full url of the forum.

Once completed, all the articles will be moved to the forum mentioned.
