# Airfoil-Performance-Analysis

The Python script generates a visualisation of the airfoil's performance characteristics as a function of velocity from 0 m/s to 100 m/s and also provides its aerodynamic performance at specific velocities from user input.

This project is provided as a standalone executable file (naca_2412_airfoil_performance.exe) for Windows, so no installation of Python or any libraries is required. 


## Simulation Parameters

The Solidowrks flow simulation analysis was configured with the following parameters to simulate realistic conditions.

* **Airfoil:** NACA 2412
* **Wing Span:** 3 m
* **Chord Length:** 0.133 m
* **Reference Area:** 0.4 m²
* **Angle of Attack:** 4 degrees
* **Fluid Speed:** 35 m/s
* **Air Density:** 1.2 kg/m³

* **Airfoil Coordinates:** Obtained from [Airfoil Tools](http://airfoiltools.com/airfoil/naca4digit).

## Equations used:

The Python model uses the following standard aerodynamic equations to calculate performance:

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

## Analysis Procedure and Outcome

Using the airfoil coordiantes, it was fist modeled on solidworks. A solidworks flow simulation was then performed to determine the airfoil's lift and drag (data can be found in Solidworks_cdf_data.xlsx) and then its aerodynamic coefficients ($C_L$ and $C_D$) under its specific conditions.

These coefficients are then used as inputs for the Python script. The script implements the standard lift, drag, and power equations to calculate the airfoil's performance across a continuous range of velocities.

The final outcome is a visualization of plots, `performance_curves_stacked.png`, which plots three performance metrics:
* **Lift Force vs. Velocity:** Shows how the airfoil's lifting capability increases with speed.
* **Drag Force vs. Velocity:** Shows how aerodynamic resistance increases with speed.
* **Power vs. Velocity:** Translates the drag force into the energy required to overcome it, providing a direct measure of the airfoil's efficiency.

The executable program is created with PyInstaller.

## Installation

* Download the naca_2412_airfoil_performance.exe file from this GitHub repository.

* Run the application by double-clicking the .exe file.

* Command-line window will appear, and the script will execute in 5 to 10 seconds. The final performance_curves_stacked.png plot will be saved in the same folder where the executable was ran.



**Simulation Software used**: SolidWorks Flow Simulation

**Programming Language**: Python 

### Libraries used:

NumPy: For numerical calculations and array management.

Matplotlib: For generating plots.
