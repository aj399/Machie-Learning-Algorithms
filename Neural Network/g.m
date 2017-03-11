function ret = g(z)

    for i=1:length(z),
    
        ret(i) = 1/(1+exp(-1*z(i)));
    end;
endfunction