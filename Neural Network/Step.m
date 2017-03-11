function ret = Step(per1)

  if per1>95,
    step = .0000000000001;
  elseif per1>90,
    step = .0000000000005;
  elseif per1>85
    step = .000000000001;
  elseif per1>80,
    step = .000000000005;
  elseif per1>75,
    step = .00000000001;
  elseif per1>70,
    step = .00000000005;
  elseif per1>65,
    step = .0000000001;
  elseif per1>55,
    step = .0000000005;
  elseif per1>50,
    step = .000000001;
  elseif per1>45
    step = .000000005;
  elseif per1>40,
    step = .00000001;
  elseif per1>35,
    step = .00000005;
  elseif per1>30,
    step = .0000001;
  elseif per1>25
    step = .0000005;
  elseif per1>20,
    step = .000001;
  elseif per1>15,
    step = .000005;
  elseif per1>10,
    step = .00001;
  elseif per1>7,
    step = .05;
  elseif per1>5,
    step = .1;
  end;
  ret = step;
endfunction;