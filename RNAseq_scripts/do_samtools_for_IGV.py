#! /home/naoki/miniconda3/bin/python
import os 
import sys
import time
import subprocess
from subprocess import Popen, PIPE

wd = os.getcwd() 
command_sam_1 = "samtools view -bS " + sys.argv[1] + ".sam > " + sys.argv[1] + ".bam"
print(command_sam_1)
subprocess.call(command_sam_1, shell=True)
command_sam_2 = "samtools sort " + sys.argv[1] + ".bam -o " + sys.argv[1] + ".sorted.bam"
print(command_sam_2)
subprocess.call(command_sam_2, shell=True)
command_sam_3 = "samtools index " + sys.argv[1] + ".sorted.bam"
print(command_sam_3)
subprocess.call(command_sam_3, shell=True)

