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
            print("Param" + obj["stations"][0]["params"][0])
            for i in obj["stations"][0]["data"]:
                print(i["PM25"])
        case "PM10":
            print("Station ID: " + obj["stations"][0]["stationID"])
            print("Param" + obj["stations"][0]["params"][1])
            for i in obj["stations"][0]["data"]:
                print(i["PM10"])
        case "O3":
            print("Station ID: " + obj["stations"][0]["stationID"])
            print("Param" + obj["stations"][0]["params"][2])
            for i in obj["stations"][0]["data"]:
                print(i["O3"])
        case "CO":
            print("Station ID: " + obj["stations"][0]["stationID"])
            print("Param" + obj["stations"][0]["params"][3])
            for i in obj["stations"][0]["data"]:
                print(i["CO"])
        case "NO2":
            print("Station ID: " + obj["stations"][0]["stationID"])
            print("Param" + obj["stations"][0]["params"][4])
            for i in obj["stations"][0]["data"]:
                print(i["NO2"])
        case "SO2":
            print("Station ID: " + obj["stations"][0]["stationID"])
            print("Param" + obj["stations"][0]["params"][5])
            for i in obj["stations"][0]["data"]:
                print(i["SO2"])
        case "WS":
            print("Station ID: " + obj["stations"][0]["stationID"])
            print("Param" + obj["stations"][0]["params"][6])
            for i in obj["stations"][0]["data"]:
                print(i["WS"])
        case "WD":
            print("Station ID: " + obj["stations"][0]["stationID"])
            print("Param" + obj["stations"][0]["params"][7])
            for i in obj["stations"][0]["data"]:
                print(i["WD"])
        case "TEMP":
            print("Station ID: " + obj["stations"][0]["stationID"])
            print("Param" + obj["stations"][0]["params"][8])
            for i in obj["stations"][0]["data"]:
                print(i["TEMP"])
        case "RH":
            print("Station ID: " + obj["stations"][0]["stationID"])
            print("Param" + obj["stations"][0]["params"][9])
            for i in obj["stations"][0]["data"]:
                print(i["RH"])
        case "BP":
            print("Station ID: " + obj["stations"][0]["stationID"])
            print("Param" + obj["stations"][0]["params"][10])
            for i in obj["stations"][0]["data"]:
                print(i["BP"])
        case "RAIN":
            print("Station ID: " + obj["stations"][0]["stationID"])
            print("Param" + obj["stations"][0]["params"][11])
            for i in obj["stations"][0]["data"]:
                print(i["RAIN"])
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
