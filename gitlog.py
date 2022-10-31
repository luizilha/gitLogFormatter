# This project is a formatter git log to send a work history based in points
# How to use
# Run this file into git project
# Example: > python3 gitlog.py 
 
import os
import subprocess


def isDeleted(deletedPaths, line):
	for i in deletedPaths:
		if (i in line):
			return True
	return False


def removeDeletedLines():
	deleteFiles = subprocess.getoutput('git log --diff-filter=D --summary | grep delete')
	deleteFiles = deleteFiles.split()
	linesDelete = []
	for i in deleteFiles:
		if('src' in i):
			linesDelete.append(i)

	with open("resultado.txt", "r+") as f:
		d = f.readlines()
		f.seek(0)
		for i in d:
			if not(isDeleted(linesDelete, i)):
				f.write(i)
		f.truncate()


chave = input("Informe a sua chave: ")
dia = input("Informe o dia de comeco de registro (YYYY-MM-DD): ")

os.system(f"git log --name-status --author={chave} --after={dia}  --pretty=format:'#%h' > projeto")
nomeProjeto = subprocess.getoutput('echo "${PWD##*/}"')

with open("projeto", "r") as arqEntrada:
    with open("resultado.txt", "w") as arqSaida:
        endereco = ''
        for line in arqEntrada:
            if ('#' in line):
                endereco = line
            else: 
                if (len(line) > 1 and line[0] != 'D'):
                    arqSaida.write(nomeProjeto + "/" + line.split()[1].strip("\n") + endereco)

os.system(f'rm projeto')
removeDeletedLines()
