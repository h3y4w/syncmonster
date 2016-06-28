import requests
import json
def getFiles():
    url = 'http://127.0.0.1:5000/GetAllFiles?user_id=1'
    r = requests.get(url)
    j=r.json()
    return j

def deleteFile(file_id):
    user_id = '1'
    url = 'http://127.0.0.1:5000/DeleteFile?user_id=%s&file_id=%s' % (user_id, file_id)
    requests.delete(url)

