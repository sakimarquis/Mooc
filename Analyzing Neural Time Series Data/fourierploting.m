clc; 
clear; 
clf; 
tmax = 8*pi; 
xl =2.8;
t = 0:0.01:tmax; 
tmp = exp(1i*t);
x = real(tmp); 
y = imag(tmp); 
[a,b] = size(x);
y1 = zeros(a,b) - xl;
x1 = zeros(a,b) + xl;
figure(1); 
plot3(x,t,y,'black');
hold on 
plot3(x,t,y1); 
plot3(x1,t,y);
axis([-xl,xl,-xl*pi,tmax + xl * pi,-xl,xl]) 
title({'$${e^{it}} = \cos t + i\sin t$$'},'Interpreter','latex') 
xlabel('Real Axis'); ylabel('Time'); 
zlabel('Imaginary Axis'); 
grid on;

tmp = exp(-1i*t); 
x = real(tmp); 
y = imag(tmp); 
[a,b] = size(x); 
y1 = zeros(a,b) - xl;
x1 = zeros(a,b) + xl;
figure(2); 
plot3(x,t,y,'black'); 
hold on 
plot3(x,t,y1);
plot3(x1,t,y);
axis([-xl,xl,-xl*pi,tmax + xl * pi,-xl,xl]) 
title({'$${e^{-it}} = \cos t - i\sin t$$'},'Interpreter','latex') 
xlabel('Real Axis'); ylabel('Time'); 
zlabel('Imaginary Axis'); 
grid on; 
tmp = (exp(-1i*t)+exp(1i*t))*0.5;
x = real(tmp); y = imag(tmp); 
[a,b] = size(x); 
y1 = zeros(a,b) - xl;
x1 = zeros(a,b) + xl; 
figure(3); 
plot3(x,t,y,'black');
hold on
plot3(x,t,y1); 
plot3(x1,t,y);
axis([-xl,xl,-xl*pi,tmax + xl * pi,-xl,xl])
title({'$$\cos \left( t \right) = {1 \over 2}\left( {{e^{it}} + {e^{ - it}}} \right)$$'},'Interpreter','latex') 
xlabel('Real Axis'); ylabel('Time'); zlabel('Imaginary Axis'); grid on;

tmp = (-exp(-1i*t)+exp(1i*t))*0.5;
x = real(tmp); y = imag(tmp); 
[a,b] = size(x); y1 = zeros(a,b) - xl; x1 = zeros(a,b) + xl;
figure(4); 
plot3(x,t,y,'black'); 
hold on
plot3(x,t,y1); plot3(x1,t,y); 
axis([-xl,xl,-xl*pi,tmax + xl * pi,-xl,xl]) 
title({'$$\sin \left( t \right) = {1 \over 2i}\left( {{e^{it}} - {e^{ - it}}} \right)$$'},'Interpreter','latex') 
xlabel('Real Axis'); ylabel('Time'); zlabel('Imaginary Axis'); grid on;