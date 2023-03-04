import sys
import matplotlib.pyplot as plt

def main():

    # if 1 or more commandline argument(s) is given
    if len(sys.argv) >= 2:      
            try:   
                # unpacks list into individual arguments which are then passed into the clean_data function           
                data_dict = clean_data(*sys.argv[1:])
                plot_data(data_dict)
            except:
                sys.exit("invalid file or text file doesn't exist")   
    

# accepts variable amount of files, stores 'files' into tuple named files
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
        

def plot_data(data_dict):

    # figure and axes
    _, ax = plt.subplots()
        
    # Loop over each file in the dictionary and extract the x, y values for the graph
    for file, data in data_dict.items():
        # produce an iterable of tuples 
        wavelengths, absorbances = zip(*data)
        # get at name for legend
        _, substance_name = file.split(sep="-")
        substance_name = substance_name.replace(".txt", "")        
        ax.plot(wavelengths, absorbances, label=substance_name)

    # we only care about y values ranging from x:300 to 1000
    ax.set_xlim(300, 1000)
    # wavelength in nanometers
    ax.set_xlabel('λ [nm]')
    # absorption in arbitrary units
    ax.set_ylabel('Abs. [a.u]')
    ax.legend(loc='upper right')         
    
    plt.show()


if __name__ == "__main__":
    main()
