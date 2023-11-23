# Phonological-Distance-in-Kenyan-Sign-Language



**Technical notes**

This repository contains two Colab notebooks to get the minimal pairs. 

The notebook consists of 7 code cells. Each is called a "block". Each comes with a brief description of its function.  
To use the code, first, upload the data in Colab and change the .csv file in block 1. Make sure that you do not put it in any folder. Then set the optional parameter in block 3 and press Ctrl+F9 or click runtime -> run all to run the entire notebook. The output files will appear in the file tab, right below the input file. The total number of pairs will appear in the output field below the code cell.

The output consists of 2 .csv file. Each consists of the following columns:
- the name of each pair,
- the number of different features
- the list of different features
- the number of similar features
- the list of similar features

The "output_statistic.csv" file stores the data for all of the strings compared. The minimal_pairs.csv file only contains pairs that differ by 1 variable, so-called minimal pairs. 

To generate the pairs that differ by a specific number of variable and in the meantime contains a specific variable, create a new code cell, and copy the code in "block_8.py" into the new cell. Make sure that you run all of the previous blocks before running block 8.  




