# -*- coding: utf-8 -*-
import time
import praw
import random
import re
import urllib2
import sys
import traceback
import requests
from pprint import pprint
import sys
print "      __     __ _                            _                        _     _                "
print "     / /    / /| |                          (_)                      | |   (_)               "
print "    / / __ / /_| | ___   __ _  ___  ___ ___  _ _ __     __ _ _ __ ___| |__  ___   _____ _ __ "
print "   / / '__/ / _` |/wow\ / _` |/ _ \/ __/ _ \| | '_ \   / _` | '__/ __| '_ \| \ \ / / _ \ '__|"
print "  / /| | / / (_| | (_) | (_| |  __/ (_| (_) | | | | | | (_| | | | (__| | | | |\ V /  __/ |  "
print " /_/ |_|/_/ \__,_|\___/ \__, |\___|\___\___/|_|_| |_|  \__,_|_|  \___|_| |_|_| \_/ \___|_| "
print "                         __/ |   "
print "                        |___/   "
print "Code written by: /u/peoplma and /u/healdb"
print "Sillines added by: /u/joshtheimpaler"
print "Wow by: /r/dogecoin"
#This was annoying during my testing
#time.sleep(5)

subName = 'dogecoin'
r = praw.Reddit('searchandarchive')
a = 'timestamp:1386460800..1386547200'
b = 'timestamp:'
c = str(1386639720)
d = '..'
e = str(1437240630)
r.config.store_json_result = True
def main():
	def my_range(start, end, step):
		while start <= end:
			yield start
			start += step

	for c in my_range(1386641400, 1437240630, 30):
		f = str(c)
		g = str(c+30)
		search_results = r.search(b+f+d+g, subreddit=subName, syntax='cloudsearch')
		if c == 1437240630:
			print 'Welp, all done here! Stopped at timestamp' , c
			quit()
		else:
			for post in search_results:
				print "I found a post! It is called:" , post
				url= (post.permalink).replace('?ref=search_posts','')
				#pprint(vars(post))
				data= {'user-agent':'archive by /u/healdb'}
				#manually grabbing this file is much faster than loading the individual json files of every single comment, as this json provides all of it
				response = requests.get(url+'.json',headers=data)
				#Create a folder called dogecoinArchive before running the script
				filename='dogecoinArchive/'+post.name
				obj=open(filename, 'w')
				obj.write(response.text)
				obj.close()
				#print post_json
main()
