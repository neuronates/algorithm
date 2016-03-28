function [seizureIndex, seizureStart] = epileptogenicity(data)
	
	% assume all traces lie in columns of data
    	
    	fs = 256;                    % sampling frequency
    	duration = 6;                % time duration of the window
    	windowSize = fs*duration;    % window size in samples
    	thresh = 0.3;                % threshold for detection
    	bias = 0.1;                  % positive bias
    	advance = duration * fs;     % the number of samples to shift the window 

	startIndex = 1;
    	endIndex = windowSize;
    
    	thetaLow = 4;
    	thetaHigh = 7;
    	alphaLow = 8;
    	alphaHigh = 12;
    
    	betaLow = 13;
    	betaHigh = 24;
    	gammaLow = 25;
    	gammaHigh = 97;

	ER = [];
	
	while (endIndex <= size(data, 1))
		energySpectrum = fft(data(:,startIndex:endIndex)).*conj(fft(data(:,startIndex:endIndex)));
		energyRatio = sum(energySpectrum(betaLow:gammaHigh)) / sum(energySpectrum(thetaLow:alphaHigh));
		
		ER = [ER, energyRatio];
		endIndex = endIndex + advance;
		startIndex = startIndex + advance;
	end
	
	U_n = [];
	seizureIndex = -1;
	seizureStart = -1;
	
	for i = 1:size(ER)
        
        	U_n = [U_n, ER(i) - mean(ER(1:i)) - bias];
        	[min_val min_ind] = min(U_n);
        	
        	if(U_n(i) - min_val(1) > thresh)
            		seizureIndex = i;
            		seizureStart = min_ind(1);
            	end
            
        end
        
return


    
