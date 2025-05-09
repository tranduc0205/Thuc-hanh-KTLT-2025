
input_file= open('C:/lt 2025/bài 7/a.txt',"r")
for line in input_file:
   l=len(line)
   s=""
   while(l>1):
      s=s+line[l-1]
      l=l-1
   print(s)
input_file.close()