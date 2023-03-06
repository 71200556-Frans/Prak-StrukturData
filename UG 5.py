class Karyawan :
    _nama=""
    _umur=""
    _jenisKelamin=""
    _upahPerHari=0.0

    def __init__(self ,nama,umur,jenisKelamin,upahPerHari):
        self . _nama = nama
        self . _umur = umur
        self . _jenisKelamin = jenisKelamin
        self . _upahPerHari = upahPerHari
    
    def setnama(self ,nama):
        self . _nama = nama

    def setumur(self ,umur):
        self . _umur = umur

    def setJenisKelamin(self ,jenisKelamin):
        self . _jenisKelamin = jenisKelamin

    def setUpahPerHari(self ,upahPerHari):
        self . _upahPerHari = upahPerHari

cc = Karyawan()
cc.setNama("Sindu")
cc.setUmur(190)
cc.setJenisKelamin("Laki-laki")
cc.setUpahPerHari(30000)

def printinfo ():
    print("===========INFO=========")
    print(cc.getNama())
    print(cc.getUmur())
    print(cc.getJenisKelamin())
    print(cc.getUpahPerHari())

