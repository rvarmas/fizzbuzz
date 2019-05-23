#https://stackoverflow.com/questions/15343743/copying-from-one-text-file-to-another-using-python
#https://stackoverflow.com/questions/41854418/how-to-replace-the-same-lowercase-and-uppercase-letters-with-a-number-in-python
fin = open('book1.txt')
fout = open('copy1.txt', 'w')

count = 0

page = 0

 #if encrp_key == 1:
     # new_msg = msg.replace('a ','1').replace('e','2')\ .replace('i','3').replace('o','4').replace('u','5')


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

		page +=1

fount.close()

