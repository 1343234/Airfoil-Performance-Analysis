# Airfoil-Performance-Analysis

This project has both a Python and a MATLAB version to generate a graph of a specifc modeled airfoil's aerodynamic performance characteristics of velocities from 0 m/s to 100 m/s. It also includes its performance at specific velocities from user input. Both versions outputs the same result.

### Windows Executable (`.exe`)
First version is a independent executable file (naca_2412_airfoil_performance.exe) for Windows. 

* Download and run the `naca_2412_airfoil_performance.exe` file.
* A stacked plot will be generated and saved as `performance_curves_stacked.png` which displays the airfoil's aerodynamic performance across 0 m/s to 100 m/s.
*  Afterwards, the command-line window will prompt the user for any specific velocity to output results for that single point.

### MATLAB Script (`.m`)
This version is a MATLAB script.

* Download and run the `main.m` file in MATLAB.
* The script will generate and save a stacked plot (`performance_curves_stacked_MATLAB.png`). Note that this is identical to the plot generated from the python script.
* Afterwards, the command window will prompt the user to enter any specific velocity to output results for that single point.


## Simulation Parameters

The Solidowrks flow simulation analysis was run with the following parameters:

* **Airfoil:** NACA 2412
* **Wing Span:** 3 m
* **Chord Length:** 0.133 m
* **Reference Area:** 0.4 m²
* **Angle of Attack:** 4 degrees
* **Fluid Speed:** 35 m/s
* **Air Density:** 1.2 kg/m³

* **Airfoil Coordinates:** Obtained from [Airfoil Tools](http://airfoiltools.com/airfoil/naca4digit).

## Equations used:

The Python script uses the following  aerodynamic equations:

#### Coefficient of Lift and Lift Force:
$$
F_L = C_L \cdot \frac{1}{2} \rho v^2 A
$$

#### Coefficient of Drag and Drag Force:
$$
F_D = C_D \cdot \frac{1}{2} \rho v^2 A
$$

#### Power Loss to Overcome Drag:
$$
P = F_D \cdot v
$$

Where:
* **$F_L$**: Lift Force (N)
* **$F_D$**: Drag Force (N)
* **$C_L$**: Coefficient of Lift
* **$C_D$**: Coefficient of Drag
* **$\rho$**: Density of air (kg/m³)
* **$v$**: Velocity (m/s)
* **$A$**: Reference Area (m²)
* **$P$**: Power (Watts)

## Method of Analysis 

Using the airfoil coordiantes, the airfoil was fist modeled on solidworks. A solidworks flow simulation at the specefic conditions was then performed to determine the airfoil's lift and drag (data can be found in Solidworks_cdf_data.xlsx) and then its aerodynamic coefficients ($C_L$ and $C_D$) was calcualted using the data.

These coefficients are then used for the Python script. The script uses the equations to output lift, drag, and power.

The final outcome, `performance_curves_stacked.png`, plots:
* **Lift Force vs. Velocity** 
* **Drag Force vs. Velocity** 
* **Power vs. Velocity** 

The executable program was made with PyInstaller.

**Simulation Software used**: SolidWorks Flow Simulation

**Programming Language**: Python 

### Libraries used:

NumPy: For numerical calculations and array management.

Matplotlib: For generating plots.
