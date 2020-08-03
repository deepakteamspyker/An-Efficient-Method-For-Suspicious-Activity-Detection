clc; clear all; close all;
outputname='ds2\';
path='ds2\';
outputname1='ds2\';
imageName = 'img';
imgPx=imread('marker.jpg');
my=1;ny=1;t=1;
obj=imread(strcat(path,num2str(1),'.jpg'));
tx=1;
count=0;
for i=1:5:375
    %obj=imread(strcat('MotionVectImages\',num2str(i),'.jpg'));
   obj1=imread(strcat(path,num2str(i),'.jpg'));
   objimset{tx}=rgb2gray(obj1);
    objx=imsubtract(rgb2gray(obj),rgb2gray(obj1));
    xst1(tx)=mean(mean(mean(uint8(objx))));
    tx=tx+1;
    count=count+1;
end
%save sus.mat xst xst1
t=1;
for i=1:length(xst1)-1
    temp(i)=xst1(i)-xst1(i+1);
    %fprintf('temp=%f i=%d\n',temp,i);
end
sorted=sort(temp,'descend');
mx1=sorted(1);
for i=1:length(xst1)-1
    if temp(i)==sorted(i)
          suspicious(t)=i;
          t=t+1;
    end
end
figure();
plot(xst1);grid on;
title('Frame object containing analysis');

for i=1:count-1
Options.upright=true;
  Options.tresh=0.0065;
  frame1=objimset{i};
  im2=objimset{i+1};
  Ipts1=OpenSurf(frame1,Options);
  Ipts2=OpenSurf(im2,Options);
  D1 = reshape([Ipts1.descriptor],64,[]); 
  [mxp,nxp]=size(D1);
  D2 = reshape([Ipts2.descriptor],64,[]); 
  [mxp1,nxp1]=size(D2);
% Find the best matches
  err=zeros(1,length(Ipts1));
  cor1=1:length(Ipts1); 
  cor2=zeros(1,length(Ipts1));
  for i=1:length(Ipts1),
      distance=sum((D2-repmat(D1(:,i),[1 length(Ipts2)])).^2,1);
      [err(i),cor2(i)]=min(distance);
  end
  err1=err;
% Sort matches on vector distance
  [err, ind]=sort(err); 
  fprintf('Matching points %d \n',length(ind));
end
