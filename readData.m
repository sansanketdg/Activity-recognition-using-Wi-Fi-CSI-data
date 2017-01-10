% READ txt file then make map
%clear all;
clc;

path = 'data_2\position1\subject1\';
d = dir(strcat(path,'*.txt'));

%for i=1:length(d)
for i=1:1
    %fileName = strcat(path,d(i).name);
    fileName = 'Falling_1.txt';
    fileID = fopen(fileName);
    disp(fileID);
    buffer = textscan(fileID, '%d','headerLines',15);
    
    %plot(buffer{1});
    buffer_ = double(buffer{1}');
    hold on;
    
    % Model for DWT, Discrete Wavelet Transform
    [Lo_D,Hi_D,Lo_R,Hi_R] = wfilters('sym45');
    g = dwt(buffer_,Lo_D);
    %y = idwt(g,Lo_R);
    figure(1)
    subplot(3,1,1);plot(buffer_);
    subplot(3,1,2);plot(g);
    %subplot(3,1,3);plot(y);
    
end
    