import json


with open("ex5.json","r") as sample:
    ex5=json.load(sample)
    sample.close()

    for data in ex5:
        if data['name'] == "Old Fashioned" and data['type'] == "donut":
            batter=data['batters']['batter']
            batter.append({"id":"1003","type":"Coffee"})
            print(data)
    

with open("ex5.json","w") as sample:
    json.dump(ex5,sample)
    sample.close