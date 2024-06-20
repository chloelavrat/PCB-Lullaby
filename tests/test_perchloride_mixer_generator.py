import pytest
import os

from src.perchloride_mixer_generator import process

@pytest.mark.parametrize(
    "filename, zPosition, numWait, bedTemp, backPosition, frontPosition, speed, timeMix, expected_lines",
    [
        # Happy path tests
        ("test1.gcode", 200, 2, 30, 150, 120, 1500, 0.001, [
            "G28\n", 
            "G90\n",
            "G0 Z200\n",
            "M117 Place Circuit NOW! 2\n", "G4 P1000\n",
            "M117 Place Circuit NOW! 1\n", "G4 P1000\n",
            "M117 Circuit Rocking G-Code\n",
            "G0 Z200\n",
            "G28 X0 Y0\n",
            "M18\n", 
            "M117 Heating Bed To 30°C\n", "M190 S30\n", 
            "G4 P1000\n",
            "M117 Rocking the PCB..\n", 
            "G1 Y150 F1500\n", "G1 Y120 F1500\n",
            "G1 Y150 F1500\n", "G1 Y120 F1500\n",
            "G1 Y150 F1500\n", "G1 Y120 F1500\n",
        ]),
        ("test2.gcode", 20, 3, 60, 15, 12, 1500, 0.002, [
            "G28\n", 
            "G90\n",
            "G0 Z20\n",
            "M117 Place Circuit NOW! 3\n", "G4 P1000\n",
            "M117 Place Circuit NOW! 2\n", "G4 P1000\n",
            "M117 Place Circuit NOW! 1\n", "G4 P1000\n",
            "M117 Circuit Rocking G-Code\n",
            "G0 Z200\n",
            "G28 X0 Y0\n",
            "M18\n", 
            "M117 Heating Bed To 60°C\n", "M190 S60\n", 
            "G4 P1000\n",
            "M117 Rocking the PCB..\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
            "G1 Y15 F1500\n", "G1 Y12 F1500\n",
        ]),
    ],
    ids=[
        "happy_path_1", "happy_path_2"
    ]
)
def test_process(filename, zPosition, numWait, bedTemp, backPosition, frontPosition, speed, timeMix, expected_lines):
    # Act
    process(filename, zPosition, numWait, bedTemp, backPosition, frontPosition, speed, timeMix)

    # Assert
    with open(filename, 'r') as file:
        lines = file.readlines()
        assert lines == expected_lines

    # Cleanup
    os.remove(filename)
