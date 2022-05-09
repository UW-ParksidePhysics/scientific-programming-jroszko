"""
Takes in data from two_column_text_read and fit_curve_array from the eq.of state and plots the data.
"""
__author__ = "Jordan Roszko"
import matplotlib.pyplot as plt


def plot_data_with_fit(data, fit_curve, data_format="", fit_format=""):
  """
  Create a combined scatter and curve plot for the data and the fit polynomial, respectively, using Pyplot's plot
  (Links to an external site.) function
  :param data: ndarray, shape(2, M)
  :param fit_curve: ndarray, shape(2, N)
  :param data_format: str, optional
  :param fit_format: str, optional
  :return: combined_plot
  A list of Line2D (Links to an external site.) objects representing the plotted data.
  This is the default return type from Pyplot's plot.
  """
  scatter_plot = plt.plot(data[0, :], data[1, :], data_format)
  curve_plot = plt.plot(fit_curve[0, :], fit_curve[1, :], fit_format)
  plt.title((r'Fm-3m Equation of State for Al in DFT GGA-PBE'), y=1.05)
  plt.xlabel(r'$V$ $A^3/atom$')
  plt.ylabel(r'$E$ $eV/atom$')

  plt.xlim([90, 137])


  plt.show()
  
  #plt.savefig("Initial_plot.png")

  return scatter_plot, curve_plot
