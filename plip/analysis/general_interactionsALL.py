"""
Quick script to process PLIP interactions summary report generated with general_plip_procesing.py script

Usage: python general_interactionsALL.py

Melchor Sanchez-Martinez, 2022 
"""

import sys, os, glob
import pandas as pd


def Interacts2Csv(intspath):
	files=glob.glob(intspath+'/interactions/interactions_summary/*Interactions_Summary.txt')
	ints=[]
	ints_dict={}
	for f in files:
		with open(f, 'r') as fr:
			lines=fr.readlines()
			for line in lines:
				if 'Interaction_type' not in line:
					if line.split('\t')[0]+'-'+line.split('\t')[1].split('\n')[0] in ints:
						pass
					else:
						ints.append(line.split('\t')[0]+'-'+line.split('\t')[1].split('\n')[0])
						ints_dict[line.split('\t')[0]+'-'+line.split('\t')[1].split('\n')[0]]=0

	with open('./Interactions_Summary_global.csv', 'w') as fw:
		fw.write('Docking_Pose/Compound'+'\t')
		for val in ints_dict:
			fw.write(str(val)+'\t')
		fw.write('\n')
		for f in files:
			with open(f, 'r')as fr:
				lines=fr.readlines()
				for line in lines:
					if 'Interaction_type' not in line:
						ints_dict[line.split('\t')[0]+'-'+line.split('\t')[1].split('\n')[0]]=ints_dict[line.split('\t')[0]+'-'+line.split('\t')[1].split('\n')[0]]+1
				print (f)
				fw.write(f.split('/')[-1].split('_Interactions_Summary.txt')[0]+'\t')
			for times in ints_dict:
				val=ints_dict[times]
				fw.write(str(val)+'\t')
			fw.write('\n')
			for times in ints_dict:
				ints_dict[times]=0

if __name__ == '__main__':
    main()
