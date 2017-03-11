function ret = Step(er1)
  if er1<.02,
    step = .000004;
  elseif er1<.05,
    step = .000006;
  elseif er1<.1,
    step = .00001;
  elseif er1<.3,
    step = .00002;
  elseif er1<.6
    step = .00035;
  elseif er1<1,
    step = .0001;
  elseif er1<2,
    step = .0005;
  elseif er1<3,
    step = .001;
  else,
    step = .01;
  end;
  ret = step;
endfunction;