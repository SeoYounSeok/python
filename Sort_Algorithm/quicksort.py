def quicksort(list):
  
  pivot = list[len(list)/2]
  if list > 1 :
    left , right , equal = [],[],[]
    
    for x in list :
     
      if x < pivot:
          left.append(x)
      elif x > pivot: 
          right.append(x)
      else 
          equal.append(x)
          
  return quicksort(left) + equal + quicksort(right)
  
  else 
    return list
