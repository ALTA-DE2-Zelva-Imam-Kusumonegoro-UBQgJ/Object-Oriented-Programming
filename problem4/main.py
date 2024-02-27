class Barang:
    def __init__(self, panjang, lebar, tinggi, berat):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
        self.berat = berat

class Pengiriman(Barang):
    def hitung_volume(self):
        return self.panjang * self.lebar * self.tinggi
    
    def hitung_harga(self):
        volume = self.hitung_volume()
        harga_per_kg = 5000  
        harga_minimum = 5000  

        if volume < 50:
            return harga_minimum
        else:
            berat_bulat = round(self.berat) 
            harga_total = max(harga_minimum, berat_bulat * harga_per_kg)
            return harga_total


def output(panjang, lebar, tinggi, berat):
    pengiriman = Pengiriman(panjang, lebar, tinggi, berat)
    harga = pengiriman.hitung_harga()
    print("Harga: Rp", harga)


output(5, 2, 4, 1)
