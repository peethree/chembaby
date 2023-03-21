# chembaby

#

automates plotting wavelength by absorption graphs from raw measuring data.

#

#### how to use:

* download chembabyapp.py (six '7-zip' files, to be extracted)
* open the program
* navigate to where you've stored your .txt files that need plotting
* highlight file(s), using ctrl+click in case you want to plot more than 1 file at once
* the program will then output a graph which you can save or edit 


  
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


