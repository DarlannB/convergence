import math
import avion
from avion import Avion

r=6371*1000 #Earth radius [m]
def distanceOblique():
    global r
    phiA:float #latitude Avion 1
    phiB:float #latitude Avion 2
    thetaA:float #longitude Avion 1
    thetaB:float #longitude Avion 2

    phiA = pt1.latitude #latitude Avion 1
    phiB = pt2.latitude #latitude Avion 2
    thetaA = pt1.longitude #longitude Avion 1
    thetaB = pt2.longitude #longitude Avion 2

    DO=r*math.acos(math.cos(thetaA)*math.cos(thetaB)+math.sin(thetaA)*math.sin(thetaB)*math.cos(phiB-phiA)) #Oblical distance formula from the ground projected point
    return DO
    
def comparaison():

    DOinit=distanceOblique()
    print("Distance Oblique initiale : {}\n".format("%.2f"%DOinit))
    pt1.deplacement()
    #print(chasseur.latitude,chasseur.longitude, chasseur.altitude)
    pt2.deplacement()
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
pt1=chasseur
pt2=bandit

#############################################CREATION FENETRE GRAPHIQUE ####################################################################
import configgraph

if __name__ == "__main__" :
    app=configgraph.Application()
    app.title("VISUALISATION CONVERGENCE VECTEUR")
    app.mainloop()