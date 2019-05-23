#https://stackoverflow.com/questions/15343743/copying-from-one-text-file-to-another-using-python
fin = open('book1.txt')
fout = open('copy1.txt', 'w')

count = 0

page = 0

for y in range(page):
	for i,val in enumerate(fin):
		s= val.strip("/n")
		for  j in s:
			print(j)
			if j == 'o' or j =='o':
				h = 'o'
				fou.write(h)
				elif j =='e' or j =='E'
					h = '3'
					fout.write(h)
				elif j == 'i' or j == 'I'
					h = '1'
					fout.write(h)
				else:
					fout.write(j)

				fout.write('/n')
				print(s)
				count +=1
				if count==25:
					break


