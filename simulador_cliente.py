import requests
import sys
import random
import json
import time
from random import randint

if len(sys.argv) < 2:
	print("Debe pasasr el id del conductor")
	sys.exit(1)

route1 = [("6.2614871","-75.5562689"),("6.26149" ,"-75.55627"),("6.26724", "-75.57452"),("6.29982" ,"-75.56515"),("6.31564" ,"-75.55702"),( "6.3378" ,"-75.55892"),("6.337683", "-75.5589119")]
route2 = [("6.3365954", "-75.5588036"),("6.3366" ,"-75.5588"),("6.33476", "-75.55604"),("6.33162", "-75.55786"),("6.32711", "-75.55789"),("6.32144", "-75.55743"),("6.31758", "-75.55711"),("6.31402", "-75.55724"),("6.30926", "-75.55997"),("6.30486", "-75.56047"),("6.30289", "-75.56283"),("6.30014", "-75.56496"),("6.29226", "-75.56838"),("6.27897", "-75.57213"),("6.27195", "-75.57359"),("6.26609", "-75.5751"),("6.2653", "-75.57414"),("6.265", "-75.57124"),("6.26444", "-75.56754"),("6.26372", "-75.56247"),("6.26294", "-75.55748"),("6.2614871", "-75.5562689")]
route3 = [("6.2068965" ,"-75.5593963"),("6.2069", "-75.5594"),("6.20605", "-75.56065"),("6.20576", "-75.56253"),("6.20702", "-75.56384"),("6.20871", "-75.56414"),("6.21079" ,"-75.5871"),("6.21143", "-75.57057"),("6.21283" ,"-75.57332"),("6.21322" ,"-75.576"),("6.21398", "-75.57897"),("6.21424", "-75.57842"),("6.20911", "-75.57908"),("6.20803", "-75.57911"),("6.19474","-75.58206"),("6.1848" ,"-75.58834"),("6.17738" ,"-75.59382"),("6.17648" ,"-75.5965"),("6.17779" ,"-75.59966"),("6.17906" ,"-75.6022"),("6.17817" ,"-75.60369"),("6.17673" ,"-75.6056"),("6.17713" ,"-75.60733"),("6.17939" ,"-75.60961"),("6.1814" ,"-75.60901"),("6.1812474" ,"-75.6075625")]
route4 = [("6.250359", "-75.5759128"),("6.25036", "-75.57591"),("6.25289" ,"-75.57738"),("6.25764", "-75.57473"),("6.2652" ,"-75.57171"),("6.2745", "-75.56946"),("6.27227" ,"-75.56531"),("6.27254", "-75.56257"),("6.2712966" ,"-75.5583969")]
route5 = [("6.2670326", "-75.5680132"),("6.26703" ,"-75.56801"),("6.26488" ,"-75.56747"),("6.26517" ,"-75.57159"),("6.26593" ,"-75.57325"),("6.26528" ,"-75.57271"),("6.26046" ,"-75.57447"),("6.2528" ,"-75.57859"),("6.25035" ,"-75.58081"),("6.24833" ,"-75.58085"),("6.24492" ,"-75.57962"),("6.23927" ,"-75.57787"),("6.23942" ,"-75.57825"),("6.2396" ,"-75.57634"),("6.23893" ,"-75.57549"),("6.23782" ,"-75.57409"),("6.2363259" ,"-75.5735631")]
routes = {0:route1,1:route2,2:route3,3:route4,4:route5}
selected = randint(0,4)
length = len(routes[selected])
cont = 0

with open('DatosECGPersonas/ECGPersona6NoAfan.json') as f:
    data = json.load(f)

print(len(data['ecg']))

for i in data['ecg']:
    print(i)
    r = requests.post("http://pi2biofeedback.dis.eafit.edu.co//signal/save", data={"ecg": i, "conductor": sys.argv[1], "lat":routes[selected][cont][0],"log":routes[selected][cont][1]})
    print(r.status_code, r.reason)
    print(r.text)
    cont = cont+1 if cont < length-1 else 0
    time.sleep(0.02)

'''while True:
    val = random.uniform(35.5,82.2)
    r = requests.post("http://localhost:3000/signal/save", data={"ecg": val, "tiempo": 11, "conductor": "5b0dd4b2761968111fb446cd"})
    print(r.status_code, r.reason)
    print(r.text)
    time.sleep(0.02)'''
