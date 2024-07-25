#mobile phone vpn
import os
import time
import requests

# Path to your OpenVPN configuration file
vpn_config_path = "/data/data/com.termux/files/home/vpnconfig.ovpn"

def connect_to_vpn():
    # Command to start OpenVPN with the configuration file
    os.system(f"openvpn --config {vpn_config_path} --daemon")

def disconnect_vpn():
    # Command to stop OpenVPN
    os.system("pkill openvpn")

def get_current_ip():
    try:
        response = requests.get('http://httpbin.org/ip', timeout=5)
        return response.json()['origin']
    except requests.RequestException as e:
        print(f"Error getting IP: {e}")
        return None

if __name__ == "__main__":
    while True:
        disconnect_vpn()  # Ensure any existing VPN connection is closed
        time.sleep(5)  # Wait for 5 seconds before reconnecting
        
        connect_to_vpn()  # Connect to VPN
        time.sleep(15)  # Wait for 15 seconds to ensure VPN connection is established
        
        current_ip = get_current_ip()
        if current_ip:
            print(f"Current IP: {current_ip}")
        
        time.sleep(20)  # Stay connected for 20 seconds before reconnecting