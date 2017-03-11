function ret = larg(z)

    largest =0;
    ind = 0;
    for i=1:length(z),
    
        if z(i)>largest,
        
            largest = z(i);
            ind = i;
         endif
     endfor
     ret = ind;
 endfunction