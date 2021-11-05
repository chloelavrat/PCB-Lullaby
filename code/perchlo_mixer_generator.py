## --------------------------------------------
## Title : Perchlo mixer gcode
## Author : C.Lavrat
## Date : 2021/01/23
## -----------------------------------------------------------------------
fileName      = "perchlo-Mixer-60sec-30C.gcode"
bedTemp       = 30  # 30°C for perchlo + copper / 0°C for perchlo + aluminium
timeMix       = 1   # duration of the mix, in minutes
numWait       = 2   # number of message at start ("Place Circuit NOW!")
speed         = 2000  # speed of the bed
## -----------------------------------------------------------------------
zPosition     = 200 # Z position to free space for the glass container
frontPosition = 125 # Y position of bed in front mode
backPosition  = 150 # Y position of bed in back mode
## -----------------------------------------------------------------------

# open file
file = open(fileName, 'w')
## -- Place plate
file.write("G28\n") # Move the X,Y,Z to absolute position
file.write("G90\n") # Absolute programming in relation to the program origin
file.write("G0 Z"+str(int(zPosition))+"\n") # Move Z axis to clear the bed
## -- Place plate
for i in range(numWait):
    file.write("M117 Place Circuit NOW! "+str(numWait-i)+"\nG4 P1000\n")
file.write("M117 Circuit Rocking G-Code\nG0 Z200\n")
## -- init zero
file.write("G28 X0 Y0\n") # move to X=0 Y=0
## -- stepper motors
file.write("M18\n") # M18: Disable all stepper motors to save energie
## -- heat bed
if bedTemp != 0:
    file.write("M117 Heating Bed To "+str(int(bedTemp))+"°C\n")
    file.write("M190 S"+str(int(bedTemp))+"\n")
## -- start Rocking
file.write("G4 P1000\n")
file.write("M117 Rocking the PCB..\n")
t = ((backPosition-frontPosition)/speed)
timeMix = int((timeMix*60)/t)
for i in range(timeMix):
    file.write(
    "G1 Y"+str(int(backPosition)) +" F"+str(int(speed))+"\n"+
    "G1 Y"+str(int(frontPosition))+" F"+str(int(speed))+"\n")
## -- close file
file.close()
