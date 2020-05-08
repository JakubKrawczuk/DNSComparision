import socket
import os
from dns import reversename, resolver
  
node_id = 0

def get_Host_name_IP():
    global node_id

    try:
        host_name = socket.gethostname() 
        host_ip = socket.gethostbyname(host_name)
        rev_name = reversename.from_address(host_ip)
        rev_dns = str(resolver.query(rev_name,"PTR")[0])
        name = rev_dns[0:rev_dns.find('.')]
        node_id = name[name.rfind('_')+1:]
        print("Hostname :  ",host_name) 
        print("IP : ",host_ip)
        print("DNS : ",rev_dns)
        print("Node id: ", node_id)
    except: 
        print("Unable to get Hostname and IP")

get_Host_name_IP()

#Get DNS config (cfg files in same dir (prefix node_id))

os.system("service bind9 reload")