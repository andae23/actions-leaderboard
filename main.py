import urlfetch
import re
import csv

# cl = [
#     '458029', #darknoob
#     '178430', #bloodless
#     '357795', #dracken
#     '208269', #jonslow
#     '212294', #derp
#     '541127', #rmcoo
#     '6440047', #blackheart
#     '1052193', #buddy
# ]

clid = []
# with open("clid.csv") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         clid.append({"id": row[0], "elo": row[1], "name": row[2]})

# trcl = [
#     '2041940', #arzach
#     '1061425', #mundo
#     '625034', #maniac
#     '291652', #jorge
#     '209596', #trennig
#     '1464442', #miked
#     '358880', #wenegor
#     '237368', #andae23
#     '583689', #gyeseongyeon
#     '4020942', #pupil
#     '639620', #bazi
#     '3512025', #pompom
#     '1434761', #mrister
#     '2304457', #marintho
#     '1361744', #x0r6zt
#     '5273455', #redraven
#     '385019', #artofthetroll
#     '448146', #strek
#     '269459', #bogsauce
# ]

trclid = []
with open("trclid.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        trclid.append({"id": row[0], "elo": row[1], "name": row[2]})


def main(clid, trclid):
#     i = 0
#     while i < len(clid):
#         id = clid[i]
#         response = urlfetch.get("https://legacy.aoe2companion.com/api/nightbot/rank?&profile_id=" + id["id"])
#         r = str(response.content)
#         if matches := re.search(r"^.*CL\.(.*)\s\((\d*)\)\s.*$",r):
#             clid[i]["elo"] = int(matches.group(2).strip())
#             clid[i]["name"] = matches.group(1).strip()
#         else:
#             clid[i]["elo"] = int(clid[i]["elo"])
#         i += 1
#     cl_sort = sorted(clid, key=lambda x: x["elo"], reverse=True)
#     
#     with open("clboard.txt","w") as file:
#         for clown in cl_sort:
#             string = clown["name"] + ": " + str(clown["elo"]) + " // "
#             file.write(string)
#     
#     with open("clid.csv","w") as file:
#         for clown in cl_sort:
#             string = clown["id"] + "," + str(clown["elo"]) + "," + clown["name"] + "\n"
#             file.write(string)


    i = 0
    while i < len(trclid):
        id = trclid[i]
        response = urlfetch.get("https://legacy.aoe2companion.com/api/nightbot/rank?&profile_id=" + id["id"])
        r = str(response.content)
        if matches := re.search(r"^.*CL\.(.*)\s\((\d*)\)\s.*$",r):
            trclid[i]["elo"] = int(matches.group(2).strip())
            trclid[i]["name"] = matches.group(1).strip()
        else:
            trclid[i]["elo"] = int(trclid[i]["elo"])
        i += 1
    trcl_sort = sorted(trclid, key=lambda x: x["elo"], reverse=True)
    
    with open("trclboard.txt","w") as file:
        for clown in trcl_sort:
            string = clown["name"] + ": " + str(clown["elo"]) + " // "
            file.write(string)
    
    with open("trclid.csv","w") as file:
        for clown in trcl_sort:
            string = clown["id"] + "," + str(clown["elo"]) + "," + clown["name"] + "\n"
            file.write(string)

if __name__ == "__main__":
    main(clid, trclid)
