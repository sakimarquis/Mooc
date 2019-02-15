function f=ComputeFeatures(raw)
%Function to compute the symmetry and intensity features of
%raw 16x16 digit images. The first column are the actual digits.

%preprocess the raw file.
digits=raw(:,1);		%the digit corresponding to row.
grayscale=raw(:,2:end);		%the grayscale values
[n,d]=size(grayscale);
w=floor(sqrt(d));

%compute the intensity feature
totsum=zeros(n,1);
for i=1:n
	totsum(i)=mean(grayscale(i,:));
end
totsum=0.5*(1+totsum);		%convert to range [0,1]
%totsum contains the intensity feature

%compute the symmetry feature
horsym=zeros(n,1);		%horizontal asymmetry
				%flip the image horizontally and take
				%the difference in the grayscale values
vertsym=zeros(n,1);		%vertical asymmetry
				%flip the image vertically and take
				%the difference in the grayscale values
for i=1:n
	full=grayscale(i,:);
	for j=1:w/2
		jsym=w+1-j;
		idxH=(j-1)*w+1:j*w;
		idxV=j:w:(w-1)*w+j;
		idxHsym=(jsym-1)*w+1:jsym*w;
		idxVsym=jsym:w:(w-1)*w+jsym;
		H=full(idxH);Hsym=full(idxHsym);
		V=full(idxV);Vsym=full(idxVsym);
		horsym(i)=horsym(i)+mean(abs(H-Hsym));
		vertsym(i)=vertsym(i)+mean(abs(V-Vsym));
	end
end
totsym=[horsym,vertsym];
totsym=mean(totsym')';
totsym=-totsym;			%Because we actually computed asymmetry

f=[digits,totsum,totsym];
