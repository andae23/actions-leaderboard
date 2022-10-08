import urlfetch
import re

cl = [
    '458029', #darknoob
    '178430', #bloodless
    '357795', #dracken
    '208269', #jonslow
    '212294', #derp
    '541127', #rmcoo
    '6440047', #blackheart
    '1052193', #buddy
]

trcl = [
    '271258', #diante
    '2041940', #arzach
    '1061425', #mundo
    '625034', #maniac
    '291652', #jorge
    '209596', #trennig
    '1464442', #miked
    '358880', #wenegor
    '237368', #andae23
    '583689', #gyeseongyeon
    '4020942', #pupil
    '639620', #bazi
    '3512025', #pompom
    '1434761', #mrister
    '2304457', #marintho
    '1361744', #x0r6zt
    '5273455', #redraven
    '385019', #artofthetroll
    '448146', #strek
]

def main(cl, trcl):
    cl_list = {}
    for id in cl:
        response = urlfetch.get("https://legacy.aoe2companion.com/api/nightbot/rank?&profile_id=" + id)
        r = str(response.content)
        if matches := re.search(r"^.*CL\.(.*)\s\((\d*)\)\s.*$",r):
            name = matches.group(1).strip()
            rating = int(matches.group(2).strip())
            cl_list[name] = rating
    cl_sort = sorted(cl_list.items(), key=lambda x: x[1], reverse=True)
    
    trcl_list = {}
    for id in trcl:
        response = urlfetch.get("https://legacy.aoe2companion.com/api/nightbot/rank?&profile_id=" + id)
        r = str(response.content)
        if matches := re.search(r"^.*CL\.(.*)\s\((\d*)\)\s.*$",r):
            name = matches.group(1).strip()
            rating = int(matches.group(2).strip())
            trcl_list[name] = rating
    trcl_sort = sorted(trcl_list.items(), key=lambda x: x[1], reverse=True)
    
    with open("clboard.txt","w") as file:
        for clown in cl_sort:
            file.write(f"{clown[0]}: {clown[1]} // ")
        
    with open("trclboard.txt","w") as file:
        for clown in trcl_sort:
            file.write(f"{clown[0]}: {clown[1]} // ")


if __name__ == "__main__":
    main(cl, trcl)