% Tensile Stress Mini-Project

% --------------------------------------------------------------------------------------------------
% The main goal of this project is to write a program that takes properties
% (yield strength, Young's modulus, length, strain/stress) of different
% types of rope (polyester, nylon, etc.) from any data set and calculate the maximum stress and strain of
% a specific type of rope. It will then produce a graph that compares the
% the stress vs. strain of the rope (this will be the visualization).
% --------------------------------------------------------------------------------------------------

% materials: cotton, hemp, nylon etc.
% This is defining the variables that is going to be going into the for
% loop.
% L is the length, given an arbitrary value of 10 meters.
rope_table_properties = readtable('rope_properties');
rope_types = table2array(rope_table_properties(:,1));
youngs_moduli = table2array(rope_table_properties(:,2));
yield_strengths = table2array(rope_table_properties(:,4));
L = 10;


% Hooke's Law shows the comparison between stress and strain with the
% following formula:
% stress = (Young's modulus) * (strain)
% Strain can be simply calculated by taking stress over Young's modulus.
% This will be the basic formula used in this program.

for index = 1:length(youngs_moduli)
   yield_strength = yield_strengths(index)
   E = youngs_moduli(index)
   maximum_strain = strain(yield_strength,E)
   deltaL = linspace(0, maximum_strain)
   strains = deltaL ./ L
   stresses = E .* strains
   plot(strains,stresses)
   hold on
end
xlabel('Strain')
ylabel('Stress (Pa)')
legend show
legend('Cotton', 'Hemp', 'Bulk Polyester', 'Bulk Nylon', 'Carbon Fibre', 'Aramid Fibre', 'Polyester Fibre', 'Nylon Fibre', 'Alloy Steel')
hold off

% This is the plot that compares stress vs. strain. Each line that is
% plotted in the graph is labeled in a legend with its own rope material
% (cotton, hemp, etc.)


% These two functions will be used to calculate the stress & strain from a
% given array of data.
function stresses = stress(strains, youngs_modulus)
    stresses = youngs_modulus.*strains;
end
function strains = strain(stresses, youngs_modulus)
    strains = stresses./youngs_modulus;
end
