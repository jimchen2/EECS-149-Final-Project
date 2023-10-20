# Setting Up Rasp Pi OS

## Download the OS Image 
I wanted to configure myself so I downloaded the light version(about 450 MB)
## Install Qemu
Since my laptop is x86 and Rasp Pi OS is arm, I cannot chroot into it natively. Instead I need qemu
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
ExecStart=/usr/local/bin/connectwifi.sh
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
```
## Adding a Sanity Check

When I tried using nmap to find the ip to ssh into it returned dozens of addresses and I couldn't find the appropriate one.

To make a sanity check to see if Rasp Pi is connected to wifi, I added another service
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
Curling the URL
```
root@wifi-10-40-196-199:/# cat /usr/local/bin/send_webhook.sh
#!/bin/bash
curl https://webhook.site/da5810be-d59c-4746-962e-bccd2a778cc3
```
