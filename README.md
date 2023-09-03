# chembaby

#

automates plotting 'wavelength by absorption' graphs from raw measuring data. 

The python script takes all arguments after the first one that are passed into the program and tries to pass them through a series of functions to clean the data so it can be used for plotting a graph -- containing potentially multiple data sets -- generated with 'matplotlib.pyplot'.

The problem to solve here was that the UV/vis spectrometer - the machine used by the person I wrote the script for - outputs data seperating numbers with commas and for plotting it, we want to replace the commas with dots. 'Origin labs' can be used to do this, but on an older version of that software, it would fail to replace a comma several times, leading to a spiky looking and generally faulty graph and having to go through the data again and manually replace the commas with dots. I figured this would be simple to fix with some python code.
The client is doing novel research and is making slight variations to the material between measurements and wants to be able to see the differences in one graph. So for this particular experiment, she added different amounts of oleic acid. 1, 2 and 3 ml of OA respectively. This would then be three .txt files output by the spectrometer. Each of these files containing 1200 lines of measurement data. Every line a representation of the wavelength (x-value), followed then by the correlating absorption value (y-value). The client is only interested in seeing the range of 300 to 1000 nanometers, since that is what supposedly works best for the material.

Initially, I made a brute force approach to the problem which checked the amount of command line arguments and depending on how many were given, would run through an altered version of the single-data-set code to accomodate for more graphs needing to be drawn. This was 246 lines of code (including empty lines and comments) and was hard-coded to only work for three inputs at maximum. I then looked into ways to improve the program. Replace repetetive code with functions and allow for a variable amount of input. This cut the code down significantly and allowed for more data sets to be plotted together. I then added functionality that would take part of the name of the input and use that for the graph legend, so the process of using the program would be: select files, run the program, display informative graph. Note: in the example graph listed below the files were not yet according to the convention I implemented. Lastly, I turned my script into an executable program with PyQt5.

#
##### sample data
![sampledata](https://i.imgur.com/vhHaqKq.png)
#

#### how to use:

* download the six '7-zip' files in the 'chembaby app' folder (the source code of the app is also in this folder, but does not need to be downloaded)
* extract the files by right clicking the first archive file (001), followed by selecting "Open archive". Then select all 6 files and extract.
* open the program
* navigate to where you've stored your .txt files that need plotting
* select file(s), use ctrl+click in case you want to plot more than 1 file at once
* the program will then output a graph which you can save and edit.


  
#### ALTERNATIVELY:
  
1. download chembaby.py and requirements.txt
2. open the program in an IDE such as VSCode
3. install the requirements from requirements.txt by writing the following in the terminal window: 'pip install -r requirements.txt'
4. name the data.txt files as follows: <something>-<label name for the graph>.txt, so for example "31_12_2023-NaBiS 1ml OA.txt" -- note that when using a space character in naming the text file, you have to use quotation marks around the filename to not mess up the argument values.
5. place the text files in the same folder as the chembaby.py app so that the ide can read them
6. run 'python chembaby.py "file.txt"', and optionally more.
7. the program will then show a graph of the wavelength values, starting at 300 nm, up to 1000nm and the absorption values in arbitrary units.




  
#  
  ![interfaceexample](https://i.imgur.com/f8V8nMy.png)  
#  
  ![graphexample](https://i.imgur.com/dNOujGX.png)
#

To clarify: the way legend naming works, is by splitting the name of the text file passed into the program. It takes whatever is **AFTER** a **single** hyphen, "-". 
In the case of "31_12_2023-NaBiS 1ml OA.txt",  "NaBis 1ml OA" would be the outcome and shown in the legend

