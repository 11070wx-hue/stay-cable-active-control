% RUN_OPEN_LOOP_DEMO  Open-loop simulation demo for a reduced stay-cable model.
%
% This script is intentionally compact. It provides a reproducible baseline
% for later controller comparisons such as LQR, MPC, and output-feedback MPC.

clear; clc; close all;

repoRoot = fileparts(fileparts(fileparts(mfilename('fullpath'))));
addpath(genpath(fullfile(repoRoot, 'src', 'matlab')));

p.omega = 1.6425;          % rad/s, first modal circular frequency
p.xi = 0.001;              % damping ratio
p.beta2 = 0.0;             % quadratic nonlinear coefficient
p.beta3 = 0.0;             % cubic nonlinear coefficient
p.excitation_amp = 0.02;   % normalized excitation amplitude
p.excitation_freq = 1.6425;% rad/s

x0 = [0.02; 0.0];          % initial modal displacement and velocity
tspan = [0, 120];

odeOpt = odeset('RelTol', 1e-8, 'AbsTol', 1e-10);
[t, x] = ode45(@(t, x) cable_rhs(t, x, p, 0.0), tspan, x0, odeOpt);

figure('Color', 'w');
plot(t, x(:, 1), 'LineWidth', 1.2);
grid on;
xlabel('Time (s)');
ylabel('Modal displacement');
title('Open-loop stay-cable response');
