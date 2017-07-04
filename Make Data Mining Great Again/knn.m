% This program calculates the missing values from an "Input" file.
% the program reads from the file that countains three columns of data at a
% time.
% In order for this code to works there should not be any Strings in the
% input file.
% transfer she missing values to a different sheet and and insert the
% number "0" that represent the missing value
% to run it just write "knn" and find the value once at a time. such as the
% following : knn 25 0 87 "enter"



function[missingV] = knn(health, access, stores)
   
    % Read input file
    data = xlsread('PCH');
    s = size(data);
    s = s(1);
    
     % Convert inputs
    health = str2double(health);
    access = str2double(access);
    stores = str2double(stores);
    
    % name of the columns to find the missing value
    if health == 0
        % sort the distances 
        distances = zeros(s,2);
        for i = 1:s
            aVal = data(i,3);
            eVal = data(i,4);
            
         d = sqrt(((access-aVal)*(access-aVal))+((stores-eVal)*(stores-eVal)));
         distances(i,1) = data(i,1);
         distances(i,2) = d;
        end
        % organize the distances and K=3
        distances = sortrows(distances, 2);
        dis1 = distances(1, 2);
        dis2 = distances(2, 2);
        dis3 = distances(3, 2);
        x = (1/dis1) + (1/dis2) + (1/dis3);
        % find the weights of the values
        weight1 = (1/dis1)/x;
        val1 = data(distances(1,1), 2);
        weight2 = (1/dis2)/x;
        val2 = data(distances(2,1), 2);
        weight3 = (1/dis3)/x;
        val3 = data(distances(3,1), 2);
        
        missingV = (weight1*val1)+(weight2*val2)+(weight3*val3);
    end
    
   
    if access == 0
   
        distances = zeros(s,2);
        for i = 1:s
            tVal = data(i,2);
            eVal = data(i,4);
       
            d = sqrt(((health-tVal)*(health-tVal))+((stores-eVal)*(stores-eVal)));
            distances(i,1) = data(i,1);
            distances(i,2) = d;
        end
       
        distances = sortrows(distances, 2);
        dis1 = distances(1, 2);
        dis2 = distances(2, 2);
        dis3 = distances(3, 2);
       
        x = (1/dis1) + (1/dis2) + (1/dis3);
    
        weight1 = (1/dis1)/x;
        val1 = data(distances(1,1), 3);
        weight2 = (1/dis2)/x;
        val2 = data(distances(2,1), 3);
        weight3 = (1/dis3)/x;
        val3 = data(distances(3,1), 3);
        
        missingV = (weight1*val1)+(weight2*val2)+(weight3*val3);
    end
    
    
    if stores == 0
        
        distances = zeros(s,2);
        for i = 1:s
            tVal = data(i,2);
            aVal = data(i,4);
            
            d = sqrt(((health-tVal)*(helth-tVal))+((access-aVal)*(access-aVal)));
            distances(i,1) = data(i,1);
            distances(i,2) = d;
        end
      
        distances = sortrows(distances, 2);
        dis1 = distances(1, 2);
        dis2 = distances(2, 2);
        dis3 = distances(3, 2);
       
        x = (1/dis1) + (1/dis2) + (1/dis3);
       
        weight1 = (1/dis1)/x;
        val1 = data(distances(1,1), 4);
        weight2 = (1/dis2)/x;
        val2 = data(distances(2,1), 4);
        weight3 = (1/dis3)/x;
        val3 = data(distances(3,1), 4);
        
        missingV = (weight1*val1)+(weight2*val2)+(weight3*val3);
    end
end

