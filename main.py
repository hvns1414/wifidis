import pywifi
from pywifi import const
import time

def scan_networks():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # İlk Wi-Fi adaptörünü seçiyoruz
    iface.scan()  # Ağ taramasını başlat
    time.sleep(5)  # Tarama sonuçlarını bekle
    scan_results = iface.scan_results()

    print(f"{'SSID':<30} {'BSSID':<20} {'Channel':<10} {'Signal Strength':<15}")
    print("=" * 80)

    for network in scan_results:
        ssid = network.ssid
        bssid = network.bssid
        channel = network.freq // 1000
        signal = network.signal
        print(f"{ssid:<30} {bssid:<20} {channel:<10} {signal:<15}")

if __name__ == "__main__":
    print("[*] Scanning for available Wi-Fi networks...")
    scan_networks()
