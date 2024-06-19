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

To get started with the PCB Lullaby project, you will need an Ender 3 Pro 3D printer and an etching tank. To use the _pcb-lullaby_ code, follow these steps:

```
$ git clone https://github.com/azerty-labs/PCB-Lullaby.git
$ cd pcb-lullaby
```

Then you can directly run the python code as the script depends on no external library. To use this Python script with argparse, you need to open a terminal and type:

```
python ./src/perchlo_mixer_gcode.py FILE [--bedtemp BEDTEMP] [--timemix TIMEMIX] [--numwait NUMWAIT] [--speed SPEED] [--zposition ZPOSITION] [--frontposition FRONTPOSITION] [--backposition BACKPOSITION]
```

Note that the default value are for an Ender-3 Pro 3D-printer:

```
$ python ./src/perchloride_mixer_generator -h
usage: perchloride_mixer_generator [-h] [--bedtemp BEDTEMP] [--timemix TIMEMIX] [--numwait NUMWAIT]
                                  [--speed SPEED] [--zposition ZPOSITION]
                                  [--frontposition FRONTPOSITION] [--backposition BACKPOSITION]
                                  FILE

perchloride mixer gcode

positional arguments:
  FILE                  name of the gcode file

options:
  -h, --help            show this help message and exit
  --bedtemp BEDTEMP     bed temperature (default: 30)
  --timemix TIMEMIX     duration of the mix, in minutes (default: 1)
  --numwait NUMWAIT     number of messages at start ("Place Circuit NOW!") (default: 2)
  --speed SPEED         speed of the bed (default: 2000)
  --zposition ZPOSITION
                        Z position to free space for the glass container (default: 200)
  --frontposition FRONTPOSITION
                        X position of bed in front mode (default: 125)
  --backposition BACKPOSITION
                        Y position of bed in back mode (default: 150)
```

Here's an example of how to use this script:

```
python ./src/perchloride_mixer_generator.py my_circuit.gcode --bedtemp 30 --timemix 2 --numwait 3 --speed 1500 --zposition 150 --frontposition 120 --backposition 145
```

This will create a new G-code file called `my_circuit.gcode` with the given parameters. Note that if you omit any of the optional arguments, the script will use the default values.

## Contributing

The PCB Lullaby project is an open-source project, and contributions are always welcome. If you would like to contribute to the project, you can do so by submitting a pull request or by creating an issue on the project's GitHub page.

## Demo

[![PCB Lullaby](https://img.youtube.com/vi/_3DP3HD8CqY/0.jpg)](http://www.youtube.com/watch?v=_3DP3HD8CqY)

## License

The PCB Lullaby project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
