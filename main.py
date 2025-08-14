import numpy as np
import matplotlib.pyplot as plt

# Constants derived from SolidWorks CFD Analysis for a NACA 2412 airfoil.
air_density = 1.2  # kg/m^3
wing_area = 0.4  # m^2 (Reference Area)
CD = 0.0188 # Coefficient of Drag
CL = 0.1367 # Coefficient of Lift

# functions

def calculate_forces(velocity, cd, cl, area, density):
    """
    Calculates the lift and drag forces using the drag force formula and the lift formula.

    Args:
        velocity (float or np.ndarray): The velocity of the fluid in m/s.
        cd (float): The coefficient of drag.
        cl (float): The coefficient of lift.
        area (float): The reference area in m^2.
        density (float): The density of the fluid in kg/m^3.

    Returns:
        tuple: A tuple containing the lift force and drag force in N.
    """

    # Common factor in both lift and drag equations
    common_factor = 0.5 * density * velocity**2 * area
    
    lift_force = cl * common_factor
    drag_force = cd * common_factor
    
    return lift_force, drag_force

def calculate_power(drag_force, velocity):
    """
    calculates the power required to overcome drag using the formula: Power = Force * Velocity.

    args:
        drag_force (float or np.ndarray): The drag force in N.
        velocity (float or np.ndarray): The velocity of the fluid in m/s.

    returns:
        float or np.ndarray: The power in Watts.
    """
    # Power = Force * Velocity
    power = drag_force * velocity
    return power

def plot_performance_stack(velocities, lift_forces, drag_forces, power_values):
    """
    generates and saves plots of the airfoil's performance (lift and drag forces, and power required to overcome drag).
    """
    # Create a stacked plot with two subplots
    fig, axes = plt.subplots(2, 1, figsize=(6, 8))  # Reduced from (8, 10)
    fig.suptitle('Aerodynamic Performance of NACA 2412 Airfoil', fontsize=12, fontweight='bold', y=0.95)

    # plot 1: Combined Lift and Drag vs. Velocity
    axes[0].plot(velocities, lift_forces, color='blue', linewidth=1.5, label='Lift Force')
    axes[0].plot(velocities, drag_forces, color='red', linewidth=1.5, label='Drag Force')
    axes[0].set_title('Lift and Drag Forces vs. Velocity', fontsize=10, pad=10)
    axes[0].set_xlabel('Velocity (m/s)', fontsize=9)
    axes[0].set_ylabel('Force (N)', fontsize=9)
    axes[0].grid(True, linestyle='--', alpha=0.6)
    axes[0].legend(fontsize=8)
    axes[0].tick_params(labelsize=8)

    # plot 2: Power vs. Velocity 
    axes[1].plot(velocities, power_values, color='green', linewidth=1.5)
    axes[1].set_title('Power Required to Overcome Drag', fontsize=10, pad=10)
    axes[1].set_xlabel('Velocity (m/s)', fontsize=9)
    axes[1].set_ylabel('Power (Watts)', fontsize=9)
    axes[1].grid(True, linestyle='--', alpha=0.6)
    axes[1].tick_params(labelsize=8)
    
    # Adjust spacing between subplots
    plt.subplots_adjust(hspace=0.3)
    
    # Adjust layout
    plt.tight_layout(rect=[0, 0.03, 1, 0.92])
    
    plt.savefig('performance_curves_stacked.png', dpi=200, bbox_inches='tight')
    print("Plot saved as 'performance_curves_stacked.png'")
    
    plt.show()


if __name__ == "__main__":
    # array of velocities to model (from 1 m/s to 100 m/s)
    velocities_to_test = np.linspace(1, 100, 200)
        
    # Calculate lift and drag forces for the range of velocities
    print("Calculating lift and drag forces for velocities from 1 m/s to 100 m/s...\n")
    results = calculate_forces(velocities_to_test, CD, CL, wing_area, air_density)
    lift_results = results[0]  # First element is lift force
    drag_results = results[1]  # Second element is drag force

    power_results = calculate_power(drag_results, velocities_to_test)
    
    # Generate and save the plots
    print("Generating and saving performance plots...\n")
    plot_performance_stack(velocities_to_test, lift_results, drag_results, power_results)

    print("Plots completed and saved successfully. \n")

    while True:
        user_input = input("Enter velocity to test (or press Enter to exit): ")
        if user_input == "":
            print("Exiting the program.")
            break
        try:
            velocity = float(user_input)

            lift, drag = calculate_forces(velocity, CD, CL, wing_area, air_density)
            power = calculate_power(drag, velocity)
            print(f"\nResults for velocity {velocity} m/s:")
            print(f"Lift Force: {lift:.2f} N")
            print(f"Drag Force: {drag:.2f} N")
            print(f"Power Required: {power:.2f} W\n")
        except ValueError:
            print("Invalid input. Please enter a number or press Enter to exit.")



    
