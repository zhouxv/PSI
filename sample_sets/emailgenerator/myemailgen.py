#!/usr/bin/python
import random
import sys

gnames_file = "Given-Names.txt"
fnames_file = "Family-Names.txt"
eprovs_file = "Email-Providers.txt"

STOP_AFTER_FAILURES = 20 # stop after this number of failures

if len(sys.argv)!=3:
 print("Syntax: "+sys.argv[0]+" N File")
 print("Generates a sorted list of N unique email adresses")
 exit()

N = int(sys.argv[1])

gnames = [line.strip() for line in open(gnames_file)]
fnames = [line.strip() for line in open(fnames_file)]
eprovs = [line.strip() for line in open(eprovs_file)]

# generate list of emails with N *unique* entries
emails = set()
failures=0
while len(emails) < N:
        gname = random.choice(gnames)
        fname = random.choice(fnames)
        eprov = random.choice(eprovs)
        email=gname+'.'+fname+'@'+eprov
        if (email in emails):
                failures+=1
                if failures == STOP_AFTER_FAILURES:
                        exit("Failure: Unable to generate new unique email.")
        else:
                failures = 0
                emails.add(email)

# sort list of emails
emails_list = list(emails)
# emails_list.sort()

# w : 打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件
file = open(sys.argv[2],'w')

for e in emails_list:
 file.write(e+'\n')

file.flush()
file.close()

