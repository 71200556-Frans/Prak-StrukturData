class NodePelanggan:
    def __init__(self, namaPelanggan):
        self._namaPelanggan = namaPelanggan
     
    def getNamaPelanggan(self):
        return self._namaPelanggan
    
    def setnamaPelanggan(self, namaPelangganBaru):
        self._namaPelanggan = namaPelangganBaru
        

class Kasir:
    DEFAULT_CAPACITY = "" #isi sesuai dengan ketentuan soal
    def __init__(self): #konstruktor
       self.customers =  []
       self.capasity = 3
       
    def __len__(self): #mengembalikan ukuran Queue
        return len(self.customers)

    def is_empty(self): #mengecek apakah Queue kosong ?
        return len(self.customers) == 0

    def dequeue(self): #menghapus data paling depan (front)
        if self.is_empty():
            return None 
        customers = self.customers.pop(0)
        self.move_customers()
        return customer

    def enqueue(self, namaPelanggan): #menambah data ke list
        if len(self.customers) == self.capasity:
            self.capasity *= 2
        self.customers.append(customer)

    def resize(self, cap): #mengubah ukuran queue pada list
        self.capasity = new_capasity
        self.move_customers()

    def printAll(self): #menampilkan daftar pelanggan dalam sebuah kasir
        for customer in self.customers:
            print(customer)
        

# test case program
tempatKasir = Kasir()
tempatKasir.enqueue("Haniif")
tempatKasir.enqueue("Sindu")
tempatKasir.enqueue("Dedi")
tempatKasir.printAll()

tempatKasir.enqueue("Beatrix")
tempatKasir.printAll()

tempatKasir.dequeue()
tempatKasir.printAll()

tempatKasir.enqueue("Shalom")
tempatKasir.printAll()

tempatKasir.dequeue()
tempatKasir.printAll()

