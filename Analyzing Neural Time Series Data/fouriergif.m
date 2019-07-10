%适用于在�?��图中表现给图过程，即图形的增长过�?

%主要用来绘制三维的欧拉公�?
clc;clear;clf;close all;

%获得数据
tmax = 4*pi;
t = 0:0.01:tmax;
tmp = exp(1i*t);
x = real(tmp);
y = imag(tmp);
[a,b] = size(x);
y1 = zeros(a,b) ;
x1 = zeros(a,b);

%确定首幅图的样式，并指定标题，坐标轴标题等样�?
plot3(x(1,1),t(1,1),y(1,1),'black');
hold on
plot3(x(1,1),t(1,1),y1(1,1),'blue');
plot3(x1(1,1),t(1,1),y(1,1),'r');
axis([-1,1,0,tmax,-1,1])
str = ['$${e^{it}} = \cos t + i\sin t $$'];
title({str},'Interpreter','latex')
xlabel('Real Axis');
ylabel('Time');
zlabel('Imaginary Axis');
grid on;
set(gcf,'Position',[0,0,600,600], 'color','w');
set(gca,'ydir','reverse')   %反转坐标�?

%确保图像在采集的过程中包括坐标轴及标�?
ax = gca;
ax.Units = 'pixels';
pos = ax.Position;
ti = ax.TightInset;
rect = [-ti(1), -ti(2), pos(3)+ti(1)+ti(3), pos(4)+ti(2)+ti(4)];

%在指定的范围内获得图像文�?
frame = getframe(ax,rect);
im=frame2im(frame);

%创建gif文件，指定其样式，写入首帧图�?
k = 1;
%用胞元存储采集到的图像，方便后面反转图像�?
[I{k},map{k}]=rgb2ind(im,256);
imwrite(I{k},map{k,1},'fouriergif.gif','gif','Loopcount',Inf,'DelayTime',0.2);
 k = k + 1;

%画图并采集到gif�?
steptmp = 20;   %每幅图要画的点数
i = steptmp;
while i < (b-1)
    x_1 = x(1,(i-steptmp+1):i+1);
    t_1 = t(1,(i-steptmp+1):i+1);
    y_1 = y(1,(i-steptmp+1):i+1);
    y1_1 = y1(1,(i-steptmp+1):i+1);
    x1_1 = x1(1,(i-steptmp+1):i+1);
    plot3(x_1,t_1,y_1,'black');
    hold on
    plot3(x_1,t_1,y1_1,'blue');
    plot3(x1_1,t_1,y_1,'r');

    %下面是制作gif的主要代码，除了调节间隔时间外，�?��不需要改�?
    ax = gca;
    ax.Units = 'pixels';
    pos = ax.Position;
    ti = ax.TightInset;
    rect = [-ti(1), -ti(2), pos(3)+ti(1)+ti(3), pos(4)+ti(2)+ti(4)];
    frame = getframe(ax,rect);
    im=frame2im(frame);
    [I{k},map{k}]=rgb2ind(im,256);
    %写入模式为�?追加”模�?
    imwrite(I{k},map{k},'fouriergif.gif','gif','WriteMode','append','DelayTime',0.1);  
    k = k + 1;

    i = i + steptmp;
end

%将图像按相反的顺序再写入到gif�?
for i = (k-1):-1:1
imwrite(I{i},map{i},'fouriergif.gif','gif','WriteMode','append','DelayTime',0.1);  
end