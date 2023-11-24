# Phonological-Distance-in-Sign-Languages

**Overview**

 Hope: add motivation and overall goals of project 
 Hope: add overview of components and where they are located

**Phonological distance**

 Hope: add the theoretical part here
 
**Technical notes**

This repository contains two Colab notebooks for determining phonological distance. The "phonological_distance" notebook applies conditionalities and can be used to extract minimal pairs. The "phonologial_distance_without_conditionalities" notebook will measure similarities and differences betweeen pairs of signs and generate minimal pairs without considering the conditionalities.

The "phonological_distance" notebook consists of 7 code cells. Each is called a "block". Each comes with a brief description of its function in a text cell.  
To use the code, open the notebook and click on the Files tab (folder icon). Upload the data as a .csv file in Colab.  Make sure that you do not put the .csv file in a specific folder. Next, change the .csv file name in block 1. Then set the optional parameters in block 3 and press Ctrl+F9 or click runtime -> run all to run the entire notebook. The output files will appear in the Files tab, right below the input file. The total number of pairs will appear in the output field below the code cell. If you want to run the notebook locally, replace the file name with the full path to the file.  

The output consists of 2 .csv files. Each consists of the following columns:
- the name of each pair
- the total number of different features
- the list of different features
- the number of similar features
- the list of similar features

The "output_statistic.csv" file stores the data for all of the strings compared. The "minimal_pairs.csv" file only contains pairs that differ by 1 variable, so-called minimal pairs. 

To generate the pairs that differ by a specific feature (variable) and also differ by a certain number of features (variables), create a new code cell, and copy the code in "block_8.py" into the new cell. Modify the optional parameters to suit your search. Make sure that you run all of the previous blocks before running block 8.  

**References**

 Hope: Add references

 **Acknowledgements**

 Hope: add project info for Onno's VICI here ; also: my CO-FUND project
 
 **Authors**

 Hope: add motiva

 **Copyright**

 What copyright to use?



