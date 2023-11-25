import subprocess

def capture_image(timeout=0, resolution=(0, 0), preview=True, hflip=False, quality=93):
    """
    Captures an image using libcamera-still and returns the image data.
    """
    cmd = ['libcamera-still', '-o', '-']  # Capture to stdout

    if timeout > 0:
        cmd += ['-t', str(timeout)]

    if resolution != (0, 0):
        cmd += ['--width', str(resolution[0]), '--height', str(resolution[1])]

    if not preview:
        cmd += ['--nopreview']

    if hflip:
        cmd += ['--hflip']

    cmd += ['-q', str(quality)]

    process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    image_data, _ = process.communicate()

    return image_data

# Example usage
# image_data = capture_image(timeout=1000, resolution=(640, 480), preview=False, hflip=True)

