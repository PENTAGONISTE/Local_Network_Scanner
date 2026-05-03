from scapy.all import Ether, ARP, srp, conf, get_if_addr # type: ignore
import requests # type: ignore
import time
import json

conf.sniff_promisc = False

my_IP = get_if_addr(conf.iface)
numbers = my_IP.split(".")
numbers[3] = "0/24"
net_ip = ".".join(numbers)


packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=net_ip)

ans, unans = srp(packet,inter=0.2, timeout=2, retry=1)

devices = {}

for send, receive in ans:
    devices[receive.hwsrc] = {"IP" : receive.psrc}
    
def get_mac_vend(mac_add):
    url = "https://api.macvendors.com/"
    try:
        response = requests.get(url+mac_add)
        
        if response.status_code == 200:
            return response.content.decode()
        elif response.status_code == 404:
            return "Unknown vendor"
        else:
            return f"Error {response.status_code}"
    except requests.exceptions.RequestException:
        print("connection error")
    

for mac_add in devices.keys():
    vendor = get_mac_vend(mac_add)
    devices[mac_add]["vendor"] = vendor
    time.sleep(2)
    


print("[*] Scan Complete. Saving database...")

with open("scan_results.json", "w") as f:
    json.dump(devices, f, indent=4)

print(json.dumps(devices, indent=4)) 
    
