clc; clear all; close all;
rect=[1022.25000000000 19.2500000000000 228 639.000000000000];
for i=500:-1:1
    stc=strcat('ds3\',num2str(i),'.jpg');
    stc1=strcat('data\',num2str(i),'.jpg')
    %stc=strcat(pathx,fnamex);
    bodyDetector = vision.CascadeObjectDetector('UpperBody');
   bodyDetector.MinSize = [40 40];
   bodyDetector.MergeThreshold = 10;
   I2 = imread(stc);
   Ir=adapthisteq(I2(:,:,1));
   Ig=adapthisteq(I2(:,:,2));
   Ib=adapthisteq(I2(:,:,3));
   I2=cat(3,Ir,Ig,Ib);
 %  I2 = imcrop(I2,[40,100,40,100]);
  %I2=imcrop(I2,[361 0 1280 720]);
  figure(1);
   imshow(I2);
   bboxBody = step(bodyDetector, I2);
   
   figure(1);
   imshow(I2);hold on;
   
    IBody = insertObjectAnnotation(I2, 'rectangle',rect,'Person 1','Color','Green');
    imshow(IBody);
    pause(0.0001);
    hold off;
%   Annotate detected upper bodies.
      I2 = imcrop(I2,rect);
        imwrite(I2,stc1);
   %end
end
