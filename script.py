#Programmed by mitchh02 on github

import os
import time
mods = []
temp = []
num = 0
manifest = open('manifest.json', 'r')
Lines = manifest.readlines()
for line in Lines:
	if "projectID" in line:
		for s in line.split():
			if s[-1] == ',':
				s = s[0:-1]
			if s.isdigit():
				temp.append(s)
				#print(s)
	elif "fileID" in line:
		for s in line.split():
			if s[-1] == ',':
				s = s[0:-1]
			if s.isdigit():
				temp.append(s)
				#print(s)
		mods.append(temp)
		temp = []
		num += 1
cur = 0
print(mods)
for item in mods:
	os.system('firefox https://www.curseforge.com/minecraft/mc-mods/{}/download/{}/file'.format(item[0], item[1]))
	cur += 1
	print('Current mod #{}/{}'.format(cur, num))
	time.sleep(0.3)
