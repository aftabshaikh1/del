import getpass
import telnetlib

HOST = input("Please enter ip of your device  : ")
user = input("Enter your telnet login name  : ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"term length 0\n")
tn.write(b"sh run\n")
tn.write(b"exit\n")
var1 = tn.read_all().decode('ascii')

print(var1)

