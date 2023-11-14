import json
from urllib.request import urlopen

obj = json.load(
    urlopen(
        "http://air4thai.pcd.go.th/webV2/history/api/data.php?stationID=70t&param=PM25,PM10,O3,CO,NO2,SO2,WS,WD,TEMP,RH,BP,RAIN&type=hr&sdate=2023-10-01&edate=2023-11-06&stime=00&etime=16"
    )
)
length = len(obj["stations"][0]["data"])

print("Station ID: " + obj["stations"][0]["stationID"])

for k, v in obj["stations"][0]["data"][0].items():
    print(k, end=" ")

print("\n")

for x in range(length):
    for k, v in obj["stations"][0]["data"][x].items():
        print(v, end=" ")
    print("\n")

# PM25,PM10,O3,CO,NO2,SO2,WS,WD,TEMP,RH,BP,RAIN

while True:
    text = input(str("Enter Someting: "))
    txt = text.upper()

    match txt:
        case "PM25":
            print("PM25")
        case "PM10":
            print("PM10")
        case "O3":
            print("O3")
        case "CO":
            print("CO")
