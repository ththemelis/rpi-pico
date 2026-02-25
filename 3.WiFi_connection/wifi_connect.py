import network
from time import sleep

SSID = 'IoT'
PASSWORD = 'q1w2E#R$t5y6U&I*'

# Συνάρτηση για την σύνδεση του  RPi Pico W στο δίκτυο που έχουμε ορίσει
# στην μεταβλητή SSID με κωδικό πρόσβασης που έχουμε ορίσει στην μεταβλητή PASSWORD
def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    while wlan.isconnected() == False:
        print('Προσπάθεια σύνδεσης στο δίκτυο ' + SSID)
        sleep(2)
    # Εκτύπωση των παραμέτρων σύνδεσης (ΙΡ, NETMASK, GATEWAY, DNS)
    print(wlan.ifconfig())

connect() # Κλήση της συνάρτησης σύνδεσης στο WLAN