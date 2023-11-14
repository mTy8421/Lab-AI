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
            "Type [DATETIMEDATA, PM25, PM10, O3, CO, NO2, SO2, WS, WD, TEMP, RH, BP, RAIN] for Show or Type [DEL] for delet list And Type [EXIT] for End : "
        )
    )
    txt = text.upper()

    if txt == "EXIT":
        break
    elif txt == "DEL":
        for v in stringList:
            stringList.remove(v)
            print("del=" + v)
        continue
    stringList.append(txt)

    print("Station ID: " + obj["stations"][0]["stationID"])
    for i in stringList:
        print(i, end=" ")
    print("\n")

    for x in range(3):
        for values in stringList:
            print(obj["stations"][0]["data"][x][values], end=" ")
        print("\n")
