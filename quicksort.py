import time

vet = [1,0,34,12,7,8,525]

start = time.process_time()

def quick(vet):
  if len(vet) <=1:
    return vet
  pivo = vet[:1]
  vet = vet[1:]

  lista1 = []
  lista2 = []
  for item in vet:
    if item < pivo[0]:
      lista1.append(item)
      # print(lista1)
    else:
      lista2.append(item)
      # print(lista2)
  return (quick(lista1) + pivo + quick(lista2))

print(quick(vet))
print(start)