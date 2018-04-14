%process the input files
genfile='GeneratorDispatch.csv';
[num,txt,~]=sheetread(genfile);

ldfile2='LoadBusB2.csv';
[ld2,~,~]=sheetread(ldfile2);

ldfile3='LoadBusB3.csv';
[ld3,~,~]=sheetread(ldfile3);

ldfile4='LoadBusB4.csv';
[ld4,~,~]=sheetread(ldfile4);

ts=timeSeries2;

gentime=0:300:86000;
gentime(1)=gentime(1)+1;
ts.addData(gentime',num(2:end,2:end));
ts.fields={'ALTA',	'PARKCITY',	'SOLITUDE',	'SUNDANCE',	'BRIGHTON'};

ts.writeBinaryFile('genData.dat');
ldtime=0:6:86395;
ldtime(1)=ldtime(1)+1;

tsld=timeSeries2;

tsld.addData(ldtime',ld2(:,2),1);
tsld.addColumn(ld3(:,2),2);
tsld.addColumn(ld4(:,2),3);
tsld.writeBinaryFile('loadData.dat');