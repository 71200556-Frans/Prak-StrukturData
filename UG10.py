class RakObat:
    def __init__(self, size):
        self.size = size
        self.hash_table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def tambahObat(self, jenisObat, namaObat):
        index = self.hash_function(jenisObat)
        while self.hash_table[index] is not None:
            if self.hash_table[index][0] == jenisObat:
                return False  # Jenis obat sudah ada dalam hash table
            index = (index + 1) % self.size
        self.hash_table[index] = (jenisObat, namaObat)
        return True  # Obat berhasil ditambahkan

    def lihatObat(self, jenisObat):
        index = self.hash_function(jenisObat)
        while self.hash_table[index] is not None:
            if self.hash_table[index][0] == jenisObat:
                return self.hash_table[index][1]
            index = (index + 1) % self.size
        return None  # Jenis obat tidak ditemukan

    def ambilObat(self, jenisObat):
        index = self.hash_function(jenisObat)
        while self.hash_table[index] is not None:
            if self.hash_table[index][0] == jenisObat:
                self.hash_table[index] = ("deleted", None)
                return True  # Obat berhasil dihapus
            index = (index + 1) % self.size
        return False  # Jenis obat tidak ditemukan

    def printAll(self):
        for index, item in enumerate(self.hash_table):
            if item is not None and item[0] != "deleted":
                print(f"Jenis obat: {item[0]}, Nama obat: {item[1]}")
