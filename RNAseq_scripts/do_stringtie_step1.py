#! /home/naoki/miniconda3/bin/python
import os 
import sys
import time
import subprocess
from subprocess import Popen, PIPE

print(sys.argv[1])
time.sleep(1)
wd = os.getcwd() #"/home/naoki/Documents/rnaseq"
command = "stringtie " + sys.argv[1] + ".bam -p 4 -G " + wd + "/TAIR10/Athaliana_167_TAIR10.gene.gff3 -o " + sys.argv[1] + ".gtf"
print(command)
subprocess.call(command, shell=True)

