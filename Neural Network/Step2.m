function ret = Step2(per1)

  switch (per1)
    case 10
      step = .0000000000001;
    case 9
      step = .000000000001;
    case 8
      step = .00000000001;
    case 7
      step = .0000000001;
    case 6
      step = .000000001;
    case 5
      step = .00000001;
    case 4
      step = .0000001;
    case 3
      step = .000001;
    case 2
      step = .00001
    case 1
      step = .0001
    otherwise
      step = .1;
  endswitch
  ret = step;
endfunction;