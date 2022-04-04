import socket

print("wtire the domain , for example : www.google.com ")

input1 = input()
ip = socket.gethostbyname(input1)

print("the ip for :>" , input1 , "<:" , ip)


