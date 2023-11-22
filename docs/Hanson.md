# Setting Up Rasp Pi OS

## Download the OS Image 
I downloaded the light version(about 450 MB)
## Install `qemu`
Since my laptop is x86 and Rasp Pi OS is Arm, I cannot chroot into it natively. I need qemu
## Chrooting
I downloaded 64-bit OS, and after chrooting
```
sudo chroot /run/media/$USER/rootfs /usr/bin/qemu-aarch64-static /bin/bash
```
I couldn't do basic commands like `ls`, `cd`.

## Registering the Architecture
So after checking the folder
```
ls /proc/sys/fs/binfmt_misc/
```
I found the `qemu-aarch64` isn't registered so I manually register it
```
echo ':qemu-aarch64:M::\x7fELF\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\xb7:\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xff\xff:/usr/bin/qemu-aarch64-static:' | sudo tee /proc/sys/fs/binfmt_misc/register
```
## Adding the Wifi Service
After chrooting, I can run commands now.

I add the wifi service to automatically connect to Berkeley Eduroam. So I add a service `/etc/systemd/system/connectwifi.service`
```
[Unit]
Description=Connect to BerkeleyEduroam
After=network.target

[Service]
Type=oneshot
ExecStartPre=/bin/sleep 30
ExecStart=/usr/local/bin/connectwifi.sh
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
```
The `/usr/local/bin/connectwifi.sh` is listed as below
```
#!/bin/bash
ip a > /home/pi/ipname

# Delete existing BerkeleyEduroam profile if it exists and re-add it
nmcli connection delete BerkeleyEduroam

nmcli con add con-name 'BerkeleyEduroam' \
ifname wlan0 \
type wifi \
ssid 'eduroam' \
wifi-sec.key-mgmt wpa-eap \
802-1x.eap peap \
802-1x.identity 'jimchen@berkeley.edu' \
802-1x.password '7%QGZ,Ad' \
802-1x.phase2-auth mschapv2

# Attempt to connect to BerkeleyEduroam
nmcli con up 'BerkeleyEduroam'

# Wait a bit for the first connection to establish (optional)
sleep 10

# Delete existing Flats Lounge profile if it exists and re-add it
nmcli connection delete "Flats Lounge"

# Add a new Wi-Fi connection for "Flats Lounge"
nmcli con add con-name "Flats Lounge" \
ifname wlan0 \
type wifi \
ssid "Flats Lounge" \
wifi-sec.key-mgmt wpa-psk \
wifi-sec.psk "5105405454"

# Attempt to connect to Flats Lounge
nmcli con up "Flats Lounge"

```
## Adding a Sanity Check

When I tried using nmap to find the ip to ssh into it returned dozens of addresses and I couldn't find the appropriate one. 

To make a sanity check to see if Rasp Pi is connected to wifi, I added another service, I post the ip address online every minute

```
[Unit]
Description=Send notification to webhook.site
After=network-online.target
Wants=network-online.target

[Service]
Type=oneshot
ExecStart=/usr/local/bin/send_webhook.sh

[Install]
WantedBy=multi-user.target
```
I used webhook, and the script
```
#!/bin/bash

IP_ADDRESS=$(ip addr show wlan0 | grep "inet\b" | awk '{print $2}' | cut -d/ -f1)

curl -X POST 	https://webhook.site/1df23e04-05ec-47c1-abc6-145c16679683 -d "ip=$IP_ADDRESS"
```
