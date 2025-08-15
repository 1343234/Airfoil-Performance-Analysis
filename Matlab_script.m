% constants derived from SolidWorks CFD Analysis for a NACA 2412 airfoil.
air_density = 1.2;  % kg/m^3
wing_area = 0.4;  % m^2 (Reference Area)
CD = 0.0188; % Coefficient of Drag
CL = 0.1367; % Coefficient of Lift



% array of velocities to model (1 m/s to 100 m/s)
velocities_to_test = linspace(1, 100, 200);
    
disp('Calculating lift and drag forces for velocities from 1 m/s to 100 m/s...');


% calculate lift and drag forces for the range of velocitie
common_factor = 0.5 * air_density * (velocities_to_test.^2) * wing_area;
lift_results = CL * common_factor;
drag_results = CD * common_factor;

% power = Force * Velocity
power_results = drag_results .* velocities_to_test;

% generate and save the plots
disp('Generating and saving performance plots...');

% create a stacked plot with two subplots
figure('Name', 'Aerodynamic Performance of NACA 2412 Airfoil');

% plot 1: Combined Lift and Drag vs. Velocity
subplot(2, 1, 1);
plot(velocities_to_test, lift_results, 'b-', 'LineWidth', 1.5);
hold on;
plot(velocities_to_test, drag_results, 'r-', 'LineWidth', 1.5);
hold off;
title('Lift and Drag Forces vs. Velocity');
xlabel('Velocity (m/s)');
ylabel('Force (N)');
grid on;
legend('Lift Force', 'Drag Force');

% plot 2: Power vs. Velocity 
subplot(2, 1, 2);
plot(velocities_to_test, power_results, 'g-', 'LineWidth', 1.5);
title('Power Required to Overcome Drag');
xlabel('Velocity (m/s)');
ylabel('Power (Watts)');
grid on;

% save plots

saveas(gcf, 'performance_curves_stacked.png');
disp("Plot saved as 'performance_curves_stacked.png'");



while true
    user_input = input("Enter velocity to test (or press Enter to exit): ", 's');
    if isempty(user_input)
        disp("Exiting the program.");
        break
    end
    try
        velocity = str2double(user_input);
        if isnan(velocity)
            error('InvalidInput');
        end

        % calculate lift and drag 
        common_factor_single = 0.5 * air_density * (velocity^2) * wing_area;
        lift = CL * common_factor_single;
        drag = CD * common_factor_single;
        
        % power 
        power = drag * velocity;
        
        fprintf('\nResults for velocity %.1f m/s:\n', velocity);
        fprintf('Lift Force: %.2f N\n', lift);
        fprintf('Drag Force: %.2f N\n', drag);
        fprintf('Power Required: %.2f W\n\n', power);
    catch
        disp("Invalid input. Please enter a number or press Enter to exit.");
    end
end