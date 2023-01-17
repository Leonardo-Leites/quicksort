from audioop import reverse
from math import ceil
from time import process_time
import random

output = ["stats-aleatorio-hoare.txt","stats-aleatorio-lomuto.txt","stats-mediana-hoare.txt","stats-mediana-lomuto.txt"]

def aleatorioLomuto(vet):
  global recursao, swap, tamanho
  
  recursao +=1

  if len(vet) <=1:
    return vet
    
  pivo = vet[:1]
  vet = vet[1:]

  esquerda = []
  direita = []
  for item in vet:
    if item <= pivo[0]:
      swap +=1
      esquerda.append(item)
    else:
      swap +=1
      direita.append(item)
  return (aleatorioLomuto(esquerda) + pivo + aleatorioLomuto(direita))
def aleatorioHoare(vet,inicio,fim):
  global recursao, swap

  recursao +=1
  if len(vet) <=1:
    return vet

  pivo = vet[inicio]
  esquerda = True

  while inicio < fim:
      if esquerda is True:
          if pivo >= vet[fim]:
              vet[inicio] = vet[fim]
              inicio += 1
              swap += 1
              esquerda = False
          else:
              fim -= 1
      else:
          if pivo < vet[inicio]:
              vet[fim] = vet[inicio]
              fim -= 1
              swap += 1
              esquerda = True
          else:
              inicio += 1

  vet[inicio] = pivo

  return inicio
def medianaLomuto(vet):
  global recursao, swap, tamanho
  
  recursao +=1

  if len(vet) <=1:
    return vet

  aux = [vet[0], vet[int(len(vet)/2)], vet[-1]]
  aux.sort()

  valueAux = vet[0]
  vet[0] = vet[aux[1]]
  vet[aux[1]] = valueAux

  pivo = vet[:1]
  vet = vet[1:]
  
  esquerda = []
  direita = []
  for item in vet:
    if item <= pivo[0]:
      swap +=1
      esquerda.append(item)
    else:
      swap +=1
      direita.append(item)
  return (aleatorioLomuto(esquerda) + pivo + aleatorioLomuto(direita))
def medianaHoare(vet,inicio,fim):
  global recursao, swap

  recursao +=1
  if len(vet) <=1:
    return vet

  pivo = vet[inicio]
  esquerda = True

  while inicio < fim:
      if esquerda is True:
          if pivo >= vet[fim]:
              vet[inicio] = vet[fim]
              inicio += 1
              swap += 1
              esquerda = False
          else:
              fim -= 1
      else:
          if pivo < vet[inicio]:
              vet[fim] = vet[inicio]
              fim -= 1
              swap += 1
              esquerda = True
          else:
              inicio += 1

  vet[inicio] = pivo

  return inicio

def write(output, tamanho, recursao,swap, start):
    saida = open(output,"a")
    linhasParaOArquivo = ["TAMANHO ENTRADA "+tamanho,"SWAPS "+swap,"RECURSOES "+recursao,"TEMPO "+str(start)]
    
    for lnh in linhasParaOArquivo:
        saida.write(lnh)
        saida.write("\n")
    saida.close()
with open('entrada-quicksort.txt', 'r') as f:
    results = [[int(entry) for entry in line.split()] for line in f.readlines()]

def  quickLomutoAleatorio():

  for count in range(0, 5):
    
    global tamanho, recursao, swap, start

    start = process_time()
    tamanho = results[count][0]
    recursao = 0
    swap = 0
    vet = results[count]
    
    aux = random.randint(0, len(vet)-1)    
    vet = vet[1:]
    valueAux = vet[0]
    vet[0] = vet[aux]
    vet[aux] = valueAux
    
    aleatorioLomuto(vet)
 
    stop = process_time()
    start = stop-start
    
    write(output[1], str(tamanho), str(recursao), str(swap),str(start))
def  quickHoareAleatorio():

  for count in range(0, 5):
    
    global tamanho, recursao, swap, start

    start = process_time()
    tamanho = results[count][0]
    recursao = 0
    swap = 0
    vet = results[count]
    
    aux = random.randint(1, len(vet))    
    vet = vet[1:]
    valueAux = vet[0]
    vet[0] = vet[aux]
    vet[aux] = valueAux

    inicio = 0
    fim = tamanho-1

    def volta(vet,inicio,fim):
      if fim > inicio:
        pos_pivo = aleatorioHoare(vet,inicio,fim)

        volta(vet, inicio, pos_pivo - 1)
        volta(vet, pos_pivo + 1, fim)
    volta(vet,inicio,fim)

    stop = process_time()
    start = stop-start
    
    write(output[0], str(tamanho), str(recursao), str(swap),str(start))
def  quickLomutoMediana():

  for count in range(0, 5):
    
    global tamanho, recursao, swap, start

    start = process_time()
    tamanho = results[count][0]
    recursao = 0
    swap = 0
    vet = results[count]
    
    vet = vet[1:]

    medianaLomuto(vet)

    stop = process_time()
    start = stop-start
    
    write(output[3], str(tamanho), str(recursao), str(swap),str(start))
def  quickHoareMediana():

  for count in range(0, 5):
    
    global tamanho, recursao, swap, start

    start = process_time()
    tamanho = results[count][0]
    recursao = 0
    swap = 0
    vet = results[count]
    
    vet = vet[1:]

    aux = [vet[0], vet[int(len(vet)/2)], vet[-1]]
    aux.sort()

    valueAux = vet[0]
    vet[0] = vet[aux[1]]
    vet[aux[1]] = valueAux

    inicio = 0
    fim = tamanho-1

    def volta(vet,inicio,fim):
      if fim > inicio:
        pos_pivo = medianaHoare(vet,inicio,fim)

        volta(vet, inicio, pos_pivo - 1)
        volta(vet, pos_pivo + 1, fim)
    volta(vet,inicio,fim)

    stop = process_time()
    start = stop-start
    
    write(output[2], str(tamanho), str(recursao), str(swap),str(start))
recursao = 0
swap = 0
tamanho = 0
start = 0

# retire o comentário de qual função deseja utilizar - obs: limpe os dados dos arquivos de saída
# quickLomutoAleatorio()
# quickHoareAleatorio()
# quickHoareMediana()
# quickLomutoMediana()
