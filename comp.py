import socket
import os
from dns import reversename, resolver
import socket
import threading


class TestThread(threading.Thread):
    def __init__(self, data, addr):
        threading.Thread.__init__(self)
        self.data = data
        self.addr = addr

    def decode(self, managerq):
        managerq = managerq.decode("utf-8")
        x = managerq.split(";;")
        url = x[2]
        dns = x[1].split(";")
        dns = list(map(lambda d: "jkdsk_dns_" + d, dns))
        return dns, url

    def respond(self, wynik):
        msg = self.data.decode("utf-8") + ";;" + str(wynik)
        byte_message = bytes(msg, "utf-8")
        print(byte_message)
        socko = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        socko.sendto(byte_message, (socket.gethostbyname("manager"), 5000))

    def run(self):
        print(self.addr, self.data)
        [dns, url] = self.decode(self.data)
        # print(dns, url)
        dns_ip = list(map(lambda d: socket.gethostbyname(d), dns))
        tmp_dns = [resolver.Resolver(), resolver.Resolver()]
        tmp_dns[0].nameservers = [dns_ip[0]]
        tmp_dns[1].nameservers = [dns_ip[1]]
        try:
            odp = list(map(lambda d: str(d.query(url, "A")[0]), tmp_dns))
            if odp[0] == odp[1]:
                wynik = 0
            else:
                wynik = 1
            print(dns, dns_ip, odp, wynik)
        except:
            wynik = False

        self.respond(wynik)


node_id = 0


def get_Host_name_IP():
    global node_id

    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        rev_name = reversename.from_address(host_ip)
        rev_dns = str(resolver.query(rev_name, "PTR")[0])
        name = rev_dns[0:rev_dns.find('.')]
        node_id = name[name.rfind('_') + 1:]
        print("Hostname :  ", host_name)
        print("IP : ", host_ip)
        print("DNS : ", rev_dns)
        print("Node id: ", node_id)
    except:
        print("Unable to get Hostname and IP")


get_Host_name_IP()

# Get DNS config (cfg files in same dir (prefix node_id))
os.rename(r'/etc/bind/' + node_id + 'db.dsk', r'/etc/bind/db.dsk')

os.system("service bind9 restart")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", 5000))
while True:
    data, addr = sock.recvfrom(1024)
    test = TestThread(data, addr)
    test.start()
