#!/opt/miniconda3/bin/python3


import re
import argparse
import pandas as pd



#read GTEX data - create dataframe with rows defining only the 1500 genes we care about, and columns defining only the liver GTEX samples


# calculate ave TPM for each transcript across all liver samples, then hash these keys by transcript name (gtex expression hash)


#read Gnomad4 data - create dictonary :gene[transcrpt]='plof value'

#iterate through Gnomaddata hash by gene
	#foreach transcript  ave TPM from GTEX expression hash
	#count number of transcript entries for a gene ( a running count whenever a GTEX transcript is in the Genomedata
	
	



