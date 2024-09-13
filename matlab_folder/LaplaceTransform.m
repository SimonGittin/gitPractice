% Laplace transform and inverse laplace
% Later on, applications will be introduced
clc; clear; close all;

%% Polynomial representation (s+3)(s+2) & s^2+4s+2
% find roots, concatenate polys

P1 = poly([-3 -2]);
P2 = [1 4 2];
rootP1 = roots(P1);
concP = conv(P1, P2);
%% Two transfer function representation

% zeros, poles, gains
F1 = zpk([], [-1 -2 -2], 2);
F2 = tf(2, [1 5 5 4]);

% F1 == F2

%% Find laplace (can only find it by "symbol" it)

syms t

f = laplace(t*exp(-5*t));
pretty(f)


%% Find inverse laplace (can only find it by "symbol" it)

syms s
f = ilaplace(3/(s*(s^2 + 2*s + 5)));
pretty(f)
%% Partial Fraction Expansion

numf = 3;
denf = [1 2 5 0];
[K, p, k] = residue(numf, denf)

%% %% Electrical circuit mesh solution p.52: Skill-assesment 2.6

syms s i1 i2 i3 v

A = [(s+1) -s -1
    -s (2*s+1) -1
    -1 -1 (s+2)];
B = [i1;i2;i3];
C = [v;0;0];

% solves i1 i2 i3
B = inv(A)*C;
pretty(B)

%% Translational mechanical system solution p.60 Skill-assessment 2.8
% suitable for rotational mechanical systems too

syms s x1 x2 f

A = [(s^2+3*s+1) -(3*s+1)
    -(3*s+1) (s^2+4*s+1)];
B = [x1; x2];
C = [f;0];

% solves i1 i2 i3
B = inv(A)*C;
pretty(B)

% basically the same way we do to electrical ones
% thats the way

