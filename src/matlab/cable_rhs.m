function dx = cable_rhs(t, x, p, u)
% CABLE_RHS  Reduced single-mode stay-cable vibration model.
%
% State vector:
%   x(1) = modal displacement
%   x(2) = modal velocity
%
% Parameters in structure p:
%   p.omega           first modal circular frequency, rad/s
%   p.xi              damping ratio
%   p.beta2           quadratic nonlinear coefficient
%   p.beta3           cubic nonlinear coefficient
%   p.excitation_amp  normalized excitation amplitude
%   p.excitation_freq excitation circular frequency, rad/s
%
% The control input u is treated as a normalized generalized control force.

if nargin < 4
    u = 0.0;
end

y = x(1);
y_dot = x(2);

external_force = p.excitation_amp * cos(p.excitation_freq * t);

y_ddot = -2.0 * p.xi * p.omega * y_dot ...
         - p.omega^2 * y ...
         - p.beta2 * y^2 ...
         - p.beta3 * y^3 ...
         + external_force ...
         + u;

dx = [y_dot; y_ddot];
end
