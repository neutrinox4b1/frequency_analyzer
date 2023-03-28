import json

def print_menu():
	print('')
	print('=================================================')
	print('0. show freqency')
	print('1. show substitution')
	print('2. modify substitution')
	print('3. import substitution')
	print('4. export substitution')
	print('5. export sorted_freq.json')
	print('9. exit')
	print('=================================================')

def show_freq():
	print('==================frequncy===================')
	for key, value in sorted_freq.items():
		print(key, ':', value)
	print('=============================================')

def show_sub():
	print('==================substitution===================')
#	while i < len(numbered_sub_freq)//10:
#		j = 0
#		while j < len(numbered_sub_freq):
#			print(j, numbered_sub_freq[j][0],':', numbered_sub_freq[j][1], end='\t')
#		print('\n')
	i = 0
	for key, value in sub_freq.items():
		print(i, key, ':', value, end='\t')
		if i%6 == 0:
			print('')
		i += 1
	print('=================================================')
	
def modify_sub():
	show_sub()
	for key, value in sub_freq.items():
		if value != '':
			cipher = cipher.replace(key, value)

def import_sub():
	with open('sub.json', 'r') as f:
		sub_freq = json.load(f)
#	for i, (key, value) in enumerate(sub_freq.items()):
#		numbered_sub_freq[i] = (key, value)

def export_sub():
	with open('sub.json', 'w') as f:
		json.dump(sub_freq, f, indent=4)

def export_sorted():
	with open('sorted_freq.json', 'w') as f:
		json.dump(sorted_freq, f, indent=4)

with open('cipher.txt', 'r') as f:
	cipher = f.read()
freq = {}
for c in cipher:
	if c not in freq:
		freq[c] = 1 else: freq[c] += 1

sorted_freq= dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))

tmp = sorted_freq.copy()
for key in tmp.keys():
	if key.isspace():
		del sorted_freq[key]

sub_freq = {}
for key in sorted_freq.keys():
	sub_freq[key] = ''

#numbered_sub_freq = {}
#for i, (key, value) in enumerate(sub_freq.items()):
#	numbered_sub_freq[i] = (key, value)

while True:
	print(cipher)
	print_menu()
	cmd = int(input('> '))

print('==================result===================')
print(cipher)
print('===========================================')
