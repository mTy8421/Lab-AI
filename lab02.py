import json
from urllib.request import urlopen

obj = json.load(
    urlopen(
        "http://air4thai.pcd.go.th/webV2/history/api/data.php?stationID=70t&param=PM25,PM10,O3,CO,NO2,SO2,WS,WD,TEMP,RH,BP,RAIN&type=hr&sdate=2023-10-01&edate=2023-11-06&stime=00&etime=16"
    )
)
length = len(obj["stations"][0]["data"])

while True:
    text = input(
        str(
            "Type [PM25, PM10, O3, CO, NO2, SO2, WS, WD, TEMP, RH, BP, RAIN] for Show or Type [EXIT] for End : "
        )
    )
    txt = text.upper()

    match txt:
        case "PM25":
            print("Station ID: " + obj["stations"][0]["stationID"])
            print("PM25")
        case "PM10":
            print("Station ID: " + obj["stations"][0]["stationID"])
            print("PM10")
        case "O3":
            print("Station ID: " + obj["stations"][0]["stationID"])
            print("O3")
        case "CO":
            print("Station ID: " + obj["stations"][0]["stationID"])
            print("CO")
        case "NO2":
            print("Station ID: " + obj["stations"][0]["stationID"])
            print("NO2")
        case "SO2":
            print("Station ID: " + obj["stations"][0]["stationID"])
            print("SO2")
        case "WS":
            print("Station ID: " + obj["stations"][0]["stationID"])
            print("WS")
        case "WD":
            print("Station ID: " + obj["stations"][0]["stationID"])
            print("WD")
        case "TEMP":
            print("Station ID: " + obj["stations"][0]["stationID"])
            print("TEMP")
        case "RH":
            print("Station ID: " + obj["stations"][0]["stationID"])
            print("RH")
        case "BP":
            print("Station ID: " + obj["stations"][0]["stationID"])
            print("BP")
        case "RAIN":
            print("Station ID: " + obj["stations"][0]["stationID"])
            print("RAIN")
        case "EXIT":
            break
        case _:
            for k, v in obj["stations"][0]["data"][0].items():
                print(k, end=" ")

            print("\n")

            for x in range(length):
                for k, v in obj["stations"][0]["data"][x].items():
                    print(v, end=" ")
                print("\n")
