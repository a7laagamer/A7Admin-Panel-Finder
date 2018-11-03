#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[32m'

from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1


def findAdmin():
	f = open("link.txt","r");
	link = raw_input("\n[*] Enter the site link : example ( www.myunlockstore.com )\n\n ==> ")
	print bcolors.BOLD + "\n\n[!] please wait ... \n"
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "[✔] Found : ",req_link
def Credit():
	Space(9); print bcolors.UNDERLINE + "#####################################"
	Space(9); print bcolors.UNDERLINE + "#      --- A7Admin Finder ---       #"
	Space(9); print bcolors.UNDERLINE + "#     --- Admin Panel Finder ---    #"
	Space(9); print bcolors.UNDERLINE + "#       --- Abn-Alhacker ---        #"
	Space(9); print bcolors.UNDERLINE + "#      Telegram : @a7laaG4          #"
	Space(9); print bcolors.UNDERLINE + "#      Telegram : @a7IaaG           #"
	Space(9); print bcolors.UNDERLINE + "#      WhatsApp : +964622348025     #"
	Space(9); print bcolors.UNDERLINE + "#####################################"

Credit()
findAdmin()
