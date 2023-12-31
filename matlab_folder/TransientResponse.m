% Time response

clc; clear; close all;

%% 

p1 = [1 3+7*i];
p2 = [1 3-7*i];

deng = conv(p1 ,p2);

% natural frequency
omegan = sqrt(deng(3)/deng(1));

% damping ratio
zeta = (deng(2)/deng(1))/(omegan*2);

% peak time
Tp = pi/(omegan*sqrt(1 - zeta^2));

% settling time
Ts = 4/(zeta*omegan);

% %OS
pos = 100*exp(-zeta*pi/sqrt(1 - zeta^2));

%% step response (tf form)

num = [24.542];
den = [1 4 24.542];
T = tf(num, den)
step(T)
%% step response display SS

A = [0 1 0; 0 0 1; -9 -8 -7];
B = [7;8;9];
C = [2 3 4];
D = 0;

T = ss(A, B, C, D);
t = 0:0.1:10;

step(T, t)
grid on
