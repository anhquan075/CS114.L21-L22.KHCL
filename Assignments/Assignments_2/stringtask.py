m = str(input()).lower()

temp = ['A', 'O', 'Y', 'E', 'U', 'I','a', 'o', 'y', 'e', 'u', 'i']

n = ''

for i in m:
	if i in temp:
		m = m.replace(i,'')

for i in m:
	n = n + '.'
	if i != '.':
		n = n + i

print(n)