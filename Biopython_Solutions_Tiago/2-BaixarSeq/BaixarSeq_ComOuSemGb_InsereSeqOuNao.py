print("Baixar sequencias do Genbank (ate 200 acessos)")
print('Adaptado por Tiago Andrade Borges Santos')

from Bio import Entrez
f=open('sequence.gb','w')
Entrez.email = "identifiqueseprogenbank@gmail.com"     # Always tell NCBI who you are
print("Insira sua lista de acessos do Genbank entre aspas, separados por virgula.")
print("Exemplo: 'GU479772', 'GU479773'")
record = input("Seqs: ")
gb_list = (record)
gb_str = ",".join(gb_list)
handle = Entrez.efetch(db="nuccore", id=gb_str, rettype="gb", retmode="txt")
text = handle.read()
f.write(str(text+'\n'))
f.close()

print("Sequencias com Genbank Number (1) ou sem Genbank Number (2)?")
resposta=int(input("resposta: "))

from Bio import SeqIO #importar SeqIO a partir do biopython:
sequencias = SeqIO.parse('sequence.gb','genbank')
nseq=0 #variavel para contar o numero de sequencias processadas
f=open('sequence.fas','w') #abre o arquivo onde vai salvar os resultados

if resposta == 1:
	for seq in sequencias: #loop que itera cada uma das sequencias
		generoespecie=seq.annotations['organism'].split(' ')
		f.write('>'+generoespecie[0]+'_'+generoespecie[1]+'_'+seq.name+'\n')
		f.write(str(seq.seq)+'\n')
		nseq=nseq+1 #incrementa a variavel para cada sequencia processada
elif resposta == 2:
	for seq in sequencias: #loop que itera cada uma das sequencias
		generoespecie=seq.annotations['organism'].split(' ')
		f.write('>'+generoespecie[0]+'_'+generoespecie[1]+'\n')
		f.write(str(seq.seq)+'\n')
		nseq=nseq+1 #incrementa a variavel para cada sequencia processada
else:
	print('Resposta errada. Tente novamente.')

print("Inserir uma sequencia? Sim (1) ou Nao (2)?")
resposta=int(input("resposta: "))

# You may often have many sequences to add together, which can be done with a for loop like this:
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

if resposta == 1:
	inserenome=(raw_input('apenas o nome da sequencia: '))
	f.write(str(inserenome)+'\n')
	insereseq=(raw_input('apenas a sequencia: '))
	f.write(str(insereseq))
else:
	f.close()

f.close()





