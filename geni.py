#Trovare geni su genome

import bs4, requests, webbrowser

cro = str(1)#input("cromosoma: ")
in_seq = str(1)#input("inizio sequenza: ")
fin_seq = str(100000)#input("fine sequenza: ")
seq = "-".join([in_seq, fin_seq])
print (seq)

genome = "https://genome.ucsc.edu/cgi-bin/hgTracks?db=hg19&lastVirtModeType=default&lastVirtModeExtraState=&virtModeType=default&virtMode=0&nonVirtPosition=&position=chr" + cro + "%3A" + seq


res = requests.get(genome)
res.raise_for_status()


soup = bs4.BeautifulSoup(res.text, "html.parser")


elem = soup.find_all("area",{"class" : "area"}, 'title') 
file = open("base.html", "w")
file.write(soup.prettify())

file = open('genometitle.html', 'a')
print(len(elem))



for i in range(len(elem)):
	file.write(elem[i]['title'])#.get())
	#file.write(str(elem[i].attrs))
	file.write("\n")
file.close()


#x = soup.body
#print(x)
#print(type(x))


#elem = soup.find("", {"id" : "td_data_knownGene"}) 
#la tabella da guardare porta a td_side_knownGene

#elem = soup.find("", {"id" : "td_side_knownGene"}) 

#elem = soup.find_all("map", "map_data_knownGene")

#prova = elem.get('title')
#print(prova)

#print(elem[0].attrs)

#elem = soup.findAll("", {"name" : "map_side_knownGene"})
#elem = soup.findAll('area')#[class="area"]')

#print(type(elem), len(elem))


#print (elem)





#sel = soup.select('name="map_side_knownGene"')


#print(sel)
#print(len(sel))
#for riga in elem:
#	righe.append(riga)

#bimbi = list()
#for child in sel.children:
#	bimbi.append(child)

#elem = soup.select("tr_knownGene")#('#imgTbl')

