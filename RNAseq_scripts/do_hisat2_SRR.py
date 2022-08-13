#! /home/naoki/miniconda3/bin/python
import os 
import sys
import time
import subprocess
from subprocess import Popen, PIPE

time.sleep(1)
wd = os.getcwd() #"/home/naoki/Documents/rnaseq"

srr = sys.argv[1]
ask1 = srr.find('_1')
#print(ask1)
if (ask1 == -1):
    srr = srr.replace('_2', '')
    print(srr)

    command = "hisat2 -p 4 --dta -x " + wd + "/TAIR10/index/TAIR10 -q " +  "--sra-acc " + srr + " -S " + srr + ".sam"
    print(command)

    subprocess.call(command, shell=True)


