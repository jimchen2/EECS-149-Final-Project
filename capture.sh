libcamera-vid -n -t 0 --width 1280 --height 960 --framerate 1 --inline --listen -o tcp://127.0.0.1:9999


mypython detect.py --source=tcp://127.0.0.1:9999 --weights /home/pi/best.pt
