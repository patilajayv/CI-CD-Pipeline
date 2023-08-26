#!/usr/bin/env python3
import requests
import subprocess
from datetime import datetime, timedelta, timezone


repo_url = "https://api.github.com/patilajayv/CI-CD-Pipeline.git"
branch = "main"


current_utc_time = datetime.utcnow()
ist_time_difference = timedelta(hours=5, minutes=30)
ist_time = current_utc_time + ist_time_difference
timestamp_ist = ist_time.isoformat()
print(timestamp_ist,"timestamp_ist")
# timestamp = (ist_time - timedelta(minutes=1)).isoformat()
timestamp = (datetime.utcnow() - timedelta(hours=2)).isoformat()
original_datetime = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%f")
converted_timestamp = original_datetime.strftime("%Y-%m-%dT%H:%M:%SZ")
print(timestamp,"timestamp")
print(converted_timestamp,"converted_timestamp")

api_url = f"{repo_url}/commits?sha={branch}&since={converted_timestamp}"
print(api_url,"apiurl")


response = requests.get(api_url)

commits = response.json()


if commits:
    print("There are recent commits. Running the bash script...")


    subprocess.run(["sudo","bash", "cicdtest.sh"])

else:
    print("No recent commits in the dev branch.")
