
# #載入套件
import urllib.request as req
import json
# #從檔案中讀取json資料，並且放入data變數中

# # # 開啟網址
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json"

# # #讀取資料(最佳實務)
urlopen=req.urlopen(src)
with urlopen as response:
    data=json.load(response)



# # 取得特定欄位資料:"stitle"、"longitude"、"latitude"、"file"

info_list=data["result"]["results"]

#最佳實務:寫出資料
with open("data.txt","w",encoding="utf-8") as file:
    for info in info_list: 
        stitle=info["stitle"]
        lon=info["longitude"]
        lat=info["latitude"]
        pic_url="http"+info["file"].split("http")[1]
        #write的分隔符號是+
        file.write(stitle+","+lon+","+lat+","+pic_url+"\n")
