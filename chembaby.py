# copyright © 2023 P.B. "peethree" Schellekens
# see bottom for extended copyright information 

import sys
import matplotlib.pyplot as plt

def main():

    # if 1 or more commandline argument(s) is given
    if len(sys.argv) >= 2:      
            try:   
                # unpacks command line argument files into individual arguments which are then passed into the clean_data function           
                data_dict = clean_data(*sys.argv[1:])
                plot_data(data_dict)
            except:
                sys.exit("invalid file or text file doesn't exist")   
    

# this function accepts a variable amount of files. it stores 'files' into a tuple named files
def clean_data(*files):

    # empty dictionary to store lists of 'file data' into
    data_dict = {}

    # loop over file and create an empty list for them
    for file in files:        
        data = []

        # read the file
        with open(file, 'r') as f:
            for line in f:
                wavelength, absorbance = line.split()
                wavelength = float(wavelength.replace(',', '.'))
                absorbance = float(absorbance.replace(',', '.'))
                if wavelength <= 1000:
                    # add the updated parameter of values to the list 
                    data.append((wavelength, absorbance))

        #store each file's data in the dictionary
        data_dict[file] = data
    return data_dict

# add ways to color the graphs
def get_colors():

    colors = ['#FF2EAD', 'teal', 'blue', 'red', 'green', 'black', 'purple', 'orange']    
    return colors     

def plot_data(data_dict):

    # figure and axes
    _, axes = plt.subplots()

    # colors for graph and legend
    colorscheme = get_colors()
    axes.set_prop_cycle(color=colorscheme)
        
    # Loop over each file in the dictionary and extract the x, y values for the graph
    for file, data in data_dict.items(): # file is the key, data is the value
        # produce an iterable of tuples 
        wavelengths, absorbances = zip(*data)
        # get at label name for legend
        _, substance_name = file.split(sep="-")
        substance_name = substance_name.replace(".txt", "")        
        axes.plot(wavelengths, absorbances, label=substance_name)
        

    # we only care about y values ranging from x:300 to 1000
    axes.set_xlim(300, 1000)
    # wavelength in nanometers
    axes.set_xlabel('λ [nm]')
    # absorption in arbitrary units
    axes.set_ylabel('Abs. [a.u]')
    legend = axes.legend(loc='upper right')   
    
    # make legend width thicker   
    for line in legend.get_lines():
        line.set_linewidth(3.0)   
    
    plt.show()


if __name__ == "__main__":
    main()

# Chembaby is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.
