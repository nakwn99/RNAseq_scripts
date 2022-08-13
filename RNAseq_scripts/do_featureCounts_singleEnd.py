#! /home/naoki/miniconda3/bin/python
import os 
import sys
import time
import subprocess
from subprocess import Popen, PIPE

time.sleep(1)
command = "ls *.sam > samlist.txt"
print(command)
subprocess.call(command, shell=True)
time.sleep(2)

wd = os.getcwd()
samlist = open(wd + "/samlist.txt", 'r')
sams = samlist.readlines()
samlist.close()

print(sams)
#
# Process singlEnd data
#
command = "featureCounts -M -O  -T4 -t exon -g gene_id -a " + wd + "/TAIR10/TAIR10_GTF2_genes.gtf -o count_featureCounts.txt"
for c in sams:
	c = c[0:(len(c)-1)]
	command = command + " " + c

print(command)

subprocess.call(command, shell=True)


