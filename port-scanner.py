import socket
from pythonping  import ping
import pyfiglet

banner = pyfiglet.figlet_format("PORTSCANNER", font="digital")
print(banner, "\t\t\t\tv1.0\n")

ip_addr = input("Enter IP address : ")
port_num  = input("Enter port range to be scanned (eg 5-20) : ")

print("<------------------------------------------------------->")
response=ping(target=ip_addr,count=1,verbose=True)
low=int((port_num.split("-",1)[0]))

if("-"  not in port_num):
    con=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    con.settimeout(1)
    status=con.connect_ex((ip_addr,low))
    if status==0:
        print("Port number",low,"is OPEN                                 ---> Hello there !!")
    else:
        print("Port number",low,"is CLOSED")    
    print("\nQuitting...")
    con.close()
    
else:
    high=int((port_num.split("-",1)[1]))
    if (low>high):
        print("!...Specified invalid port range...!") 
    
    else:
        print("Started scanning",ip_addr, "from Port",low,"to",high)
        for port in  range(low,high+1):
            con = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            con.settimeout(0.09)
            status = con.connect_ex((ip_addr,port))
            if status ==  0:
                print("Port number",port,"is OPEN                                 ---> Hello there !!")
            else:
                print("Port number",port,"is CLOSED")
        print("\nQuitting...")
        con.close()
        
    