%%%% RENAME from mini_project.m to (your_project_short_name).m
% Comments describing mini-project ~ 100-200 words ~

% Tensile Stress Mini-Project - Written
%It is important to address the problem of tensile stress of materials that are used to hang or pull 
%different objects. Objects such as traffic lights, chandeliers, and even hanging baskets for flowers 
%all produce tensile stress on ropes and chains as they are hung from a surface, object, pulley 
%system, etc. The tensile stress of chains/ropes/string is important for manufacturers to know so 
%they can determine the purpose of these materials and how much force these materials can 
%withstand. The main variable to solve for tensile stress is force over the material’s cross-sectional area. The main physical 
%principle of this problem is the force of an object that exerts on a chain or rope, which mainly 
%includes principles such as gravity or friction, depending on if an object is being pulled on the 
%ground or hung in the air. Functions that need to be written have to relate to work (force times 
%displacement) if an object is being pulled on the ground, or the force of gravity (mass times the 
%gravity constant) to calculate the net force on the material that’s pulling an object. As a 
%disclaimer, this project will only be focusing on objects that are being pulled straight horizontally or hung 
%straight vertically to simplify this project. This project will be using vectors to store the values of work as 
%polar coordinates, as well as using arrays to store the values of displacement as an object is being 
%pulled on the ground. As for data, it will be necessary to read into physics textbooks and also use 
%the internet as a free resource to look up how to calculate the cross-sectional area of ropes, 
%chains, strings, etc., and to look up the equation of work involving friction. There is also a great 
%article from Harvey Mudd College that explains the physics behind ropes, strings, and chains 
%(https://www.math.hmc.edu/~dyong/papers/strings.pdf). The results will be visualized by using charts 
%of objects being pulled by chains/ropes and include arrows and other indicators to display the 
%physics behind this problem.

% Simulation parameters
%	These are values particular to the simulation 
%	that do not change later in the script

% materials: cotton, hemp, etc.
youngs_moduli = [2.9*10^9,2.5*10^9];
yield_strengths = [50*10^6,63*10^6];
L = 10
deltaL = linspace(0, maximum_strain)


for index = 1:length(youngs_moduli)
   yield_strength = yield_strengths(index)
   E = youngs_moduli(index)
   maximum_strain = strain(yield_strength,E)
end
pause

maximum_strain = strain(yield_strength,E_polyester)
deltaL = linspace(0, maximum_strain) % elastic strain at failure --> strength/Young's Modulus
L = 10 % meters
epsilon = deltaL ./ L
E = E_polyester
sigma = E .* epsilon
plot(epsilon,sigma)
hold on
% E = young's modulus
% sigma = stress
% epsilon = strain
E_nylon = 2.5*10^9 % Young's modulus for Bulk Nylon
deltaL = (0:linspace(0, 25.2):25.2) % elastic strain at failure --> strength/Young's Modulus
L = 10 % meters
epsilon = deltaL ./ L
E = E_nylon
sigma = stress(epsilon, E)



plot(epsilon,sigma)
hold off


% Computed parameters (from simulation parameters)
%	These are values that do not change later in the script
%	and are calculated from formulas using the simulation parameters


% Function calls and simple calculations for:
%	data read-in
%	simulation solution 
%	visualization

% Function definitions for simulation solution & visualization
%	Each function contains help text: https://www.mathworks.com/help/matlab/matlab_prog/add-help-for-your-program.html

%
%url = 'https://industrialrope.com/catalog-fiber-rope/cordage-comparative-weight-strength-and-working-load-chart/';
%data = webread(url);
%whos data

function stresses = stress(strains, youngs_modulus)
    stresses = youngs_modulus.*strains;
end
function strains = strain(stresses, youngs_modulus)
    strains = stresses./youngs_modulus;
end
