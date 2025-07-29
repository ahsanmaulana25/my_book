import streamlit as st

# Kelas Mahasiswa
class Buku:
    def __init__(self, judul, penulis, tahun_terbit):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit

    def __str__(self):
        return f"Judul: {self.judul}, Penulis: {self.penulis}, Tahun: {self.tahun_terbit}"

# Data disimpan di list session_state
if 'data_buku' not in st.session_state:
    st.session_state.data_buku = []

# Tampilan utama
#format berupa judul/bold
st.title("Aplikasi Manajemen Buku")

#format peenulisan biasa
st.write("### Pilihan Menu:")
st.write("1. Lihat Data Buku")
st.write("2. Tambah Data Buku")
st.write("3. Ubah Data Buku")
st.write("4. Hapus Data Buku")

menu = st.text_input("Masukkan angka menu (1-4):")

# Fungsi menu
if menu == "1":
    st.subheader("📄 Daftar koleksi buku")
    if st.session_state.data_buku:
        for i, book in enumerate(st.session_state.data_buku):
            st.write(f"{i+1}. {book}")
    else:
        st.info("Belum ada data.")

elif menu == "2":
    st.subheader("➕ Tambah Data Buku")
    judul = st.text_input("Masukkan Judul Buku")
    penulis = st.text_input("Masukkan Nama Penulis")
    tahun_terbit = st.text_input("Masukkan Tahun Terbit")
    if st.button("Simpan"):
        if judul and penulis and tahun_terbit:
            book = Buku(judul=judul, penulis=penulis, tahun_terbit=tahun_terbit)
            st.session_state.data_buku.append(book)
            st.success("Data berhasil ditambahkan.")
        else:
            st.warning("Harap isi semua kolom.")

elif menu == "3":
    st.subheader("✏️ Ubah Data Buku")
    data = st.session_state.data_buku
    

elif menu == "4":
    st.subheader("🗑️ Hapus Data Buku")
    

elif menu != "":
    st.warning("Masukkan angka 1 - 4 sesuai menu.")
