import math

r=6371*1000 #Earth radius [m]
DOinit:float
class Avion():
    
    heading:float #[degree]
    horizontalSpeed:float #[kt]
    verticalSpeed:float #[ft/min]
    latitude:float #[degree] or Phi
    longitude:float #[degree] or Theta
    altitude:float #[ft]
    global r
    
    def __init__(self, heading:float,horizontalSpeed:float,verticalSpeed:float, latitude:float,longitude:float,altitude:float):
        self.heading = heading
        self.horizontalSpeed = horizontalSpeed
        self.verticalSpeed = verticalSpeed
        self.latitude=latitude
        self.longitude=longitude
        self.altitude=altitude
        rho= r+altitude #Earth radius [m] + Altitude


    def deplacement(heading, horizontalSpeed, verticalSpeed, latitude, longitude, altitude):
        i=0 #test time in second
        global r
        rho=(r+altitude*Conversion.FT2M)
        #We make the hypothesis of a local flat Earth
        Vx=horizontalSpeed*math.cos(heading) #Projection of speed on x axis
        Vy=horizontalSpeed*math.sin(heading) #Projection of speed on y axis
        Vz=verticalSpeed*Conversion.FT2M #Projection of speed on z axis

        Vx*=Conversion.KT2MS
        Vy*=Conversion.KT2MS

        #Projection of spherical position to a cartesian referential

        x=rho*math.sin(90-latitude)*math.cos(longitude)
        y=rho*math.sin(90-latitude)*math.sin(longitude)
        z=rho*math.cos(90-latitude)

        #Position evolution for t=10s
        while i<10:
            x+=Vx*1
            y+=Vy*1
            z+=Vz*1
            i+=1

        #New final position on spherical reference
        rho= math.sqrt(x^2+y^2+z^2)
        theta=math.acos(z/rho)
        latitude=90-theta
        longitude=math.atan2(y,x)

class Conversion():
    ## UNITY CONVERSION TO INTERNATIONAL SYSTEM ##
    DEG2RAD= math.pi/180 #Conversion degree to rad
    KT2MS= 1852/3600 #Conversion kt to m/s
    FT2M:float=0,3048 #Conversion ft to meters
    FTMIN2MS=0,3048*1/60 #Conversion ft/min to m/s

def distanceOblique():
    global r
    phiA:float #latitude Avion 1
    phiB:float #latitude Avion 2
    thetaA:float #longitude Avion 1
    thetaB:float #longitude Avion 2

    phiA = chasseur.latitude
    phiB = bandit.latitude
    thetaA = chasseur.longitude
    thetaB = chasseur.longitude

    DOinit=r*math.acos(math.cos(thetaA)*math.cos(thetaB)+math.sin(thetaA)*math.sin(thetaB)*math.cos(phiB-phiA)) #Oblical distance formula from the ground projected points
    print(DOinit)
    return DOinit

    
def comparaison():

    global DOinit
    phiAfin = chasseur.latitude
    phiBfin = bandit.latitude
    thetaAfin = chasseur.longitude
    thetaBfin = chasseur.longitude

    DOfin=r*math.acos(math.cos(thetaAfin)*math.cos(thetaBfin)+math.sin(thetaAfin)*math.sin(thetaBfin)*math.cos(phiBfin-phiAfin))
    print (DOfin)

    if DOinit<DOfin:
        print("Divergence")
    elif DOinit>DOfin:
        print("Convergence")
    elif DOinit==DOfin:
        print("Ni convergence ni divergence")

chasseur = Avion(0,100,0,45,0,5000)
bandit = Avion(90,100,0,45,0,5000)

distanceOblique()
chasseur.deplacement
bandit.deplacement
comparaison()