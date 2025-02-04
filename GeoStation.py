import subprocess
import os
import ctypes
import socket

def is_admin():
    """Check if the program is run as administrator."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def flush_dns():
    """Flush the DNS resolver cache."""
    print("Flushing DNS cache...")
    subprocess.call("ipconfig /flushdns", shell=True)

def optimize_tcp():
    """Optimize TCP settings for better network performance."""
    print("Optimizing TCP settings...")
    commands = [
        "netsh int tcp set heuristics disabled",
        "netsh int tcp set global autotuninglevel=normal",
        "netsh int tcp set global rss=enabled"
    ]
    for command in commands:
        subprocess.call(command, shell=True)

def set_dns_to_google():
    """Set DNS to Google Public DNS."""
    print("Setting DNS to Google Public DNS...")
    adapter_name = get_active_adapter()
    if adapter_name:
        command = f'netsh interface ip set dns "{adapter_name}" static 8.8.8.8'
        subprocess.call(command, shell=True)

def get_active_adapter():
    """Get the name of the active network adapter."""
    print("Retrieving active network adapter...")
    output = subprocess.check_output("netsh interface show interface", shell=True).decode()
    for line in output.split("\n"):
        if "Connected" in line and "Dedicated" in line:
            return line.split()[-1]
    return None

def display_network_info():
    """Display current network information."""
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(f"Hostname: {hostname}")
    print(f"Local IP Address: {local_ip}")

def main():
    if not is_admin():
        print("This program requires administrative privileges.")
        return
    
    print("Welcome to GeoStation - Network Optimization Tool")
    display_network_info()
    
    while True:
        print("\nOptions:")
        print("1. Flush DNS")
        print("2. Optimize TCP")
        print("3. Set DNS to Google Public DNS")
        print("4. Display Network Information")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            flush_dns()
        elif choice == '2':
            optimize_tcp()
        elif choice == '3':
            set_dns_to_google()
        elif choice == '4':
            display_network_info()
        elif choice == '5':
            print("Exiting GeoStation...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()