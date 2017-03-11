function ret = error(par)
  ret = 0;
  for i=1:5,
    ret = abs(par(i));
  end;
  ret = ret/5;
endfunction;
