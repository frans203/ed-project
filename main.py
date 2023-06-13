import time
import pprint
from algorithms import Algoritmhs
def readFile(option):
    array = []
    
    if option == 1:
        file = "instances/num.1000.1.in"
    elif option == 2:
        file = "instances/num.1000.2.in"
    elif option == 3:
        file = "instances/num.1000.3.in"
    elif option == 4:
        file = "instances/num.1000.4.in"
    elif option == 5:
        file = "instances/num.10000.1.in"
    elif option == 6:
        file = "instances/num.10000.2.in"
    elif option == 7:
        file = "instances/num.10000.3.in"
    elif option == 8:
        file = "instances/num.10000.4.in"
    elif option == 9:
        file = "instances/num.100000.1.in"
    elif option == 10:
        file = "instances/num.100000.2.in"
    elif option == 11:
        file = "instances/num.100000.3.in"
    elif option == 12:
        file = "instances/num.100000.4.in"
    else:
        print("Selecione uma opção válida")

    with open(file, 'r') as file:
        arq = file.readlines()

    for linha in arq:
        num = int(linha)
        array.append(num)

    return array

def chooseAlgorithm(optionFromList, list):
    if optionFromList == 1:
       array = list.copy()
       startTime = time.time()
       Algoritmhs().selectionSort(array)
       endTime = time.time()
       total = endTime - startTime
       pprint.pprint(array, compact=True, width=100)
       print("Tempo total gasto para selectionSort:", total, "segundos")

    elif optionFromList == 2:
       array = list.copy()
       startTime = time.time()
       Algoritmhs().bubbleSort(array)
       endTime = time.time()
       total = endTime - startTime
       pprint.pprint(array, compact=True, width=100)
       print("Tempo total gasto para bubbleSort:", total, "segundos")
    elif optionFromList == 3:
       array = list.copy()
       startTime = time.time()
       Algoritmhs().insertionSort(array)
       endTime = time.time()
       total = endTime - startTime
       pprint.pprint(array, compact=True, width=100)
       print("Tempo total gasto para insertionSort:", total, "segundos")
    elif optionFromList == 4:
       array = list.copy()
       startTime = time.time()
       Algoritmhs().mergeSort(array)
       endTime = time.time()
       total = endTime - startTime
       pprint.pprint(array, compact=True, width=100)
       print("Tempo total gasto para mergeSort:", total, "segundos")
    elif optionFromList == 5:
       array = list.copy()
       startTime = time.time()
       Algoritmhs().quickSort(array)
       endTime = time.time()
       total = endTime - startTime
       pprint.pprint(array, compact=True, width=100)
       print("Tempo total gasto para quickSort:", total, "s")
    

print("Bem vindo!")
print("Projeto de estrutura de dados feito por: Francisco Santana\nImplementando os seguintes algoritmos e verificando seus tempos de execução:")
print("SelectionSort, bubbleSort, insertionSort, mergeSort, quickSort")

array = []
while True:
    try:
        optionFile = int(input('Selecione primeiro o arquivo de instâncias desejado: \n1 - num.1000.1.in\n2 - num.1000.2.in\n3 - num.1000.3.in\n4 - num.1000.4.in\n5 - num.10000.1.in\n6 - num.10000.2.in\n7 - num.10000.3.in\n8 - num.10000.4.in\n9 - num.100000.1.in\n10 - num.100000.2.in\n11 - num.100000.3.in\n12 - num.100000.4.in\n'))
        if optionFile < 1 or optionFile > 12:
             print("Selecione um número válido")
             continue
        else:
            array = readFile(optionFile)
            break;
    except ValueError:
        print("Selecione um número válido")

while True:
    try:
        optionAlgo = int(input('Agora, selecione o algorimo desejado:\n0) Sair\n1) SelecionSort\n2) BubbleSort \n3) InsertionSort \n4) MergeSort\n5) QuickSort\nOpção:'))
        if optionAlgo < 0 or optionAlgo > 5:
             print("Selecione um número válido")
             continue
        elif optionAlgo == 0:
            print("Obrigado")
            break
        else:
            chooseAlgorithm(optionAlgo, array)
            continue
    except ValueError:
         print("Selecione um número válido")
