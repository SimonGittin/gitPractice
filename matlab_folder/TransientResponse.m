% Time response

clc; clear; close all;

%% Second order parameters

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

%% step response  (SS form)

A = [0 1 0; 0 0 1; -9 -8 -7];
B = [7;8;9];
C = [2 3 4];
D = 0;

T = ss(A, B, C, D);
t = 0:0.1:10;

step(T, t)
grid on

%% step response with SS with x(0) initial state vector

syms s

A = [0 1 0; 0 0 1; -24 -26 -9];
B = [0; 0; 1];
C = [1 1 0];
X0 = [1; 0; 2];
U = 1/(s+1); %exp(-t)


I = eye(3);

% visit (4.96) solve X
X = ((s*I - A)^-1)*(X0 + B*U);

% visit (4.97) solve Y
Y = C*X;
Y = simplify(Y)

% show graph
step(tf([1 11 5], [1 9 26 24]))

% solve y(t)
y = ilaplace(Y);
pretty(y)

% find eigenvalues of A which are poles of Y(s)
eig(A)


%% if U(s) is 1/s, graph becomes ramp line which is to be discussed