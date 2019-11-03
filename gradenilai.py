nilai = input("Silahkan inputkan nilai anda : ")

if nilai >= 90:
    grade = "A"
elif nilai >= 85:
    grade = "A-"
elif nilai >= 82:
    grade = "B+"
elif nilai >=75:
    grade = "B"
elif nilai >= 70:
    grade = "C"
else:
    grade = "E"

print ("Grade anda : %s" ) % grade 