function [itrfin] = apsvm( test )
load appleds

x=feat_ds(1:400,:);
y=species(1:400);


rand_num=randperm(400);

x_train=x(rand_num(1:end),:);
y_train=y(rand_num(1:end),:);
x_test= test;
% x_test=x(rand_num(375:end),:);
% y_test=y(rand_num(375:end),:);

X = x_train;
Y = categorical(y_train);
tabulate(Y)
n = numel(Y);
K = numel(unique(Y));
t = templateEnsemble('GentleBoost',50,'Tree');
rng(1); % For reproducibility
Coding = designecoc(K,'ternarycomplete');
delete(gcp('nocreate'));
pool = parpool;                      % Invokes workers
options = statset('UseParallel',1);
CVMdl = fitcecoc(X,Y,'Learner',t,'Options',options,'Coding',Coding,...
    'FitPosterior',1,'Holdout',0.05);

CMdl = CVMdl.Trained{1};           % Extract trained, compact classifier
%testInds = test(CVMdl.Partition);  % Extract the test indices
%XTest = X(testInds,:);
%YTest = Y(testInds,:);
[label,~,~,posterior] = predict(CMdl,x_test,'Options',options);
% idx = randsample(25,25);
% table(y_test(idx),label(idx),posterior(idx,1),...
%     'VariableNames',{'TestSampleIndex','TrueLabel','PosteriorNoArrhythmia'})
b=table(label(1));
itrfin=table2cell(b);


end