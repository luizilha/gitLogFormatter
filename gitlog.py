# This project is a formatter git log to send a work history based in points
# How to use
# Run this file into git project
# Example: > python3 gitlog.py 
 
import os
import subprocess

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
                if (len(line) > 1):
                    arqSaida.write(nomeProjeto + "/" + line.split()[1].strip("\n") + endereco)


# Next steps to project:
# Remove delete files from git log
# git log --diff-filter=D --summary | grep delete
