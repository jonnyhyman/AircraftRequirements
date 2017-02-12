import numpy as np
import AeroData as aero
#---------------- Helper Funcitons
def MetersToRhos(meters):
    a =       1.228 # Exponential fit done in MATLAB
    b =  -0.0001168
    rho = a*np.exp(b*meters)
    return rho

def double(data):
    return '{0:.2f}'.format(data)

#---------------- Aircraft Values
Acft={}
Acft['Altitude']= 3000 # Meters 3000m ~= 10,000ft
Acft['Airspeed']= 67 # Meters per Second
Acft['EmptyKG'] = 213 # kg
Acft['Seats']   = 2
Acft['Baggage'] = 80 # kg
Acft['Payload'] = 80*Acft['Seats'] # kg 80 is the weight of the average human
Acft['WingArea']= 8*Acft['Seats']   # m^2 wing area per seat typical of g-a
Acft['PerfMrgn']= 0.5 # The fraction of lift still available in cruise

Prop={}
Prop['WhPerKg']       = 265     # Wh/kg
Prop['Effectiveness'] = 15/1000 # N/Watt
Prop['PowerPerMass']  = 1000/1 - 250 # W/kg of propulsion system,
                                     # by typical motor data, minus some margin
AOA={}
AOA['Climb']  =(10) # deg
AOA['Cruise'] =(5)  # deg
AOA['Descent']=(-5) # deg

#---------------- Calculate

a=AOA['Cruise']
v=Acft['Airspeed'] # m/s
S=Acft['WingArea'] # m^2
rho=MetersToRhos(Acft['Altitude']) # kg/m^3

print(' ')
cL = aero.CL(a)
cD = aero.CD(a)
print('Lift Coeff =',cL,'')
print('Drag Coeff =',cD,'')

Lf = (1/2)*(rho)*(v**2)*(S)*(cL);
Df = (1/2)*(rho)*(v**2)*(S)*(cD);
# Drag force, also the force for which propulsion must counteract
print('Lift Force =',Lf,'N')
print('Drag Force =',Df,'N')

P_Cruise = Df/Prop['Effectiveness'] # Newtons/(Newtons/Watt) = Watts
KW_Cruise= P_Cruise/1000
Prop['PropKG'] = P_Cruise/Prop['PowerPerMass'] # Watts / (Watts/kg) = kg

print('Cruise Power =',KW_Cruise,'kW')

BatMass = ( (Lf/9.80665) # N -> kgf
                -Acft['Baggage']
                -Acft['Payload']
                -Acft['EmptyKG']
                -Prop['PropKG']
          )*(Acft['PerfMrgn'])

print(' ')

Wh = Prop['WhPerKg']*BatMass
kWh= Wh/1000

Endurance=kWh/KW_Cruise # kW * h / kW = hrs
Range=(Acft['Airspeed']*60*60)*Endurance # meters
Range=Range/1000# kilometers
Range=Range/1.852# nautical miles

print('Battery Mass     =',BatMass,'kg')
print('Battery Capacity =',double(kWh),'kWh')
print('Battery Endurance=',double(Endurance),'hrs')
print(' ')

AircraftKG=BatMass+Acft['Baggage']+Acft['Payload']+Acft['EmptyKG']+Prop['PropKG']
TWR       =(P_Cruise*Prop['Effectiveness'])/(AircraftKG*9.80665) # N/N
LWR       =Lf/(AircraftKG*9.80665)

print('Aircraft Range   =',double(Range),'nautical miles')
print('Aircraft Gross   =',double(AircraftKG),'kg','=',double(AircraftKG*2.2),'lbs')
print('Aircraft Prop    =',Prop['PropKG'],'kg')
print('Aircraft TWR     =',TWR,'')
print('Aircraft LWR     =',LWR,'')
