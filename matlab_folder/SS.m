% State space
clc; clear;close all;

%% A, B, C, D: ss representation

A = [0 1 0; 0 0 1; -9 -8 -7];
B = [7;8;9];
C = [2 3 4];
D = 0; 

F = ss(A, B, C, D);

%% Transfer function to state space and vice versa

[A, B, C, D] = tf2ss(24, [1 9 26 24]);

%% ss2tf

A = [0 1 0; 0 0 1; -9 -8 -7];
B = [7;8;9];
C = [2 3 4];
D = 0;

% one way
T = ss(A,B,C,D);
Tss = tf(T);
% turn into factored form
Tzpk = zpk(Tss);

% other way (there is bug)
[n, d] = ss2tf(A, B, C, D, 1);

%% 