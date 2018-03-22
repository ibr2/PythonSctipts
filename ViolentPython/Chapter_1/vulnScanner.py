import socket
import os
import sys



def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except Exception, e:
        print "[!] Error = " + str(e)
        return

def checkVuln(banner):
    # os.chdir('C:\\PentesterAcademy\\Violent Python')
    file = open("vuln_banners.txt", "r")
    for line in file.readlines():
        if line.strip("\n") in banner:
            print "[+] Server is vulnerable: " + banner.strip("\n")


def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print "[-] "+ filename + "doesn't exist. "
            exit(0)
        if not os.access(filename, os.R_OK):
            print "[-] "+ filename + " access denied"
            exit(0)
        print "[+] Reading Vulnerability From: "+ filename

    else:
        print "[-] Usage " + str(sys.argv[0]) + " <vuln filename>"
        exit(0)

    portList = [21,22,25,80,110,443]
    for x in range(1,255):
        ip = "208.118.235."+str(x)
        for port in portList:
            banner = retBanner(ip,port)
            if banner:
                print "[+] "+ ip + ": " + banner
                checkVuln(banner)


if __name__ == '__main__':
    main()




