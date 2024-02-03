num = int(input("masukkan bilangan ganjil di atas 20 : "))

while num % 2 == 0 or num < 20:
    num = int(input("masukkan bilangan ganjil di atas 20 : "))
else:
    print("benar..")
