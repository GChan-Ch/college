print("-------------------------------------------")
print("--------------------UAS--------------------")
print("----------------Menara Hanoi---------------")
print("-------------------------------------------")
print("-------------------------------------------")
print("")
def TowerOfHanoi(n , source, destination, auxiliary):
        if n==1:
                print ("Pindahkan piringan 1 dari menara",source,"ke menara",destination)
                return
        TowerOfHanoi(n-1, source, auxiliary, destination)
        print ("Pindahkan piringan",n,"dari menara",source,"ke menara",destination)
        TowerOfHanoi(n-1, auxiliary, destination, source)

# Driver code
n = 4
TowerOfHanoi(n,'A','C','B')
# A, C, B are the name of rods

