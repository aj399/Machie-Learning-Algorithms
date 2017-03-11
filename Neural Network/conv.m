function ret = conv(y)

    for i=1:10,
    
        if y==i,
        
            ret(i) = 1;
        else,
        
            ret(i) = 0;
        endif;
    endfor;
endfunction;