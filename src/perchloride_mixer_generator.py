"""
Title  : Perchloride mixer gcode
Author : C.Lavrat
Date   : 2021/01/23
"""
def process(filename: str, zPosition: int, numWait: int, bedTemp: int, backPosition: int, frontPosition: int, speed: int, timeMix: float) -> None:
    """
    Processes the PCB mixing operation and generates G-code instructions.

    Args:
        filename: The name of the file to write the G-code instructions to.
        zPosition: The Z-axis position for the PCB.
        numWait: The number of waiting cycles.
        bedTemp: The temperature for heating the bed.
        backPosition: The back position for the PCB.
        frontPosition: The front position for the PCB.
        speed: The speed of the PCB movement.
        timeMix: The time duration for mixing.

    Returns:
        None
    """
    with open(filename, 'w') as file:
        ## -- Place plate
        file.write("G28\nG90\n")
        file.write(f"G0 Z{zPosition}\n")
        for i in range(numWait):
            file.write(f"M117 Place Circuit NOW! {numWait - i}\nG4 P1000\n")
        file.write("M117 Circuit Rocking G-Code\nG0 Z200\n")
        ## -- init zero
        file.write("G28 X0 Y0\nM18\n")
        if bedTemp != 0:
            file.write(f"M117 Heating Bed To {bedTemp}°C\nM190 S{bedTemp}\n")
        ## -- start Rocking
        file.write("G4 P1000\nM117 Rocking the PCB..\n")
        
        t = (backPosition - frontPosition) / (speed if speed != 0 else 100)
        timeMix = int((timeMix * 60) / t)
        
        for _ in range(timeMix):
            file.write(f"G1 Y{backPosition} F{speed}\nG1 Y{frontPosition} F{speed}\n")



if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Perchloride mixer gcode')
    parser.add_argument('filename', metavar='FILE', type=str, help='name of the gcode file')
    parser.add_argument('--bedTemp', type=int, default=30, help='bed temperature (default: 30)')
    parser.add_argument('--timeMix', type=float, default=1, help='duration of the mix, in minutes (default: 1)')
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