#Linux binaries that can cause privilege escalation in linux
import subprocess

file=open("./binaries", "r")

count = 0
binaries = file.readlines()
found_binaries = [''] # binaries found in /usr/bin
notfound_binaries = [''] # not found binaries in /usr/bin

for line in binaries:
	temp_binary = line.strip()
	temp_binary_path = "locate -r /usr/bin/" + temp_binary + "$"
	try:
		output = subprocess.check_output(temp_binary_path, shell=True)
		found_binaries.append(output)	
	except subprocess.CalledProcessError as e:
		try:
			temp_binary_path = "locate -r /usr/sbin/" + temp_binary + "$"
			output = subprocess.check_output(temp_binary_path, shell=True)
			found_binaries.append(output)	
		except subprocess.CalledProcessError as e:
			notfound_binaries.append(output)	    	
	temp_binary_path = ""

print('\n___________________________________________________')
print("Binaries Found the can cause privilege escalation!")
print('___________________________________________________')
for binary in found_binaries:
	print(binary.strip())

print('\n___________________________________________________')
print("Binaries that are Not Found!")
print('___________________________________________________')
for binary in notfound_binaries:
	print(binary.strip())

















