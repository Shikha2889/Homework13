import sys
import json
import urllib.request


try:
    res = urllib.request.urlopen("https://neverssl.com/asdfhjkahsdjkfbs")
    data = json.load(res)
    print("TVMaze API seems to be working")
    res.close()
except Exception as e:
        print(str(e))


