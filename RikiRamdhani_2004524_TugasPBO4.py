#Superclass
class Pendidikan():
    
    def __init__(self, nama_sekolah, alamat_sekolah ) :
        self.nama_sekolah = nama_sekolah
        self.alamat_sekolah = alamat_sekolah

#Subclass Pendidikan Sekolah Dasar dan Sekolah Menengah Atas
class Pendidikan_SekolahDasar(Pendidikan):
    pass

class Pendidikan_SekolahMenengahAtas(Pendidikan):
    pass

Alhusna = Pendidikan("Alhusna", "Bandung")
SDN1Cilegon = Pendidikan_SekolahDasar("SDN1Cilegon", "Cilegon")
SMA51Jakarta = Pendidikan_SekolahMenengahAtas("SMA51Jakarta", "Jakarta")

#Output
print(Alhusna.nama_sekolah, Alhusna.alamat_sekolah)
print(SDN1Cilegon.nama_sekolah, SDN1Cilegon.alamat_sekolah)
print(SMA51Jakarta.nama_sekolah, SMA51Jakarta.alamat_sekolah)
