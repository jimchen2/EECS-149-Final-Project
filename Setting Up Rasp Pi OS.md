# Setting Up Rasp Pi OS

## Download the OS Image 
## Install Qemu
Since my laptop is x86 and Rasp Pi OS is arm, I cannot chroot into it natively. Instead I need qemu
## Chrooting
I downloaded 64-bit OS, and after chrooting
```
sudo chroot /run/media/jimchen/rootfs /usr/bin/qemu-aarch64-static /bin/bash
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
