import math
import avion
from avion import Avion

def distanceOblique():
    global r
    phiA:float #latitude Avion 1
    phiB:float #latitude Avion 2
    thetaA:float #longitude Avion 1
    thetaB:float #longitude Avion 2

    phiA = chasseur.latitude #latitude Avion 1
    phiB = bandit.latitude #latitude Avion 2
    thetaA = chasseur.longitude #longitude Avion 1
    thetaB = chasseur.longitude #longitude Avion 2

    DO=r*math.acos(math.cos(thetaA)*math.cos(thetaB)+math.sin(thetaA)*math.sin(thetaB)*math.cos(phiB-phiA)) #Oblical distance formula from the ground projected point
    return DO
    
def comparaison():

    DOinit=distanceOblique()
    print("Distance Oblique initiale : {}\n".format("%.2f"%DOinit))
    chasseur.deplacement()
    #print(chasseur.latitude,chasseur.longitude, chasseur.altitude)
    bandit.deplacement()
    #print(bandit.latitude,bandit.longitude, bandit.altitude)
    DOfin=distanceOblique()
    print("Distance Oblique finale : {}\n".format("%.2f"%DOfin))

    if DOinit<DOfin:
        print("Divergence")
    elif DOinit>DOfin:
        print("Convergence")
    elif DOinit==DOfin:
        print("Ni convergence ni divergence")

##DEBUT PROGRAMME##

chasseur = Avion(270,100,0,46,5,5000)
bandit = Avion(90,100,0,45,5,5000)
comparaison()