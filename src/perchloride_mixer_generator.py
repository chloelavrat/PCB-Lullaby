## --------------------------------------------
## Title : Perchloride mixer gcode
## Author : C.Lavrat
## Date : 2021/01/23
## -----------------------------------------------------------------------

def process(fileName, zPosition, numWait, bedTemp, backPosition, frontPosition, speed, timeMix):
    with open(fileName, 'w') as file:
        ## -- Place plate
        file.write("G28\n") # Move the X,Y,Z to absolute position
        file.write("G90\n") # Absolute programming in relation to the program origin
        file.write(f"G0 Z{int(zPosition)}" + "\n")
        for i in range(numWait):
            file.write(f"M117 Place Circuit NOW! {str(numWait - i)}" + "\nG4 P1000\n")
        file.write("M117 Circuit Rocking G-Code\nG0 Z200\n")
        ## -- init zero
        file.write("G28 X0 Y0\n") # move to X=0 Y=0
        ## -- stepper motors
        file.write("M18\n") # M18: Disable all stepper motors to save energie
        if bedTemp != 0:
            file.write(f"M117 Heating Bed To {int(bedTemp)}" + "°C\n")
            file.write(f"M190 S{int(bedTemp)}" + "\n")
        ## -- start Rocking
        file.write("G4 P1000\n")
        file.write("M117 Rocking the PCB..\n")
        t = ((backPosition-frontPosition)/speed)
        timeMix = int((timeMix*60)/t)
        for _ in range(timeMix):
            file.write(
                (
                    (
                        (
                            (f"G1 Y{int(backPosition)} F{int(speed)}" + "\n")
                            + "G1 Y"
                        )
                        + str(int(frontPosition))
                        + " F"
                    )
                    + str(int(speed))
                    + "\n"
                )
            )


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Perchloride mixer gcode')
    parser.add_argument('filename', metavar='FILE', type=str, help='name of the gcode file')
    parser.add_argument('--bedTemp', type=int, default=30, help='bed temperature (default: 30)')
    parser.add_argument('--timeMix', type=int, default=1, help='duration of the mix, in minutes (default: 1)')
    parser.add_argument('--numWait', type=int, default=2, help='number of messages at start ("Place Circuit NOW!") (default: 2)')
    parser.add_argument('--speed', type=int, default=2000, help='speed of the bed (default: 2000)')
    parser.add_argument('--zPosition', type=int, default=200, help='Z position to free space for the glass container (default: 200)')
    parser.add_argument('--frontPosition', type=int, default=125, help='X position of bed in front mode (default: 125)')
    parser.add_argument('--backPosition', type=int, default=150, help='Y position of bed in back mode (default: 150)')

    args = parser.parse_args()

    filename = args.filename
    bedTemp = args.bedTemp
    timeMix = args.timeMix
    numWait = args.numWait
    speed = args.speed
    zPosition = args.zPosition
    frontPosition = args.frontPosition
    backPosition = args.backPosition

    # call the process function

    process(filename, zPosition, numWait, bedTemp, backPosition, frontPosition, speed, timeMix)