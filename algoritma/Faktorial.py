print("-------------------------------------------")
print("--------------------UAS--------------------")
print("---------------------1---------------------")
print("-------------------------------------------")
print("-------------------------------------------")
print("")
def faktorial(x):
  if x<=1: # base scenario
    return 1
  else:
    f = x * faktorial(x-1)
  return f

print('Menghitung bilangan faktorial menggunakan fungsi rekursif')
angka = int(input('Masukkan bilangan = '))
faktorial_bil = faktorial(angka)
print('Bilangan faktorial dari {} adalah {}'.format(angka,faktorial_bil))
