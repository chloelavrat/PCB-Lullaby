# PCB Lullaby

The PCB Lullaby project is a tool designed to make the PCB etching process faster and more efficient by using a 3D printer as a moving bed to mix the etching fluid. The tool can be built with an Ender 3 Pro 3D printer and a few additional components, and it can be used by makers and hobbyists to produce high-quality PCBs with less time and effort.

## How it Works

The PCB Lullaby tool is designed to mix the etching fluid in an etching tank, which is placed on the bed of the 3D printer. The tool uses G-code commands to control the movement of the bed, which moves back and forth to agitate the etching fluid. This helps to speed up the etching process and achieve better results. Furthermore, PCB Lullaby can heat the solution to enhances the chemical process.

## Features

The PCB Lullaby tool includes several features that make it easy to use and customize, including:

- **Calibration**: The tool includes a calibration process to ensure that the 3D printer is properly aligned.
- **Preheating**: The tool can be used to preheat the etching fluid, which enhances the chemical process.
- **Customizable parameters**: The tool includes several customizable parameters, such as bed temperature, mix duration, and speed.

## Getting Started

To get started with the PCB Lullaby project, you will need an Ender 3 Pro 3D printer and an etching tank. To use the *pcb-lullaby* code, follow these steps:

```
$ git clone https://github.com/azerty-labs/PCB-Lullaby.git
$ cd pcb-lullaby
```

Then you can directly run the python code as the script depends on no external library. To use this Python script with argparse, you need to open a terminal and type:

```
python ./code/perchlo_mixer_gcode.py FILE [--bedtemp BEDTEMP] [--timemix TIMEMIX] [--numwait NUMWAIT] [--speed SPEED] [--zposition ZPOSITION] [--frontposition FRONTPOSITION] [--backposition BACKPOSITION]
```

Note that the default value are for an Ender-3 Pro 3D-printer: 

- Replace `FILE` with the name of your G-code file.
- `--bedtemp` is an optional argument that sets the bed temperature to 30°C for perchlo and copper, or 0°C for perchlo and aluminium. Default value is 30.
- `--timemix` is an optional argument that sets the duration of the mix, in minutes. Default value is 1.
- `--numwait` is an optional argument that sets the number of messages at the start ("Place Circuit NOW!"). Default value is 2.
- `--speed` is an optional argument that sets the speed of the bed. Default value is 2000.
- `--zposition` is an optional argument that sets the Z position to free space for the glass container. Default value is 200.
- `--frontposition` is an optional argument that sets the Y position of the bed in front mode. Default value is 125.
- `--backposition` is an optional argument that sets the Y position of the bed in back mode. Default value is 150.

Here's an example of how to use this script:

```
python ./code/perchlo_mixer_gcode.py my_circuit.gcode --bedtemp 30 --timemix 2 --numwait 3 --speed 1500 --zposition 150 --frontposition 120 --backposition 145
```

This will create a new G-code file called `my_circuit.gcode` with the given parameters. Note that if you omit any of the optional arguments, the script will use the default values.

## Contributing

The PCB Lullaby project is an open-source project, and contributions are always welcome. If you would like to contribute to the project, you can do so by submitting a pull request or by creating an issue on the project's GitHub page.

## Demo

[![PCB Lullaby](https://img.youtube.com/vi/_3DP3HD8CqY/0.jpg)](http://www.youtube.com/watch?v=_3DP3HD8CqY)

## License

The PCB Lullaby project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.