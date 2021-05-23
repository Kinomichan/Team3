# Library to access and use Kintone apps
# May 14, 2021 v0.03
# Jun Suzuki (https://github.com/jxsboston)
# IoT for Kids: https://jxsboston.github.io/IoT-Kids/

import requests, json, datetime
from typing import Optional, Dict, Any

# Function to upload a file to a Kintone app
#   subDomain (string): Name of a subdomain where the Kitone app runs
#   apiToken (string):  API token to access the Kintone app
#   filePath (string):  Relative path to a file to be uploaded 
#
#   Returns the uploaded file's key in string or None (if the upload failed)
#
#   This function accepts keyword arguments only. 
#
def uploadFile(*, subDomain: str, apiToken: str, filePath: str) -> Optional[str]:
    url = "https://" + subDomain + ".kintone.com/k/v1/file.json"
    headers = {"X-Cybozu-API-Token": apiToken}
    with open(filePath, "rb") as f:
        file = {"file": (filePath, f, "multipart/form-data")}
        response = requests.post(url, headers=headers, files=file)

    if response.status_code == 200 and "fileKey" in json.loads(response.text):
        print("File uploaded. ", end="")
        fileKey = json.loads(response.text)["fileKey"]
        print("File key: " + fileKey)
        return fileKey
    else:
        print("File upload failed. Status code: " + str(response.status_code))
        print(response.text)
        return None

# Function to upload a new record to a Kintone app
#   subDomain (string): Name of a subdomain where the Kitone app runs
#   apiToken (string):  API token to access the Kintone app
#   record (dict):      Dictionary form of JSON record to be uploaded
#
#   Returns the uploaded record's ID in string or None (if the upload failed)
#
#   This function accepts keyword arguments only. 
#
def uploadRecord(*, subDomain: str, apiToken: str, record: Dict[str, Any]) -> Optional[str]:
    url = "https://" + subDomain + ".kintone.com/k/v1/record.json"
    headers = {"X-Cybozu-API-Token": apiToken,
               "Content-Type": "application/json"}
    
    response = requests.post(url, headers=headers, json=record)
    if response.status_code == 200 and "id" in json.loads(response.text):
        print("Record uploaded.", end=" ")
        recordId = json.loads(response.text)["id"]
        print("Record ID: " + recordId)
        return recordId
    else:
        print("Record upload failed. Status code: " + str(response.status_code))
        return None

# Function to replace (overwrite) an existing record in a Kintone app with new record data
#   subDomain (string): Name of a subdomain where the Kitone app runs
#   apiToken (string):  API token to access the Kintone app
#   record (dict):      Dictionary form of JSON record to replace an existing record
#
#   Returns the updated record's revision number in string or None (if the update failed)
#
#   This function accepts keyword arguments only. 
#
def replaceRecord(*, subDomain: str, apiToken: str, record: Dict[str, Any]) -> Optional[str]:
    url = "https://" + subDomain + ".kintone.com/k/v1/record.json"
    headers = {"X-Cybozu-API-Token": apiToken,
               "Content-Type": "application/json"}
    
    response = requests.put(url, headers=headers, json=record)
    if response.status_code == 200 and "revision" in json.loads(response.text):
        print("Record replaced.", end=" ")
        print("Record ID: " + record["id"], end=" ")
        revisionNum = json.loads(response.text)["revision"]
        print("Record revision number: " + revisionNum)
        return revisionNum
    else:
        print("Record replacement failed. Status code: " + str(response.status_code))
        return None

# Function to return the current date and time in string based on
#   the YR-MO-DAY-HR-MIN-SEC format.
#
def getCurrentTimeStamp() -> str:
    dt = datetime.datetime.now()
    return "{:d}-{:02d}-{:02d}-{:02d}-{:02d}-{:02d}".format(
        dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)

