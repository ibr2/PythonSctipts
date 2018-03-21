# Networking and Selection on Chapter 1 [Violent Python]


import socket

socket.setdefaulttimeout(2)
s = socket.socket()
s.connect(("208.118.235.20",21))
banner = s.recv(1024)
print banner
if ("FreeFloat Ftp Server (Version 1.00)" in banner):
    print "[+] FreeFloat FTP Server is vulnerable."
elif ("3Com 3CDaemon FTP Server Version 2.0" in banner):
    print "[+] 3CDaemon FTP Server is vulnerable."
elif ("Ability Server 2.34" in banner):
    print "[+] Ability FTP Server is vulnerable."
elif ("Sami FTP Server 2.0.2" in banner):
    print "[+] Sami FTP Server is vulnerable."
else:
    print "[-] FTP Server is not vulnerable."
