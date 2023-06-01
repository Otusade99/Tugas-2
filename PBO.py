class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    def tampilkan_info(self):
        print("Nama:", self.nama)
        print("NIM:", self.nim)
        print("Jurusan:", self.jurusan.NamaJurusan)


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


