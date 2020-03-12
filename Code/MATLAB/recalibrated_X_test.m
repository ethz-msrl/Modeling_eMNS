clc
clear all

addpath ../CalibratedSystem_CardioMag_orginal_files
% this should be path to where the MPEM model parametrization are saved
MODELS_PATH = '../../../Models/MPEM';
addpath(MODELS_PATH);
% this should be path to where the MATLAB data is stored
DATA_PATH = '../../../Data/MPEM';
addpath(DATA_PATH);

load('CardioMag_CalibrationCube_03-04-19.mat')
%load('cmag_05-12-18.mat')
cmag.lastCoilAsOffset = 1;
load('X_test.mat')

fieldStrength = zeros(length(X_test), 8);
for i = 1:length(X_test)
    if rem(i, 200) == 0
        fprintf('%d out of %d samples processed\n',i, length(X_test));
    end
    
    Position = X_test(i,1:3)';
    CurrentVector = X_test(i, 4:11)';
    fieldStrength(i, :) = cmag.FieldAndGradient(Position,CurrentVector)';
end

save(fullfile(DATA_PATH, 'mpem_y_pred.mat'), 'fieldStrength');
    
    
%Position = [0;0;0];
%CurrentVector = [1 1 1 1 1 1 1 1]';
%BG = magSystem.FieldAndGradient(Position,CurrentVector);
