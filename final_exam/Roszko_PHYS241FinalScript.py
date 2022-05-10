import numpy as np

from convert_units import convert_units
from equations_of_state import fit_eos
from fit_curve_array import fit_curve_array
from plot_data_with_fit import plot_data_with_fit
from quadratic_fit import quadratic_fit
from bivariate_statistics import bivariate_statistics
from two_column_text_read import two_column_text_read
import matplotlib.pyplot as plt
from numpy import linspace

display_graph = True


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

min_x = statistics[2]
max_x = statistics[3]


fit_eos_curve, fit_parameters = fit_eos(array[0], array[1], quadratic_coefficients, eos='vinet',
                                        number_of_points=50)
bulk_modulus = fit_parameters[1]
equilibrium_volume = fit_parameters[3]


def annotate_graph(axes, symbol, structure, bulk_modulus, equilibrium_volume, data_extremes):
    # from matplotlib.ticker import ScalarFormatter

    # bulk_modulus_gpa = convert_units(bulk_modulus, "rydberg/cubic bohr")
    bulk_modulus_gpa = bulk_modulus

    x_range = data_extremes[1] - data_extremes[0]
    y_range = data_extremes[3] - data_extremes[2]
    x_min = data_extremes[0] - x_range * 0.10
    x_max = data_extremes[1] + x_range * 0.10
    y_min = data_extremes[2] - y_range * 0.10
    y_max = data_extremes[3] + y_range * 0.10



    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    # y_formatter = ScalarFormatter(useOffset=False)
    # axes.yaxis.set_major_formatter(y_formatter)

    axes.annotate(symbol, xy=(x_min+0.03*x_range, y_max-0.05*y_range))

    axes.annotate(r'$ {}\overline{{{}}} {}$'.format(structure[0:2],
                                                    structure[3],
                                                    structure[1]),
                  xy=(115, 0))

    axes.annotate(r'$K_0$={:.2f} GPa'.format(bulk_modulus_gpa),
                  xy=(0.5*x_range+x_min, 0.5*y_range+y_min))

    axes.annotate(r'$V_0$={:.3f}Å$^3$/atom'.format(equilibrium_volume),
                  xy=(115, -0.001))

    graph_y_range = y_max - y_min
    vertical_line_y_max = 1.3*(data_extremes[2] - y_min) / graph_y_range
    plt.axvline(x=equilibrium_volume, ymax=vertical_line_y_max, color="black", linestyle='--')

    plt.text(91, -0.0025, "Created by Jordan Roszko 2022-05-09")
    plt.title("{} Equation of State for {} in DFT {}".format('Vinet', symbol, acronym))
    plt.xlabel(r'$V$ (Å$^3$/atom)')
    plt.ylabel(r'$E$ (eV/atom)')
    return axes


fig = plt.figure()
ax = fig.add_subplot(111)
#
#
# volumes = linspace(min_x, max_x, len(fit_eos_curve))
# line1, = ax.plot(array_2[0], array_2[1], 'o')
# line2, = ax.plot(volumes, fit_eos_curve, color="black")
#


annotate_graph(ax, symbol, structure, bulk_modulus, equilibrium_volume, statistics[2:])

fit_curve = fit_curve_array(quadratic_coefficients, min_x, max_x, number_of_points=100)
plot_data_with_fit(ax, array, fit_curve, data_format="bo", fit_format="k")
# fig.tight_layout()
if display_graph:
    plt.show()
elif not display_graph:
    plt.savefig("")
