import math

class Conversion():
    ## UNITY CONVERSION TO INTERNATIONAL SYSTEM ##
    DEG2RAD= math.pi/180 #Conversion degree to rad
    KT2MS= 1852/3600 #Conversion kt to m/s
    FT2M=0.3048 #Conversion ft to meters
    FTMIN2MS=0.3048*1/60 #Conversion ft/min to m/s

    RAD2DEG=180/math.pi
    MS2KT=3600/1852
    M2FT=1/0.3048