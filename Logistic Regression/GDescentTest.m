function ret = GDescentTest(train,test)
TrX1 = train(:,1);
TeX1 = test(:,1);
TrX2 = train(:,2);
TeX2 = test(:,2);
TrX3 = train(:,3);
TeX3 = test(:,3);
TrX4 = train(:,4);
TeX4 = test(:,4);
TrY1 = train(:,5);
TeY1 = test(:,5);
n = length(TeX1);
H = [ones(length(train), 1),TrX1,TrX2,TrX3,TrX4];
w = [zeros(5,1)];
par = partial(H,TrY1,w);
pw = w;
step=0.01;
w = pw + step*par';
er1 = error(par);
er = 0.01;
while (er1 > er),
  par = partial(H,TrY1,w);
  step = Step(er1);
  pw = w;
  w = pw + step*par';
  er1 = error(par)
end;
Test = [ones(n,1),TeX1,TeX2,TeX3,TeX4];
a=0;
for j=1:length(Test),
  really = TeY1(j,1);
  pred(1,j) = (1/(1+exp(-1*(w'*Test(j,:)'))));
  diff = (really - pred(1,j))*(really - pred(1,j));
  a = a+diff;
end;
ret = sqrt(a/length(Test));
endfunction;






