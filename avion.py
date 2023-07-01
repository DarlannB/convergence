import math
import conversion
from conversion import Conversion

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
        rho=(r+(self.altitude*Conversion.FT2M))
        Vz:float
        print("POSITION INITIALE SPHERIQUE -> Z:{}, LAT:{}, LONG:{}".format("%.2f"%self.altitude,"%.2f"%self.latitude,"%.2f"%self.longitude))
        #We make the hypothesis of a local flat Earth
        Vx=(self.horizontalSpeed*Conversion.KT2MS)*math.cos(self.heading*Conversion.DEG2RAD) #Projection of speed on x axis
        print("Vx == {}".format(Vx))
        Vy=(self.horizontalSpeed*Conversion.KT2MS)*math.sin(self.heading*Conversion.DEG2RAD) #Projection of speed on y axis
        print("Vy == {}".format(Vy))
        Vz=self.verticalSpeed*Conversion.FT2M #Projection of speed on z axis

        #Projection of spherical position to a cartesian referential
        x=rho*(math.sin((math.pi/2)-self.latitude*Conversion.DEG2RAD))*(math.cos(self.longitude*Conversion.DEG2RAD))
        y=rho*math.sin((math.pi/2)-self.latitude*Conversion.DEG2RAD)*math.sin(self.longitude)*Conversion.DEG2RAD
        z=rho*math.cos(self.latitude*Conversion.DEG2RAD)
        print("X={}, Y={}, Z={}".format(x,y,z))
        ##print("POSITION INITIALE CARTESIEN -> X:{}; Y:{}; Z:{}".format(x,y,z))

        #Position evolution by the time :t 
        t=1
        x+=Vx*t
        y+=Vy*t
        self.altitude+=Vz*t
        ##print("DEPLACEMENT CARTESIEN -> X:{}; Y:{}; Z:{}".format(x,y,z))

        #New final position on spherical reference
        rho= math.sqrt((x**2)+(y**2)+(z**2))
        theta=math.acos(z/rho)
        self.latitude=((math.pi/2)-theta)*Conversion.RAD2DEG
        self.longitude=(math.atan2(y,x))*Conversion.RAD2DEG

        print("NOUVELLE POSITION SPHERIQUE -> Z:{}, LAT:{}, LONG:{}\n".format("%.2f"%self.altitude,"%.2f"%self.latitude,"%.2f"%self.longitude))

        return self.altitude, self.latitude, self.longitude