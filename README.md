
# GuiPlot
Simple GUI program that allows you to create a chart from a `.txt` file.

<img align="right" width="33%" src="https://cdn-icons.flaticon.com/png/512/1807/premium/1807350.png?token=exp=1636196066~hmac=cef44ea793e045280015e06c74468d63">

## Table of contents

* [General info](#general-info)
* [Installation](#installation)
* [How to run it](#how-to-run-it)
* [Basic usages](#basic-usages)
* [License](#license)

## General info
Simple GUI program that allows you to create a chart from a `.txt` file.
The program allows you to create points and draw a trendline.
## Installation

1. Git clone repository:
```bash
$ git clone https://github.com/gunater/ChartingPrograms.git
```
2. Install the necessary python dependencies you can use `pipenv`:
```bash
$ pipenv install
$ piipenv shell
```
or you can install from requirements.txt with `pip`:
```bash
$ pip install -r requirements.txt
```
## How to run it
To run the script, go to the main directory:
```bash
$ cd GuiPlot/
```
and then run script with an argument `--help`:
```bash
$ python3 uiplot.py
```
## Basic usages
As shown in the figure below, you must first specify the name of the data file, which should be in the same folder as the program. Then select the options we need and fill in the labels. Click plot it and enjoy the graph !

<p align="center">
  <img align="center" width="auto" src="https://github.com/gunater/ChartingPrograms/blob/master/assets/1.png?raw=true">
</p>
below is the output chart:
<p align="center">
  <img align="center" width="487" src="https://github.com/gunater/ChartingPrograms/blob/master/assets/2.png?raw=true">
</p>

## License
All code is licensed under an MIT license. This allows you to re-use the code freely, remixed in both commercial and non-commercial projects. The only requirement is to include the same license when distributing.

