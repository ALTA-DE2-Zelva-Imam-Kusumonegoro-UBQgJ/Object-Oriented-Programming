import math

class BangunRuang:
    def __init__(self, sisi = 0, tinggi = 0, panjang = 0, lebar = 0):
        self.sisi = sisi
        self.tinggi = tinggi
        self.panjang = panjang
        self.lebar = lebar

class Kubus(BangunRuang):
    def hitung_volume(self):
        return self.sisi ** 3

class Balok(BangunRuang):
    def hitung_volume(self):
        return self.panjang * self.lebar * self.tinggi

class Tabung(BangunRuang):
    def hitung_volume(self):
        return math.ceil(math.pi * self.sisi ** 2 * self.tinggi)

def output():
    # Volume
    print("Volume")
    kubus = Kubus(sisi=10)
    print("Kubus:", kubus.hitung_volume())
    
    balok = Balok(panjang=3, lebar=6, tinggi=10)
    print("Balok:", balok.hitung_volume())
    
    tabung = Tabung(sisi=7, tinggi=10)
    print("Tabung:", tabung.hitung_volume())

output()
