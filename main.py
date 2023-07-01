import math
import avion
from avion import Avion
import gui
from conversion import Conversion

r=6371*1000 #Earth radius [m]
conv="Need calculation"
def distanceOblique():
    global r
    phiA:float #latitude Avion 1
    phiB:float #latitude Avion 2
    thetaA:float #longitude Avion 1
    thetaB:float #longitude Avion 2

    phiA = pt1.latitude*Conversion.DEG2RAD #latitude Avion 1
    phiB = pt2.latitude*Conversion.DEG2RAD #latitude Avion 2
    thetaA = pt1.longitude*Conversion.DEG2RAD #longitude Avion 1
    thetaB = pt2.longitude*Conversion.DEG2RAD #longitude Avion 2

    DO=r*math.acos(math.cos(thetaA)*math.cos(thetaB)+math.sin(thetaA)*math.sin(thetaB)*math.cos(phiB-phiA))+math.sqrt(((pt1.altitude-pt2.altitude)*Conversion.FT2M)**2) #Oblical distance formula from the ground projected point
    return DO
    
def comparaison():
    global conv
    DOinit=distanceOblique()
    print("Distance Oblique initiale : {}m\n".format("%.2f"%DOinit))
    pt1.deplacement()
    #print(chasseur.latitude,chasseur.longitude, chasseur.altitude)
    pt2.deplacement()
    #print(bandit.latitude,bandit.longitude, bandit.altitude)
    DOfin=distanceOblique()
    print("Distance Oblique finale : {}m\n".format("%.2f"%DOfin))

    if DOinit<DOfin:
        conv="Divergence"
        print(conv)
    elif DOinit>DOfin:
        conv="Convergence"
        print(conv)
    elif DOinit==DOfin:
        conv="Ni convergence ni divergence"
        print(conv)
    return conv

##DEBUT PROGRAMME##

chasseur = Avion(90,100,0,45,0,5000)
bandit = Avion(0,100,0,45,0.01, 3000)
pt1=chasseur
pt2=bandit

#############################################CREATION FENETRE GRAPHIQUE ####################################################################

if __name__ == "__main__":
    gui.Run_graphic.gui_mainloop()