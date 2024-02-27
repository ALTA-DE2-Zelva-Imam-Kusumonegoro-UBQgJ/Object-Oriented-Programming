class Operasi:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Penjumlahan(Operasi):
    def hitung(self):
        return self.x + self.y

class Pengurangan(Operasi):
    def hitung(self):
        return self.x - self.y

class Perkalian(Operasi):
    def hitung(self):
        return self.x * self.y

class Pembagian(Operasi):
    def hitung(self):
        if self.y == 0:
            return "Error"
        else:
            return int(self.x / self.y)

# Fungsi untuk melakukan operasi kalkulator
def output():
    penjumlahan = Penjumlahan(3, 4)
    print("Penjumlahan:", penjumlahan.hitung())

    pengurangan = Pengurangan(15, 4)
    print("Pengurangan:", pengurangan.hitung())
 
    perkalian = Perkalian(10, 10)
    print("Perkalian:", perkalian.hitung())
    
    pembagian = Pembagian(12, 3)
    print("Pembagian:", pembagian.hitung())


output()
