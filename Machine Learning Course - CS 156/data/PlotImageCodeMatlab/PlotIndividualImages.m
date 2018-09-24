% This M-file constructs the individual images for 60 digits
% and plots them to a file.
% The file zip.train containing raw images is assumed to be in the directory.
% The number of images to show is NumIm

clear
format short g
load zip.train		%raw data containing images.
NumIm=9;		%number of images to plot.


digits=zip(:,1);
grayscale=zip(:,2:end);
[n,d]=size(grayscale);
w=floor(sqrt(d));

%Plot the first NumIm digits and pring to .png file.
for i=1:NumIm
	[i, digits(i)]
	curimage=reshape(grayscale(i,:),w,w);
	curimage=curimage';
	l=displayimage(curimage);
	sstr=['image',int2str(i)];
	set(gca,'LineWidth',12,'Color','none');
	export_fig(sstr,'-png','-transparent',gcf);
end
