def rmv(array, index):
# removes single elements located at index in given array
  rmved = []
  for i in range(len(array)):
      if i == index:
        continue
      else:
        rmved.append(array[i])
  return rmved

def newmax(array):
# sorts the given array from maximum to minimum
  sorted = []
  initialarr = len(array)
  maxindex = 0
  while len(sorted)<initialarr:
    m = 0
    k = array[0]
    for i in array:
      if (k==i) or (k>i):
        m += 1
        continue
      else:
        k = i
        maxindex = m
        m += 1
    sorted.append(k)
    array = rmv(array, maxindex)
  return sorted

def rmvarrindex(array, indexarray):
# removes multiple elements given by array of indexes
  sortedindexarray = newmax(indexarray)
  for i in sortedindexarray:
    array = rmv(array,i)

  return array

def indfinder(array, element):
# finds the index of element in array
  indexes = []
  z = 0
  for i in array:
    if i == element:
      indexes.append(z)
      z += 1
      continue
    else:
      z += 1
      continue
  return indexes

def uniquefinder(array):
# returns the unique values of array
  uniq = []
  while len(array)>0:
    k = array[0]
    indices = indfinder(array, k)
    array = rmvarrindex(array, indices)
    uniq.append(k)
    continue
  return uniq

