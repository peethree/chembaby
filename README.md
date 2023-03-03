# chembaby

#

automates plotting highly specific graphs from raw data.

#

#### how to use:

1. download chembaby
2. install the requirements from requirements.txt by writing the following in the terminal window: 'pip install -r requirements.txt'
3. name the data.txt files as follows: <something>-<label name for the graph>.txt, so for example "31_12_2023-NaBiS 1ml OA.txt" -- note that when using a space character in naming the text file, you have to use quotation marks around the filename to not mess up the argument values.
4. place the text files in the same folder as the chembaby app
5. run 'python chembaby.py "file.txt"', and optionally up to 2 more .txt files, seperated by a space
6. the program will then show a graph of the wavelength values, starting at 300 nm, up to 1000nm and the absorbtion values in arbitrary units.
  
#

admittedly a very ugly heuristic approach.
