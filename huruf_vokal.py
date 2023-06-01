r1=open("C:/Users/NOVO/Downloads/Hitung Huruf Vokal.txt","r")
r2=r1.read()
r1.close()
def jumlah(huruf):
	output=0
	vokal=['a','i','u','e','o']
	for a in huruf:
		if a in vokal:
			output +=1
	return output
	
def get_huruf_hidup(huruf):
	output = 0
	for a in huruf.lower().split(" "):
		output += jumlah(a)
	return output
	
a1= get_huruf_hidup(r2)
print(f"jumlah huruf vokal : {a1}")

		
		