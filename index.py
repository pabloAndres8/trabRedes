import csv


path = str(input('Por favor, digite o caminho para o arquivo .csv:'))
ipv4 = str(input('Ponha o endereço IPv4:'))



arq = csv.reader(open(path),delimiter=';')
for line in arq:
    if(ipv4 == line[0]):
        print(line[2])
    else:
        print("Não foi encontrado a interface para o ip")