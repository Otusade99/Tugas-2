# Tugas-2
Nama : Ade Irawan
NPM : G1A022083
Mata Kuliah : PBO



class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    def tampilkan_info(self):
        print("Nama:", self.nama)
        print("NIM:", self.nim)
        print("Jurusan:", self.jurusan.NamaJurusan)
Penjelasan Kode :
Pada kode program di atas menampilkan class mahasiswa yang terdapat fungsi def __init__ dan di dalamnya ada nama,nim,jurusan yang akan dipanggil.
Untuk self.nama, self.nim, dan self.jurusan akan diinisiasikan dari nama,nim,jurusan. Kemudian, fungsi def tampilkan_info(self) akan memanggil nama,nim,dan jurusan
seperti penjelasan sebelumnya dan dicetak dengam method print.


class Jurusan:
    def __init__(self, nama_jurusan):
        self.NamaJurusan = nama_jurusan
        self.DaftarMahasiswa = []

    def tambah_mahasiswa(self, mahasiswa):
        self.DaftarMahasiswa.append(mahasiswa)

    def tampilkan_daftar_mahasiswa(self):
        print("Daftar Mahasiswa di Jurusan", self.NamaJurusan)
        for mahasiswa in self.DaftarMahasiswa:
            print("- Nama:", mahasiswa.nama, ", NIM:", mahasiswa.nim)
Penjelasan Kode :
Pada kode lanjutannya menampilkan class dari jurusan yang terdapat atribut nama_jurusan dan DaftarMahasiswa. 
def__init__(self, nama_jurusan) akan dipanggil saat objek Jurusan dibuat. Method ini akan menginisialisasi nama_jurusan dengan suatu niali yang akan diatmabahkan nantinya dan membuat daftar kosong dari DaftarMahasiswa
Pada bagian  self.NamaJurusan = nama_jurusan dan self.DaftarMahasiswa = [] akan menaginisialisasi NamaJurusan dengan nilai yang ditambahkan pada objek Jurusan yang sudah dibuat.
def tambah_mahasiswa(self, mahasiswa) adalah method untuk menambahakan objek Mahasiswa ke dalam objek DaftarMahasiswa yang kosong di objek Jurusan.
Kemudian self.DaftarMahasiswa.append(mahasiswa) dengan fungsi ini akan menambahkan mahasiswa ke dalam DaftarMahasiswa
def tampilkan_daftar_mahasiswa(self) method ini akan menampilkan dafatar mahasiswa pada objek jurusan
print("Daftar Mahasiswa di Jurusan", self.NamaJurusan) akan mencetak kalimat Daftar Mahasiswa di Jurusan
for mahasiswa in self.DaftarMahasiswa: melakukan iterasi atau perulangan pada setiap objek Mahasiswa dalam DaftarMahasiswa
print("- Nama:", mahasiswa.nama, ", NIM:", mahasiswa.nim) mencetak informasi nama dan nim dari mhasiswa tersebut.



class Universitas:
    def __init__(self, nama_universitas):
        self.NamaUniversitas = nama_universitas
        self.DaftarJurusan = []

    def tambah_jurusan(self, jurusan):
        self.DaftarJurusan.append(jurusan)

    def tampilkan_daftar_jurusan(self):
        print("Daftar Jurusan di Universitas", self.NamaUniversitas)
        for jurusan in self.DaftarJurusan:
            print("- Nama Jurusan:", jurusan.NamaJurusan)
  Penjelasan Kode:
  Pada lanjutan dari kode sebebelumnya, kode program ini menampilkan class Universitas
  def __init__(self, nama_universitas) method yang akan dipanggil jika objek Universitas dibuat
  self.NamaUniversitas = nama_universitas akan menganalisis NamaUniversitas dari objek Universitas
  self.DaftarJurusan = [] masih berupa daftar kosong
  def tambah_jurusan(self, jurusan): Method yang akan menambahkan objek jurusan ke DaftarJurusan
  self.DaftarJurusan.append(jurusan) Fungsi yang akan menambahkan objek jurusan ke dalam DaftarJurusan
  Kemudian, akan ditampikan dengan method   def tampilkan_daftar_jurusan(self): dan mencetak kalimat Daftar Jurusan di Universitas pada baris program berikutnya
  for jurusan in self.DaftarJurusan: akan melakukan perulangan atau iterasi pada objek jurusan dalam DaftarJurusan
  print("- Nama Jurusan:", jurusan.NamaJurusan) akan mencetak Nama jurusan
  
  
# Langkah 1
# Implementasi kelas Mahasiswa, Jurusan, dan Universitas

# Langkah 2
universitas_xyz = Universitas("XYZ University")

# Langkah 3
jurusan_ti = Jurusan("Teknik Informatika")
universitas_xyz.tambah_jurusan(jurusan_ti)

# Langkah 5
universitas_xyz.tampilkan_daftar_jurusan()

# Langkah 6
jurusan_ti.tampilkan_daftar_mahasiswa()
# Langkah 7: Masukkan daftar mahasiswa menggunakan input

# Membuat dictionary untuk menyimpan daftar mahasiswa berdasarkan jurusan
daftar_mahasiswa_per_jurusan = {}

# Minta pengguna untuk memasukkan jumlah mahasiswa yang akan ditambahkan
jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa yang akan ditambahkan: "))
Penjelasan Kode :
Untuk lanjutan kodenya 
Pada langkah 1, kelas-kelas Mahasiswa, Jurusan, dan Universitas didefinisikan dengan atribut dan metode yang sesuai.
Pada langkah 2, sebuah objek Universitas dengan nama "XYZ University" dibuat dan disimpan dalam variabel universitas_xyz.
Pada langkah 3, sebuah objek Jurusan dengan nama "Teknik Informatika" dibuat dan disimpan dalam variabel jurusan_ti. Objek ini kemudian ditambahkan ke DaftarJurusan dalam objek universitas_xyz menggunakan metode tambah_jurusan().
Pada langkah 5, metode tampilkan_daftar_jurusan() dipanggil pada objek universitas_xyz untuk menampilkan daftar jurusan yang ada di universitas tersebut.
Pada langkah 6, metode tampilkan_daftar_mahasiswa() dipanggil pada objek jurusan_ti untuk menampilkan daftar mahasiswa yang ada di jurusan "Teknik Informatika".
Pada langkah 7, program meminta pengguna untuk memasukkan jumlah mahasiswa yang akan ditambahkan



for i in range(jumlah_mahasiswa):
    print(f"\nMasukkan data untuk Mahasiswa ke-{i+1}:")
    nama = input("Nama Mahasiswa: ")
    nim = input("NIM Mahasiswa: ")
    nama_jurusan = input("Jurusan Mahasiswa: ")

    # Mengecek apakah jurusan sudah ada dalam dictionary
    if nama_jurusan in daftar_mahasiswa_per_jurusan:
        jurusan = daftar_mahasiswa_per_jurusan[nama_jurusan]
    else:
        # Jika jurusan belum ada, membuat objek Jurusan baru dan menambahkannya ke dictionary
        jurusan = Jurusan(nama_jurusan)
        daftar_mahasiswa_per_jurusan[nama_jurusan] = jurusan

    mahasiswa_baru = Mahasiswa(nama, nim, jurusan)
    jurusan.tambah_mahasiswa(mahasiswa_baru)

# Menampilkan daftar mahasiswa per jurusan
print("\nDaftar mahasiswa per jurusan:")
for nama_jurusan, jurusan in daftar_mahasiswa_per_jurusan.items():
    print("\nJurusan:", nama_jurusan)
    jurusan.tampilkan_daftar_mahasiswa()

Penjelasan Kode :
Untuk lanjutan kode nya Selanjutnya, program melakukan pengulangan sebanyak jumlah_mahasiswa yang telah ditentukan pengguna. Pada setiap iterasi, program meminta pengguna untuk memasukkan data mahasiswa seperti nama, NIM, dan jurusan.
Program memeriksa apakah jurusan yang dimasukkan sudah ada dalam daftar_mahasiswa_per_jurusan. Jika sudah ada, objek jurusan diambil dari dictionary. Jika belum ada, objek Jurusan baru dengan nama yang dimasukkan dibuat dan ditambahkan ke daftar_mahasiswa_per_jurusan.
Program membuat objek Mahasiswa baru dengan data yang dimasukkan pengguna. Objek tersebut ditambahkan ke DaftarMahasiswa di objek jurusan yang sesuai menggunakan metode tambah_mahasiswa().
Setelah selesai memasukkan semua data mahasiswa, program menampilkan daftar mahasiswa per jurusan dengan melakukan iterasi melalui setiap pasangan kunci-nilai dalam daftar_mahasiswa_per_jurusan. Untuk setiap jurusan, program mencetak judul jurusan dan memanggil metode tampilkan_daftar_mahasiswa() pada objek jurusan untuk menampilkan daftar mahasiswa di jurusan tersebut.
  

Output yang dihasilkan :
Daftar Jurusan di Universitas XYZ University
- Nama Jurusan: Teknik Informatika
Daftar Mahasiswa di Jurusan Teknik Informatika
Masukkan jumlah mahasiswa yang akan ditambahkan: 3

Masukkan data untuk Mahasiswa ke-1:
Nama Mahasiswa: Ade
NIM Mahasiswa: G1A022083
Jurusan Mahasiswa: Teknik Informatika

Masukkan data untuk Mahasiswa ke-2:
Nama Mahasiswa: Rino
NIM Mahasiswa: G1A022085
Jurusan Mahasiswa: Teknik Informatika

Masukkan data untuk Mahasiswa ke-3:
Nama Mahasiswa: Riyan
NIM Mahasiswa: G1C022049
Jurusan Mahasiswa: Teknik Mesin

Daftar mahasiswa per jurusan:

Jurusan: Teknik Informatika
Daftar Mahasiswa di Jurusan Teknik Informatika
- Nama: Ade , NIM: G1A022083
- Nama: Rino , NIM: G1A022085

Jurusan: Teknik Mesin
Daftar Mahasiswa di Jurusan Teknik Mesin
- Nama: Riyan , NIM: G1C022049

Penjelasan :
Di atas merupakan output yang dihasilkan dari kode program di atas dengan menggunakan fungsi input untuk memasukkan informasi-informasi yang diinginkan.
