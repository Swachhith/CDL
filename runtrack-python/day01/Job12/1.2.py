def drawtriangle(n):
  for i in range(0, n):
    print(' '*(n-i+1) + '/' + ' '*(i*2) + '\\')

    if (i == n-1):
      print(' '*(n-i) + '/' + '_'*(i*2+2) + '\\')  
drawtriangle(5)      