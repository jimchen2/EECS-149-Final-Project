import subprocess
import os
import time
import tempfile
import numpy as np

def upload_image_to_dropbox(image_data, is_numpy=True, folder_path='/'):
    """
    Uploads an image to Dropbox using dbxcli. If is_numpy is True, the image_data is assumed to be a numpy array,
    and it will be converted to a text representation.
    """
    # Create a named pipe (FIFO)
    fifo_path = tempfile.mktemp()
    os.mkfifo(fifo_path)

    timestamp = time.strftime("%Y%m%d-%H%M%S")
    dropbox_path = f"{folder_path}image_{timestamp}.txt" if is_numpy else f"{folder_path}image_{timestamp}.jpg"

    # Start a subprocess that waits for data on the fifo and uploads it to Dropbox
    upload_process = subprocess.Popen(['dbxcli', 'put', fifo_path, dropbox_path])

    # Write image data to the fifo
    with open(fifo_path, 'w' if is_numpy else 'wb') as fifo:
        if is_numpy:
            np.savetxt(fifo, image_data.reshape(-1, image_data.shape[-1]), fmt='%d')
        else:
            fifo.write(image_data)

    # Wait for the upload process to finish
    upload_process.wait()

    # Clean up: remove the fifo
    os.remove(fifo_path)

    print(f"Uploaded image to Dropbox: {dropbox_path}")

# Example usage
# upload_image_to_dropbox(image_data, is_numpy=True)
# or
# upload_image_to_dropbox(raw_image_data, is_numpy=False)

