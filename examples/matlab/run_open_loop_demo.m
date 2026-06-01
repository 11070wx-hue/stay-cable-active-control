%RUN_OPEN_LOOP_DEMO Reproducible MATLAB open-loop stay-cable example.

addpath(genpath(fullfile(fileparts(mfilename('fullpath')), '..', '..', 'src', 'matlab')));

p = struct();
p.damping_ratio = 0.003;
p.cubic_stiffness = 0.08;
p.excitation_amplitude = 0.02;

tspan = [0, 20];
x0 = [0.02; 0.0];
[time, state] = ode45(@(t, x) cable_state_rhs(t, x, p, 0.0), tspan, x0);

rms_displacement = sqrt(mean(state(:, 1).^2));
peak_displacement = max(abs(state(:, 1)));

fprintf('open_loop: rms=%.6f, peak=%.6f\n', rms_displacement, peak_displacement);
fprintf('samples=%d, t_final=%.2f\n', numel(time), time(end));
