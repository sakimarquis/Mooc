function out=displayimage(curimage)
%This is a function that creates a graphical image 
%of a digit which is a 256 row grayscale vector 
%whose entries are in the range [-1,1]

[m,n]=size(curimage);
im=zeros(m,n,3);
for i=1:3	
	im(:,:,i)=0.5*(1-curimage);	%grayscale values in [0,1]
end

out=image(im);
h=gca;
set(h,'XTick',[]);
set(h,'YTick',[]);
