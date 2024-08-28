import subprocess
import ipaddress

def calculate_subnet_ips(ip, subnet_mask):
    network = ipaddress.ip_network(f'{ip}/{subnet_mask}', strict=False)
    return list(network.hosts())

def ping_ip(ip):
    result = subprocess.run(['ping', '-c', '1', ip], stdout=subprocess.PIPE)
    return result.returncode == 0  # Ping başarılıysa 0 döner
