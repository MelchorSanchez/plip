"""
Quick and dirty script to process PLIP interactions report files in txt 
format

A folder called interactions should contain interactions reports that should be
named as NAME_report.txt

Usage: python general_plip_pricessing.py

Melchor Sanchez-Martinez, 2022 
"""
import sys,os
sys.path.append ( os.path.join ("/home/melchor/science/code/" ) )
import glob
import pandas as pd
import shutil
from dock.general_interactionsALL import Interacts2Csv




def createPath(path):
    if not os.path.isdir(path):
        os.mkdir(path)

def moveFiles(filesTomove, destination):
	files_to_move=glob.glob(filesTomove)
	for f in files_to_move:
		shutil.move(f, destination)

files=glob.glob('interactions/*report.txt')
to_exclude=['MG2+', 'NA+', 'SO4', 'GOL', 'ZN2+', 'FE3+','FE2+']
for f in files:
	if os.path.isfile('interactions/'+f.split('/')[-1].split('_report.txt')[0]+'_clean_interactions.txt') != True:
		with open(f, 'r') as fr:
			lines=fr.readlines()
			count=0
			start=0
			for line in lines:
				count=count+1
				ligID='None'
				if 'SMALLMOLECULE' in line:
					ligID=line.split(':')[0]
					start=count-1
				print(f.split('/')[-1].split('_report.txt')[0]+'_clean_interactions.txt')
				if ligID != 'None' and ligID not in to_exclude:
					with open('interactions/'+f.split('/')[-1].split('_report.txt')[0]+'.'+ligID+'_clean_interactions.txt', 'w')as fw:
						#fw.write(lines[start])
						for i  in range(start+5, len(lines)):
							if '**Hydrophobic Interactions**' in lines[i]:
								hydro=i
								for j in range(hydro, len(lines)):
									if '|' in lines[j] and not 'SMALLMOLECULE' in lines[j] :
										if 'RESNR' in lines[j-2]:
											fw.write(lines[j-2])
										fw.write('HI '+lines[j])
									if '**Hydrogen Bonds**' in lines[j]:
										break
									if '**pi-Stacking**' in lines[j]:
										break
									if '**pi-Cation Interactions**' in lines[j]:
										break
									if '**Salt Bridges**' in lines[j]:
										break
									if '**Halogen Bonds**' in lines[j]:
										break
							if '**Hydrogen Bonds**' in lines[i]:
								hbonds=i
								for j in range(hbonds, len(lines)):
									if '|' in lines[j] and not 'SMALLMOLECULE' in lines[j] :
										if 'RESNR' in lines[j-2]:
											fw.write(lines[j-2])
										fw.write('HB '+lines[j])
									if '**pi-Stacking**' in lines[j]:
										break
									if '**pi-Cation Interactions**' in lines[j]:
										break
									if '**Salt Bridges**' in lines[j]:
										break
									if '**Hydrophobic Interaction**' in lines[j]:
										break
									if '**Halogen Bonds**' in lines[j]:
										break
							if '**Salt Bridges**' in lines[i]:
								sbridge=i
								for j in range(sbridge, len(lines)):
									if '|' in lines[j] and not 'SMALLMOLECULE' in lines[j] :
										if 'RESNR' in lines[j-2]:
											fw.write(lines[j-2])
										fw.write('SB '+lines[j])
									if '**Hydrogen Bonds**' in lines[j]:
										break
									if '**pi-Stacking**' in lines[j]:
										break
									if '**pi-Cation Interactions**' in lines[j]:
										break
									if '**Hydrophobic Interactions**' in lines[j]:
										break
									if '**Halogen Bonds**' in lines[j]:
										break
							if '**pi-Stacking**' in lines[i]:
								pistack=i
								for j in range(pistack, len(lines)):
									if '|' in lines[j] and not 'SMALLMOLECULE' in lines[j] :
										if 'RESNR' in lines[j-2]:
											fw.write(lines[j-2])
										fw.write('PS '+lines[j])
									if '**pi-Cation Interactions**' in lines[j]:
										break
									if '**Salt Bridges**' in lines[j]:
										break
									if '**Hydrogen Bonds**' in lines[j]:
										break
									if '**Hydrophobic Interaction**' in lines[j]:
										break
									if '**Halogen Bonds**' in lines[j]:
										break
							if '**pi-Cation Interactions**' in lines[i]:
								pication=i
								for j in range(pication, len(lines)):
									if '|' in lines[j] and not 'SMALLMOLECULE' in lines[j] :
										if 'RESNR' in lines[j-2]:
											fw.write(lines[j-2])
										fw.write('PC '+lines[j])
									if '**Salt Bridges**' in lines[j]:
										break
									if '**Hydrogen Bonds**' in lines[j]:
										break
									if '**pi-Stacking**' in lines[j]:
										break
									if '**Hydrophobic Interactions**' in lines[j]:
										break
									if '**Halogen Bonds**' in lines[j]:
										break
							if '**Halogen Bonds**' in lines[i]:
								halogen=i
								for j in range(halogen, len(lines)):
									if '|' in lines[j] and not 'SMALLMOLECULE' in lines[j] :
										if 'RESNR' in lines[j-2]:
											fw.write(lines[j-2])
										fw.write('HalB '+lines[j])
									if '**Salt Bridges**' in lines[j]:
										break
									if '**Hydrogen Bonds**' in lines[j]:
										break
									if '**pi-Stacking**' in lines[j]:
										break
									if '**Hydrophobic Interactions**' in lines[j]:
										break
									if '**pi-Cation Interactions**' in lines[j]:
										break
							else:
								print(f'Not interactions for : {ligID}')
								
files=glob.glob('./interactions/*clean_interactions.txt')
for f in files:
	print (f)
	with open(f, 'r') as fr:
		if os.path.isfile('interactions/'+f.split('/')[-1].split('_clean_interactions.txt')[0]+'_Interactions_Summary.txt') == True:
			print (os.path.isfile(f.split('/')[-1].split('_report.txt')[0]+'_clean_interactions.txt'))
			pass
		if os.path.isfile('interactions/'+f.split('/')[-1].split('_clean_interactions.txt')[0]+'_Interactions_Summary.txt') != True:
			with open('interactions/'+f.split('/')[-1].split('_clean_interactions.txt')[0]+'_Interactions_Summary.txt', 'w') as fw:
				print('interactions/'+f.split('/')[-1].split('_clean_interactions.txt')[0]+'_Interactions_Summary.txt', 'w')
				fw.write('Interaction_type'+'\t'+'Interacting residue'+'\n')
				lines=fr.readlines()
				for i in range(len(lines)):
					if ' | ' in lines[i] and 'RESTYPERESNR.RESCHAIN' not in lines[i] and 'RESNR' not in lines[i]:
						print (lines[i])
						fw.write(lines[i].split(' | ')[0]+'\t'+lines[i].split(' | ')[2].split(' ')[0]+lines[i].split(' | ')[1].split(' ')[0]+'.'+lines[i].split(' | ')[3].split(' ')[0]+'\n')

createPath('interactions/clean_interactions')
moveFiles('interactions/*clean_interactions.txt','interactions/clean_interactions')
createPath('interactions/interactions_summary')
moveFiles('interactions/*Interactions_Summary.txt','interactions/interactions_summary')
Interacts2Csv('.')
