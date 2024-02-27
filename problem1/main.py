class BangunDatar:
    def __init__(self, sisi=0, tinggi=0):
        self.sisi = sisi
        self.tinggi = tinggi

class Persegi(BangunDatar):
    def hitung_luas(self):
        return self.sisi ** 2
    
    def hitung_keliling(self):
        return 4 * self.sisi

class Segitiga(BangunDatar):
    def hitung_luas(self):
        return int(0.5 * self.sisi * self.tinggi)
    
    def hitung_keliling(self):
        sisi_miring = (self.sisi ** 2 + self.tinggi ** 2) ** 0.5
        return int(self.sisi + self.tinggi + sisi_miring)

class PersegiPanjang(BangunDatar):
    def hitung_luas(self):
        return self.sisi * self.tinggi
    
    def hitung_keliling(self):
        return 2 * (self.sisi + self.tinggi)

def output():
    print("Luas")
    persegi = Persegi(sisi=4)
    print("Persegi:", persegi.hitung_luas())
    
    segitiga = Segitiga(sisi=3, tinggi=4)
    print("Segitiga:", segitiga.hitung_luas())
    
    persegi_panjang = PersegiPanjang(sisi=7, tinggi=8)
    print("Persegi Panjang:", persegi_panjang.hitung_luas())
    
    # Keliling
    print("\nKeliling")
    print("Persegi:", persegi.hitung_keliling())
    print("Segitiga:", segitiga.hitung_keliling())
    print("Persegi Panjang:", persegi_panjang.hitung_keliling())

# Memanggil fungsi untuk menghitung luas dan keliling
output()
