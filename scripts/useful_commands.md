Useful Commands

## Put a video to dropbox
`
dbxcli put /home/pi/Pictures/example.txt /path/to/example.png`

## Capture an image and store it in Pictures folder
`libcamera-still -o /home/pi/Pictures/image_$(date +%s).jpg`

## Capture quickly
`libcamera-still -t 1 -o /home/pi/Pictures/quick_image.jpg`

## Capture low-res image
`libcamera-still --width 640 --height 480 -o /home/pi/Pictures/low_res_image.jpg`

## Other commands
```
--nopreview  		#Without a preview window
--hflip      		#Horizontal Flip:
-q 75 			#Set Specific JPEG Quality
--timelapse 5000        #Timelapse Photography(ms)
```

## Utilizing the scripts
```
from capture_image import capture_image
from upload_to_dropbox import upload_image_to_dropbox
# Capture the image and get the raw image data
raw_image_data = capture_image(timeout=1000, resolution=(640, 480), preview=False, hflip=True)
# Upload the raw image data to Dropbox as a JPEG file
upload_image_to_dropbox(raw_image_data, is_numpy=False)
```

```
from capture_numpy_image import capture_numpy_image
from upload_to_dropbox import upload_image_to_dropbox
# Capture the image and get it as a NumPy array
numpy_image = capture_numpy_image(timeout=1000, resolution=(640, 480), preview=False, hflip=True)
# Upload the NumPy array data to Dropbox as a text file
upload_image_to_dropbox(numpy_image, is_numpy=True)
```
