## --------------------------------------------
## Title : Perchlo mixer gcode
## Author : C.Lavrat
## Date : 2021/01/23
## -----------------------------------------------------------------------

def process(fileName, zPosition, numWait, bedTemp, backPosition, frontPosition, speed, timeMix):
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


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Perchlo mixer gcode')
    parser.add_argument('filename', metavar='FILE', type=str, help='name of the gcode file')
    parser.add_argument('--bedtemp', type=int, default=30, help='bed temperature (30 for perchlo + copper, 0 for perchlo + aluminium)')
    parser.add_argument('--timemix', type=int, default=1, help='duration of the mix, in minutes')
    parser.add_argument('--numwait', type=int, default=2, help='number of messages at start ("Place Circuit NOW!")')
    parser.add_argument('--speed', type=int, default=2000, help='speed of the bed')
    parser.add_argument('--zposition', type=int, default=200, help='Z position to free space for the glass container')
    parser.add_argument('--frontposition', type=int, default=125, help='Y position of bed in front mode')
    parser.add_argument('--backposition', type=int, default=150, help='Y position of bed in back mode')

    args = parser.parse_args()

    filename = args.filename
    bedTemp = args.bedtemp
    timeMix = args.timemix
    numWait = args.numwait
    speed = args.speed
    zPosition = args.zposition
    frontPosition = args.frontposition
    backPosition = args.backposition

    # call the process function

    process(filename, zPosition, numWait, bedTemp, backPosition, frontPosition, speed, timeMix)