#!/bin/bash

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

nmcli con up 'BerkeleyEduroam'
