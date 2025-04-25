import nháp # Note no.py

values= [2,4,6,8,10]
print('Squares:')
for v in values:
    print (nháp.square(v))
print("Cubes:")
for v in values:
    print(nháp.cube(v))
print('Average:'+ str(nháp.average(values)))