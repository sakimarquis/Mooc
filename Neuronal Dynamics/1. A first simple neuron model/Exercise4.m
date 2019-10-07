%% Solve
syms u(t) w(t)
    ode1 = diff(u) == -(u + 70) + 2 * exp((u + 50) / 2) - 500 * w;
    ode2 = diff(w) == 0.5 * (u + 70) - w + 7 * 100 * 1;
    odes = [ode1; ode2];
    
[V] = odeToVectorField(odes);
M = matlabFunction(V,'vars', {'t','Y'});
sol = ode45(M,[-100 100],[-100 100]);
fplot(@(x)deval(sol,x,1), [-100 100]);

%% Slope field

[u,w] = meshgrid(-100:10:100);
du = -(u + 70) + 2 * exp((u + 50) / 2) - 500 * w;
dw = 0.5 * (u + 70) - w + 7 * 100 * 1;
r = ( du.^2 + dw.^2 ).^0.5;
pu = du./r;
pw = dw./r;
quiver(u,w,pw,pu);