X = load('training_x.txt');
Y = load('training_y.txt');
fid = fopen ("myfile.txt", "w");
fid1 = fopen ("output.txt", "w");
Cost = 2.0;
Delta1 = zeros(25,401);
Delta2 = zeros(10,26);
epsilon = 0.12;
Theta1 = rand(25,401)*2*epsilon - epsilon;
Theta2 = rand(10,26)*2*epsilon - epsilon;
Per = 90
per = 1.0;
while per<Per,

    Cost = 0;
    Cost1 = 0;
    Cost2 = 0;
    tot = 0;
    for i=1:5000,
      
        a1 = horzcat(1,X(i,:));
        #a1 = a1'
        z2 = a1*(Theta1)';
        a2 = horzcat(1,g(z2));
        #a2 = a2'
        z3 = a2*(Theta2)';
        a3 = g(z3);
        ta3 = conv(Y(i));
        pred = larg(a3);
        if pred == Y(i),
        
            tot = tot+1;
        endif; 
        gamma3 = a3-ta3;
        gamma3 = gamma3';
        gamma2 = (Theta2)'*gamma3*(g1(z2));
        gamma2 = gamma2(2:length(gamma2),:);
        Delta2 = Delta2+gamma3*(a2);
        Delta1 = Delta1+gamma2*(a1);
        for k=1:10,
        
            Cost1 = Cost1 + ((-1*ta3(k)*log(a3(k)))-((1-ta3(k))*log(1-(a3(k)))));
        endfor;
    endfor;
    per = (tot/5000)*100
    printf(num2str(per));
    Cost1 = Cost1/5000;
    fputs(fid,"Cost1 = ");
    fputs(fid,num2str(Cost1));
    fputs(fid,"\n");
    for i =1:25,
    
        for j =1:401,
        
            Cost2 = Cost2 + Theta1(i,j)*Theta1(i,j);
        endfor;
    endfor;
    for i =1:10,
    
        for j =1:26,
        
            Cost2 = Cost2 + Theta2(i,j)*Theta2(i,j);
        endfor;
    endfor;
    Cost2 = Cost2/(2*5000)
    fputs(fid,"Cost2 = ");
    fputs(fid,num2str(Cost2));
    fputs(fid,"\n");
    Cost = Cost1+Cost2
    for i =1:25,
    
        dTheta1(i,1) = (1/5000)*Delta1(i,1);
        for j =2:401,
        
            dTheta1(i,j) = (1/5000)*Delta1(i,j) + (1/5000)*Theta1(i,j);
        endfor;
    endfor;
    for i =1:10,
    
        dTheta2(i,1) = (1/5000)*Delta2(i,1);
        for j =2:26,
        
            dTheta2(i,j) = (1/5000)*Delta2(i,j) + (1/5000)*Theta2(i,j);
        endfor;
    endfor;
    for i =1:25,
    
        for j =1:401,
        
            Theta1(i,j) = Theta1(i,j) - Step(per)*dTheta1(i,j);
        endfor;
    endfor;
    for i =1:10,
    
        for j =1:26,
        
            Theta2(i,j) = Theta2(i,j) - Step(per)*dTheta2(i,j);
        endfor;
    endfor;
    fputs(fid,"Cost = ");
    fputs(fid,num2str(Cost));
    fputs(fid,"\n");
    fputs(fid,"Per = ");
    fputs(fid,num2str(per));
    fputs(fid,"\n");
    #printf(num2str(Cost));
endwhile;
fputs(fid1,"Cost = ");
fputs(fid1,num2str(Cost));
fputs(fid1,"\n");
fputs(fid1,"Per = ");
fputs(fid1,num2str(per));
fputs(fid1,"\n");      