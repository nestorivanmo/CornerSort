import random

contador = 0
listaOrdenada = []

def cornerSort(data,element):                       #log(n)
    global contador
    global listaOrdenada
    if len(data) == 1:                              ##4
        listaOrdenada.append(data[0])               ##4
        return                                      ##1
    else:
        low = []                                    ## 1
        high = []                                   ## 1
        i = 0                                       ## 1   ------- 12
        while i < len(data):                        ## 4n
            contador += 1                           ## 3(n-1)
            if data[i] < element:                   ## 4(n-1)
                low.append(data[i])                 ## 4(n-1)
            else:
                high.append(data[i])                ## 4(n-1)
            i += 1                                  ## 3(n-1) ------ 22n - 18
        if not low:                           ##1
            if high == data:                        ##3
                e = high[len(high)-1]               ##6
                if high[0] != e:                    ##4      ------14
                    high[0],high[len(high)-1] = high[len(high)-1], high[0] ##6
                    cornerSort(high, e)             ##2
                else:
                    x = 0                           ##2      ------10
                    while x < len(high):            ##4n
                        if data[x] != e:            ##4(n-1)
                            e = data[x]             ##4(n-1)
                            break                   ##1(n-1)
                        x += 1                      ##3(n-1) ------ 16n -12
                    if e != high[len(high)-1]:      ##6
                        cornerSort(high, e)         ##2
                    else:
                        listaOrdenada += high       ##4
            else:
                cornerSort(high, high[len(high)-1]) ##4
            return
        else:
            cornerSort(low, low[0])                 ##3
            cornerSort(high, high[len(high)-1])     ##4     ------- 21
    return listaOrdenada                            ## 38n + 27




# data = [7,35,124,641,45,124,62,234,6235,5,6132,24,51,61,7127,8,3,7127,12,8,1]
# data = [10,9,8,7,6,5,4,3,2,1]
# data = [1,2,3,4,5,6,7,8,9,10]
# data = [1,1,1,1,1,1,1,1,2,14,1,4134,-1,432,52,5,63,65,65,65,65]
# data = [14,52,5]
# data = [87,1,35,55,46,124,6,7124,1234,2,1236,375,357,345,234,4,126,712,6,352]
# data = [20,1,3,4,6,7]


data = [2,7,5,15,70,-10,35]
# for i in range(0,20000):
#     data.append(random.randint(0,1000))

print(data)
cornerSort(data, data[1])
print("D")
print(listaOrdenada)
