#! /home/naoki/miniconda3/bin/python
import os 
import sys
import time
import subprocess
from subprocess import Popen, PIPE

# Set directory
wd = os.getcwd()
print(wd)
# Read mergelist.txt 
with open(wd + '/mergelist.txt', 'r') as f:
    for line in f:
        samplename = line.replace('.gtf', '')
        samplename = samplename.replace('\n', '')
        time.sleep(1)
        sampledir = wd + '/ballgown/' + samplename
        print(sampledir)
        os.mkdir(sampledir)
        time.sleep(1)
        command = "stringtie " + samplename + ".bam -e -B -p 4 -G " + "merged_data.gtf -o " + sampledir + "/ball_" + samplename + ".gtf"
        print(command)
        subprocess.call(command, shell=True)
