def bubbleSort(x):
  for i in range(len(x)-1):
    for j in range(len(x) - i):
      if x[j] > x[j+1]:
        x[j], x[j+1] = x[j+1], x[j] # swap

return x
