import psutil
import socket
import sys
sys.path.append('../')
import rgb1602
import time

def get_all_interfaces_with_ips(): #Gets all interfaces and their ip
    interface_info = {}

    for interface, addrs in psutil.net_if_addrs().items():
        ip_addresses = []
        for addr in addrs:
            if addr.family == socket.AF_INET:
                ip_addresses.append(addr.address)
        interface_info[interface] = ip_addresses

    return interface_info



lcd=rgb1602.RGB1602(16,2)  #create LCD object,specify col and row
lcd.setRGB(173,216,230) #set backlight in RGB

while True:
        interfaces = get_all_interfaces_with_ips()

        for interface, ip_addresses in interfaces.items():
                lcd.clear() #clears the text on the lcd

                lcd.setCursor(0,0) #Sets the cursor on the 0th column, 0th row position
                lcd.printout(interface) #Displays the interface name

                lcd.setCursor(0,1) #Sets the cursor on the 0th column, 2th row position. aka the second line
                if ip_addresses:
                        lcd.printout(ip_addresses[0]) #Displays the ip of the interface.
                else:
                        lcd.printout("Not connected")

                time.sleep(3) #Wait in seconds before continuing
