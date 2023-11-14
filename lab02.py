import json
from urllib.request import urlopen

obj = json.load(
    urlopen(
        "http://air4thai.pcd.go.th/webV2/history/api/data.php?stationID=70t&param=PM25,PM10,O3,CO,NO2,SO2,WS,WD,TEMP,RH,BP,RAIN&type=hr&sdate=2023-10-01&edate=2023-11-06&stime=00&etime=16"
    )
)
length = len(obj["stations"][0]["data"])

stringList = []

while True:
    text = input(
        str(
            "Type [PM25, PM10, O3, CO, NO2, SO2, WS, WD, TEMP, RH, BP, RAIN] for Show or Type [EXIT] for End : "
        )
    )
    txt = text.upper()

    if txt == "EXIT":
        break

    stringList.append(txt)

    for i in stringList:
        print("Station ID: " + obj["stations"][0]["stationID"])
        print(i, end=" ")
    print("\n")

    for x in range(length):
        for value in obj["stations"][0]["data"][x]:
            print(value[stringList])
