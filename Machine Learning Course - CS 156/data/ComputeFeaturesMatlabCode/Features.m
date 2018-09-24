clear
format short g

%%%%%%construct the features 

load zip.train
Ftrain=ComputeFeatures(zip);
load zip.test
Ftest=ComputeFeatures(zip);


save features.train Ftrain -ascii
save features.test Ftest -ascii

%%%%%%

%%%%%%make a scatter-plot of the features

j0=find(Ftrain(:,1)~=1);
j1=find(Ftrain(:,1)==1);
figure(1)
l=plot(Ftrain(j0,2),Ftrain(j0,3),'rx',Ftrain(j1,2),Ftrain(j1,3),'bo');
h=gca;
set(h,'FontSize',28)
set(l(2),'MarkerSize',14);
set(l(1),'MarkerSize',12);
set(l,'LineWidth',2)
leg=legend(l,'not 1 ','Digit 1',4);
set(leg,'LineWidth',4,'FontSize',20);
xh=xlabel('Intensity');set(xh,'FontSize',25);
yh=ylabel('Symmetry');set(yh,'FontSize',25);
axis([0 0.7 -8 0.1]);
set(h,'XTick',[])
set(h,'YTick',[])
set(gca,'LineWidth',4,'Color','none')
axis square
export_fig('featuresScatter.png','-png','-transparent',gcf);
%%%%%%


