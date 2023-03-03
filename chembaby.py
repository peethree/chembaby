import sys
import matplotlib.pyplot as plt

# ---How to use? "python babychem.py text_file_name.txt"---
# ---Text file needs to be in the same folder as the python program---
# ---Won't work unless it's in this format: "something-substance_name.txt" or "2023_01_31-AgInS2.txt" for example---

if len(sys.argv) == 2:   
    # empty list to add the values to plot to 
    graph_values = []
    
    try:
        # clean up data
        with open(sys.argv[1], 'r') as f_in:
            for line in f_in:
                # split the values at the tab character
                wavelength, absorbance = line.split(sep="\t")

                # replace commas with dots
                wavelength = wavelength.replace(",", ".")
                absorbance = absorbance.replace(",", ".")

                # remove rows with over 1000 nm wavelength    
                if float(wavelength) <= 1000:
                    # append rows that meet the requirement to the graph_values list         
                    line = f"{wavelength},{absorbance}"
                    graph_values.append(line)
    except:
        sys.exit("not a text file or does not exist")

    # iterates over every row of original graph_values list, converts the values to float and makes a new list with said float values
    graph_values = [list(map(float, line.split(sep=","))) for line in graph_values]

    # create new lists for x and y to plot
    x = []
    y = []

    # loop over the rows of data and add values to plot-lists
    for row in graph_values:
        x.append(row[0])
        y.append(row[1])


    # get the substance name by splitting at the "-" 
    _, label = sys.argv[1].split(sep="-")

    # label for legend
    label = label.replace(".txt", "")

    # plot the graph
    plt.plot(x, y, color='teal', label=label)
    plt.xlim(300, 1000)
    plt.xlabel("λ [nm]")
    plt.ylabel("Abs. [a.u]")
    plt.legend(loc='upper right')

    # show the graph
    plt.show()

elif len(sys.argv) == 3:   
    # empty list to add the values to plot to 
    graph_values1 = []
    graph_values2 = []
    
    try:
        # clean up data
        with open(sys.argv[1], 'r') as f_in1:
            for line1 in f_in1:
                # split the values at the tab character
                wavelength1, absorbance1 = line1.split(sep="\t")

                # replace commas with dots
                wavelength1 = wavelength1.replace(",", ".")
                absorbance1 = absorbance1.replace(",", ".")

                # remove rows with over 1000 nm wavelength    
                if float(wavelength1) <= 1000:
                    # append rows that meet the requirement to the graph_values list         
                    line1 = f"{wavelength1},{absorbance1}"
                    graph_values1.append(line1)
    except:
        sys.exit("first argument is not a text file or does not exist")
    try:              
        with open(sys.argv[2], 'r') as f_in2:
            for line2 in f_in2:
                # split the values at the tab character
                wavelength2, absorbance2 = line2.split(sep="\t")

                # replace commas with dots
                wavelength2 = wavelength2.replace(",", ".")
                absorbance2 = absorbance2.replace(",", ".")

                # remove rows with over 1000 nm wavelength    
                if float(wavelength2) <= 1000:
                    # append rows that meet the requirement to the graph_values list         
                    line2 = f"{wavelength2},{absorbance2}"
                    graph_values2.append(line2)
    except:
        sys.exit("second argument is not a text file or does not exist")
    

    # iterates over every row of original graph_values list, converts the values to float and makes a new list with said float values
    graph_values1 = [list(map(float, line1.split(sep=","))) for line1 in graph_values1]
    graph_values2 = [list(map(float, line2.split(sep=","))) for line2 in graph_values2]

    # create new lists for x and y to plot
    x1 = []
    y1 = []
    x2 = []
    y2 = []

    # loop over the rows of data and add values to plot-lists
    for row in graph_values1:
        x1.append(row[0])
        y1.append(row[1])
    
    for row in graph_values2:
        x2.append(row[0])
        y2.append(row[1])


    # get the substance name by splitting at the "-" 
    _a, label1 = sys.argv[1].split(sep="-")
    _b, label2 = sys.argv[2].split(sep="-")

    # label for legend
    label1 = label1.replace(".txt", "")
    label2 = label2.replace(".txt", "")

    # plot the graph
    plt.plot(x1, y1, color='teal', label=label1)
    plt.plot(x2, y2, color='red', label=label2)
    plt.xlim(300, 1000)
    plt.xlabel("λ [nm]")
    plt.ylabel("Abs. [a.u]")
    plt.legend(loc='upper right')    
    plt.show()

elif len(sys.argv) == 4:   
    # empty list to add the values to plot to 
    graph_values1 = []
    graph_values2 = []
    graph_values3 = []
    
    try:
        # clean up data
        with open(sys.argv[1], 'r') as f_in1:
            for line1 in f_in1:
                # split the values at the tab character
                wavelength1, absorbance1 = line1.split(sep="\t")

                # replace commas with dots
                wavelength1 = wavelength1.replace(",", ".")
                absorbance1 = absorbance1.replace(",", ".")

                # remove rows with over 1000 nm wavelength    
                if float(wavelength1) <= 1000:
                    # append rows that meet the requirement to the graph_values list         
                    line1 = f"{wavelength1},{absorbance1}"
                    graph_values1.append(line1)
    except:
        sys.exit("first argument is not a text file or does not exist")
    try:              
        with open(sys.argv[2], 'r') as f_in2:
            for line2 in f_in2:
                # split the values at the tab character
                wavelength2, absorbance2 = line2.split(sep="\t")

                # replace commas with dots
                wavelength2 = wavelength2.replace(",", ".")
                absorbance2 = absorbance2.replace(",", ".")

                # remove rows with over 1000 nm wavelength    
                if float(wavelength2) <= 1000:
                    # append rows that meet the requirement to the graph_values list         
                    line2 = f"{wavelength2},{absorbance2}"
                    graph_values2.append(line2)
    except:
        sys.exit("second argument is not a text file or does not exist")
    
    try:              
        with open(sys.argv[3], 'r') as f_in3:
            for line3 in f_in3:
                # split the values at the tab character
                wavelength3, absorbance3 = line3.split(sep="\t")

                # replace commas with dots
                wavelength3 = wavelength3.replace(",", ".")
                absorbance3 = absorbance3.replace(",", ".")

                # remove rows with over 1000 nm wavelength    
                if float(wavelength3) <= 1000:
                    # append rows that meet the requirement to the graph_values list         
                    line3 = f"{wavelength3},{absorbance3}"
                    graph_values3.append(line3)
    except:
        sys.exit("third argument is not a text file or does not exist")
    

    # iterates over every row of original graph_values list, converts the values to float and makes a new list with said float values
    graph_values1 = [list(map(float, line1.split(sep=","))) for line1 in graph_values1]
    graph_values2 = [list(map(float, line2.split(sep=","))) for line2 in graph_values2]
    graph_values3 = [list(map(float, line3.split(sep=","))) for line3 in graph_values3]

    # create new lists for x and y to plot
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    x3 = []
    y3 = []
    
    # loop over the rows of data and add values to plot-lists
    for row in graph_values1:
        x1.append(row[0])
        y1.append(row[1])
            
    for row in graph_values2:
        x2.append(row[0])
        y2.append(row[1])

    for row in graph_values3:
        x3.append(row[0])
        y3.append(row[1])


    # get the substance name by splitting at the "-" 
    _a, label1 = sys.argv[1].split(sep="-")
    _b, label2 = sys.argv[2].split(sep="-")
    _c, label3 = sys.argv[3].split(sep="-")

    # label for legend
    label1 = label1.replace(".txt", "")
    label2 = label2.replace(".txt", "")
    label3 = label3.replace(".txt", "")

    # plot the graph
    plt.plot(x1, y1, color='teal', label=label1)
    plt.plot(x2, y2, color='red', label=label2)
    plt.plot(x3, y3, color='black', label=label3)
    plt.xlim(300, 1000)
    plt.xlabel("λ [nm]")
    plt.ylabel("Abs. [a.u]")
    plt.legend(loc='upper right')    
    plt.show()
  
    