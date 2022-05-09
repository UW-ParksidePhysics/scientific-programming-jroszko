from convert_units import convert_units
from equations_of_state import fit_eos
from fit_curve_array import fit_curve_array
from plot_data_with_fit import plot_data_with_fit
from quadratic_fit import quadratic_fit
from bivariate_statistics import bivariate_statistics
from two_column_text_read import two_column_text_read
import matplotlib.pyplot as plt
from numpy import linspace


def parse_file_name(file_name):
    to_parse = file_name.split(".")
    symbol = to_parse[0]
    structure = to_parse[1]
    acronym = to_parse[2]
    return symbol, structure, acronym


file_name = "Ag.Fm-3m.GGA-PBE.volumes_energies.dat"
symbol, structure, acronym = parse_file_name(file_name)
array = two_column_text_read("Ag.Fm-3m.GGA-PBE.volumes_energies.dat")
statistics = bivariate_statistics(array)
quadratic_coefficients = quadratic_fit(array)
print(quadratic_coefficients)

