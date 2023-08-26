#!/usr/bin/env python3
import requests
import subprocess
from datetime import datetime, timedelta, timezone


repo_url = "https://api.github.com/repos/patilajayv/CICDpractise"
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
    
    
    subprocess.run(["bash", "cicdtest.sh"])
    
else:
    print("No recent commits in the dev branch.")


# ---------------------latest change-------------------------------------------------------



# import requests
# import subprocess
# from datetime import datetime, timedelta, timezone

# repo_url = "https://api.github.com/repos/Akhilbmsb/CICDpractise"
# branch = "dev"

# # Get the current time in UTC
# current_utc_time = datetime.utcnow()

# # Calculate IST time difference
# ist_time_difference = timedelta(hours=5, minutes=30)
# ist_time = current_utc_time + ist_time_difference

# # Convert IST time to ISO 8601 format
# timestamp_ist = ist_time.isoformat()

# # Calculate the timestamp one minute before the current IST time
# timestamp = (ist_time - timedelta(minutes=20)).isoformat()
# print(timestamp,"timestamp")

# # Construct the API URL
# api_url = f"{repo_url}/commits?sha={branch}"

# # Send API request to retrieve commits
# response = requests.get(api_url)
# commits = response.json()

# # Check if there are commits and find the latest commit timestamp
# latest_commit_timestamp = None
# if commits:
#     latest_commit_timestamp = commits[0]['commit']['committer']['date']
#     print(latest_commit_timestamp,"latestcommittimestamp")

# # Compare the latest commit timestamp with the calculated timestamp
# if latest_commit_timestamp and latest_commit_timestamp > timestamp:
#     print("There are recent commits. Running the bash script...")
#     subprocess.run(["bash", "cicdtest.sh"])
# else:
#     print("No recent commits in the dev branch.")


