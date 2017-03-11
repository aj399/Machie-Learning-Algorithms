function ret = partial(H,y,w)
 # len=length(y)
  for i=1:5,
    ret(i) = 0;
    for j=1:length(H),
      ret(i) = ret(i) + (H(j,i)*(y(j)-(1/(1+exp(-1*w'*H(j,:)')))));
    end;
  end;
endfunction;
