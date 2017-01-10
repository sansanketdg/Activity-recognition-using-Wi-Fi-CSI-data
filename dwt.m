function g = dwt(f,h)
%  function g = dwt(f,h,NJ); Calculates the DWT of periodic  f
%  with scaling filter  h

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% This script/function was created by 
% Abdullah Al Muhit
% contact - almuhit@gmail.com
% website - https://sites.google.com/site/almuhit/
% Please use it at your own risk. Also, Please cite the following paper:
% A A Muhit, M S Islam, and M Othman, “VLSI Implementation of Discrete Wavelet Transform (DWT) for Image Compression”, in Proc. of The Second International Conference on Autonomous Robots and Agents, Palmerston North, New Zealand, pp. 391-395, 2004, ISBN 0-476-00994-4. [PDF]
% A A Muhit, M S Islam, and M Othman, “ Design Design and Analysis of Discrete Wavelet Transform (DWT) for Image Compression Using VHDL”, in Proc. of the International Conference on Parallel and Distributed Processing Techniques and Applications, PDPTA 2005, Volume 1. CSREA Press 2005, pp. 157-160, Las Vegas, Nevada, USA, 2005, ISBN 1-932415-58-0. [PDF]
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

N = length(h);  L = length(f);
c = f;
h0  = fliplr(h);                          % Scaling filter
h1 = h;  h1(1:2:N) = -h1(1:2:N);          % Wavelet filter

L = length(c);
c = [c(mod((-(N-1):-1),L)+1) c];          % Make periodic

%subplot(3,1,1);plot(f);
%subplot(3,1,2);plot(c);

d = conv(c,h1);   d = d(N:2:(N+L-2));     % Convolve & d-sample
c = conv(c,h0);   c = c(N:2:(N+L-2));     % Convolve & d-sample

g = [c,d];                                % The DWT
