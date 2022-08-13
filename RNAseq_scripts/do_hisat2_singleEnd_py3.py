#! /home/naoki/miniconda3/bin/python
import os 
import sys
import time
import subprocess
from subprocess import Popen, PIPE

time.sleep(1)
wd = os.getcwd() # "/home/naoki/Documents/rnaseq"

command = "hisat2 -p 4 --dta -x " + wd + "/TAIR10/index/TAIR10 -q -U " + wd + "/" + sys.argv[1] + ".fastq.gz  -S " + sys.argv[1] + ".sam"

#command = "hisat2 -p 4 --dta -x " + wd + "/TAIR10/index/TAIR10 -q -U " + wd + "/" + sys.argv[1] + ".fastq  -S " + sys.argv[1] + ".sam"

print(command)

subprocess.call(command, shell=True)

