data  = load('training_data.txt');
Terror = 0;
fid = fopen ("myfile.txt", "w");
for j=1:10,
  dupdata = data;
  l = length(dupdata);
  ninth = int32(l*9/10);
  index=1;
  for i=1:ninth,
    r = int32((l-1)*rand(1,1))+1;
    temp(index,:) = dupdata(r,:);
    dupdata(r,:) = [];
    index=index+1;
    l=l-1;
  end;
  err= GDescentTest(temp,dupdata)
  fputs(fid,"Error ");
  fputs(fid,j);
  fputs(fid," = ");
  fputs(fid,num2str(err));
  fputs(fid,"\n");
  Terror += err;
end;
Errorrate = Terror/10
fputs(fid,"Average error rate = ");
fputs(fid,num2str(Errorrate));
fclose(fid);
