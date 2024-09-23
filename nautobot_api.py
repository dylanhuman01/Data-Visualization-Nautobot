import requests
from rich import as r_print

header_nautobot = {"Authorization": "Token 727286601d44e4ee66ba3e6244061dc060176107"}

url= "https://192.168.118.130/api/"

device_type = "dcim/device-types/"
status = "extras/statuses"
role = "extras/roles"
location = "dcim/locations/"
platform = "dcim/platforms/"
rack = "dcim/racks/"


response = request.get(url + device_type, headers=header_nautobot, verify=False)
for each_line in response.json()["results"]:
    r_print(each_line)

exit() 
