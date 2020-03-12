#-*- coding: utf-8 -*-

import requests
import colorama
import sys
import os
f = open("dork.txt", "r").read().split("\n")
page = 1
# define how many pages to look in
def helper4():
	
	banner = """\033[94m
                             _       _       _  ___ _ _____      
███╗░░██╗░█████╗░███╗░░██╗░█████╗░░██████╗███████╗░█████╗░
████╗░██║██╔══██╗████╗░██║██╔══██╗██╔════╝██╔════╝██╔══██╗
██╔██╗██║███████║██╔██╗██║██║░░██║╚█████╗░█████╗░░██║░░╚═╝
██║╚████║██╔══██║██║╚████║██║░░██║░╚═══██╗██╔══╝░░██║░░██╗
██║░╚███║██║░░██║██║░╚███║╚█████╔╝██████╔╝███████╗╚█████╔╝
╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░╚═════╝░╚══════╝░╚════╝░ 
                                                            
		  
	"""
helper4()
os.system('clear')
PageDepth = int(input('\033[94m How many pages to scrape? '))
for dork in f:
    if dork == "":
        continue
    for k in range(0, PageDepth):
        bingurl = "https://www.bing.com/search?q=" + dork +"&first=" + str(page) + "&FORM=PERE"
        page += 10
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
        try:
            pageSource = requests.get(bingurl, headers=headers).text
        except requests.exceptions.HTTPError:
            continuecontinue
        except requests.exceptions.ConnectionError:
            continue
        except requests.exceptions.Timeout:
            continue
        da = pageSource.split('<li class="b_algo"><h2><a href="')
        domains = []
        for i in range(0, 10):
            try:
                domains.append(da[i+1].split('"')[0])
            except:
                pass
        for l in domains:
            open('Bing_Result.txt', 'a+').close()
            l = l.split('/')
            l = l[0] + '//' + l[1] + l[2]
            if l not in open('Bing_Result.txt', 'r').read():
                open('Bing_Result.txt', 'a+').write(l + '\n')
                print(l)
print("Done")