# Phonological-Distance-in-Sign-Languages

**Overview**

This repository contains Python code used in a project to compare discrete phonological forms between signs—specifically, how many categorical differences there are between signs in a lexicon. This project is based on a linguistic analysis of sign language, informed by three theoretical models of sign phonology: the Dependency Model (van der Kooij 2002; van der Hulst 1993), the Prosodic Model (Brentari 1998), and a synthesis of the two (Morgan 2022). 

The Python code is one of four components in a larger project. The four components are listed here with their location in parentheses:
1. Phonological features of signs coded in a lexical database and output as a .csv file (dataset not publicly available)
2. String structure of phonological feature types and feature values related to each type (OSF project: ## not set up yet ## )
3. Conditionalities for comparing each feature type between pairs of signs (listed in Morgan ##in prep##)
4. Python script that operationalizes all three components above (this GitHub repository)

**Phonological distance**

The degree of phonological similarity between spoken words is typically measured using a Levenstein distance calculation applied to words written in an alphabetic orthography or words transcribed in a sound-based encoding, such as the International Phonetic Alphabet. Words—i.e., *signs*—in sign languages pose a number challenges for tracking phonological similarities and differences as is done in spoken languages. In spoken languages, phonological units, segments, are written as strings of sounds that crucially appear in a specific order. In contrast, the sub-parts of signs are highly simultaneous, and a single sign can contain several dozen phonological features within the main phonological parameters of handshape, location, movement, etc. Large-scale phonological comparisons between signs have improved over time, but even recent large-scale analyses have not taken the full range of  phonological content into account; for example, Yu et al. (2018); Caselli et al. (2021); Martinez del Rio et al. (2022). The current measurement of phonological distance in this Python script uses a larger set of categorical differences and uses custom conditionalities that target only the contrastable parts of signs.
 
**Technical notes**

*Description*

This repository contains two Colab notebooks for determining phonological distance. The `phonological_distance` notebook applies conditionalities and can be used to extract minimal pairs. The `phonologial_distance_without_conditionalities` notebook will measure similarities and differences betweeen pairs of signs and generate minimal pairs without considering the conditionalities.

The `phonological_distance` notebook consists of 7 code cells. Each is called a "block". Each comes with a brief description of its function in a text cell. The `phonologial_distance_without_conditionalities` notebook has 5 code cells.

The output of both notebook consists of 2 `.csv` files. Each consists of the following columns:
- the name of each pair
- the total number of different features
- the list of different features
- the number of similar features
- the list of similar features

The `output_statistic.csv` file stores the data for all of the strings compared. The `minimal_pairs.csv` file only contains pairs that differ by 1 variable, so-called minimal pairs. 

*Instruction*

To use the code, open the notebook and click on the `Files` tab (folder icon). Upload the data as a `.csv` file in Colab.  Make sure that you do not put the .csv file in a specific folder. Next, change the .csv file name in `block 1`. Then set the optional parameters in block 3 and press `Ctrl+F9` or click `runtime` -> `run all` to run the entire notebook. The output files will appear in the Files tab, right below the input file. The total number of pairs will appear in the output field below the code cell. If you want to run the notebook locally, replace the file name with the full path to the file.  

To generate the pairs that differ by a specific feature (variable) and also differ by a certain number of features (variables), create a new code cell, and copy the code in `block_8.py` into the new cell. Modify the optional parameters to suit your search. Make sure that you run all of the previous blocks before running block 8.  

**References**

1. Brentari, Diane. 1998. *A prosodic model of sign language phonology*. Cambridge, MA: MIT Press.
2. Caselli, Naomi K., Karen Emmorey, & Ariel M. Cohen-Goldberg. 2021. The signed mental lexicon: Effects of phonological neighborhood density, iconicity, and childhood language experience. *Journal of Memory and Language 121*: 104282. https://doi.org/10.1016/j.jml.2021.104282
3. Hulst, Harry van der. 1993. Units in the analysis of signs. *Phonology 10*(2). 209–241. [doi:10.1017/S095267570000004X](https://doi.org/10.1017/S095267570000004X)
4. Kooij, Els van der. 2002. *Phonological categories in Sign Language of the Netherlands: The role of phonetic implementation and iconicity*. Leiden, Netherlands: Leiden University dissertation. [LOT publications](https://www.lotpublications.nl/phonological-categories-in-sign-language-of-the-netherlands-phonological-categories-in-sign-language-of-the-netherlands-the-role-of-phonetic-implementation-and-iconicity)
5. Martinez del Rio, A., Ferrara, C., Kim, S. J., Hakgüder, E., & Brentari, D. 2022. Identifying the Correlations Between the Semantics and the Phonology of American Sign Language and British Sign Language: A Vector Space Approach. *Frontiers in Psychology 13*. https://doi.org/10.3389/fpsyg.2022.806471
6. Morgan, Hope E. 2022. *A Phonological Grammar of Kenyan Sign Language*, Berlin, Boston: De Gruyter Mouton. [doi.org/10.1515/9783110765694](https://doi.org/10.1515/9783110765694)
7. Morgan, Hope E. *Manuscript in prep*. Closing the loop: Developing a measure of phonological distance in sign languages using a dataset of minimal pairs.
8. Shi Yu, Carlo Geraci, Natasha Abner. 2018. Sign Languages and the Online World Online Dictionaries & Lexicostatistics. *LREC Proceedings* (Proceedings of the Eleventh International Conference on Language Resources and Evaluation), May 2018, Miyazaki, Japan. ijn_03082152  https://hal.science/ijn_03082152

 **Acknowledgements**

Funding for this project from (1) the Centre for Language Studies at Radboud University, the Netherlands; and (2) NWO VICI grant, *Deaf Communication without a Shared Language* (2017-2023), Principal Investigator: Onno Crasborn.
 
 **Authors**

- Dang Thi Thao Anh, Radboud University, thithaoanh.dangthithaoanh at ru.nl
- Hope E. Morgan, Radboud University, hope.morgan at ru.nl




