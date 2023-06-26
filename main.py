import math

r=6371*1000 #Earth radius [m]
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


    def deplacement(self):
        i=0 #test time in second
        global r
        rho=(r+self.altitude*Conversion.FT2M)
        Vz:float
        print("POSITION INITIALE SPHERIQUE -> Z:{}, LAT:{}, LONG:{}".format(self.altitude,self.latitude,self.longitude))
        #We make the hypothesis of a local flat Earth
        Vx=self.horizontalSpeed*math.cos(self.heading) #Projection of speed on x axis
        Vy=self.horizontalSpeed*math.sin(self.heading) #Projection of speed on y axis
        Vz=self.verticalSpeed*Conversion.FT2M #Projection of speed on z axis

        Vx=Vx*Conversion.KT2MS
        
        Vy=Vy*Conversion.KT2MS


        #Projection of spherical position to a cartesian referential

        x=rho*(math.sin(90-self.latitude))*(math.cos(self.longitude))
        y=rho*math.sin(90-self.latitude)*math.sin(self.longitude)
        z=rho*math.cos(90-self.latitude)
        print("POSITION INITIALE CARTESIEN -> X:{}; Y:{}; Z:{}".format(x,y,z))
        #Position evolution for t=10s
        while i<1:
            x+=Vx*1
            y+=Vy*1
            z+=Vz*1
            i+=1
        print("DEPLACEMENT CARTESIEN -> X:{}; Y:{}; Z:{}".format(x,y,z))
        #New final position on spherical reference
        rho= math.sqrt(x**2+y**2+z**2)
        theta=math.acos(z/rho)
        self.latitude=90-theta
        self.longitude=math.atan2(y,x)
        self.altitude=(rho-r)*(1/Conversion.FT2M)
        print("NOUVELLE POSITION SPHERIQUE -> Z:{}, LAT:{}, LONG:{}".format(self.altitude,self.latitude,self.longitude))
        return self.altitude, self.latitude, self.longitude

class Conversion():
    ## UNITY CONVERSION TO INTERNATIONAL SYSTEM ##
    DEG2RAD= math.pi/180 #Conversion degree to rad
    KT2MS= 1852/3600 #Conversion kt to m/s
    FT2M=0.3048 #Conversion ft to meters
    FTMIN2MS=0.3048*1/60 #Conversion ft/min to m/s

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

    DO=r*math.acos(math.cos(thetaA)*math.cos(thetaB)+math.sin(thetaA)*math.sin(thetaB)*math.cos(phiB-phiA)) #Oblical distance formula from the ground projected points
    print(DO)
    return DO
    
def comparaison():

    DOinit=distanceOblique()
    chasseur.deplacement()
    bandit.deplacement()
    DOfin=distanceOblique()

    if DOinit<DOfin:
        print("Divergence")
    elif DOinit>DOfin:
        print("Convergence")
    elif DOinit==DOfin:
        print("Ni convergence ni divergence")

chasseur = Avion(0,100,0,45,0,5000)
bandit = Avion(90,100,0,45,0,5000)
comparaison()