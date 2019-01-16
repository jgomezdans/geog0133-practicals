#!/usr/bin/env python

from pathlib import Path
import os
import zipfile
import time
import requests

def grab_data(url="https://www.dropbox.com/sh/6wt85sf0ubc9e8n/AACberbeIDG39yzjppNzhHMha?dl=1"):

    print(f"{time.asctime():s} -> Please wait while I get hold of the data")
    if not os.path.exists("./data/"):
        os.mkdir("./data")
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open("./temporal.zip", 'wb') as f:
            for chunk in r:
                f.write(chunk)
    print(f"{time.asctime():s} Downloaded")
    zipper = zipfile.ZipFile("temporal.zip")
    zipper.extractall("./data/")
    print(f"{time.asctime():s} -> Successfully downloaded data!")

if __name__ == "__main__":    
    grab_data()
