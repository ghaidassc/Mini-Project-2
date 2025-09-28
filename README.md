# Mini-Project-2

Nama : Ghaida Suci Nahiza
Nim : 2509116077
Kelas : Sistem Informasi B

Sistem Daftar Belanja Untuk Keperluan E-Commerce.
Program ini dibuat dan bisa digunakan oleh admin dan user/pengguna. Sebagai admin, kamu dapat menambahkan barang baru, mengedit jumlah barang tersedia, melihat/mengecek barang yang masih tersedia, dan menghapus barang yang ingin dihapus. sSebagai user/pengguna, kamu dapat menambahkan barang ke keranjang dan melihat barang yang tersedia.

# Flowchart
<img width="2230" height="1603" alt="flowMinpro2 fixx" src="https://github.com/user-attachments/assets/0b2947ec-e4dc-4919-b55d-891813e9b7a4" />




# Cara kerja program.
Pertama-tama, kamu akan diarahkan untuk login menggunakan username dan password. Jika kamu adalah admin, maka kamu akan masuk ke menu admin. Dan jika kamu adalah user/pengguna, maka kamu akan masuk ke menu user/pengguna.

# Menu login.
<img width="418" height="107" alt="Cuplikan layar 2025-09-28 111027" src="https://github.com/user-attachments/assets/9fb7d57f-449a-4661-9686-420e3eb6c8e3" />

<img width="449" height="112" alt="Cuplikan layar 2025-09-28 111120" src="https://github.com/user-attachments/assets/1f0d8653-507c-481c-901b-689b63430a98" />

Menu login untuk admin dan user/pengguna. jika salah memasukkan username/password, maka akan menghasilkan output login gagal dan diminta untuk memasukkan username dan password lagi. Jika sudah berhasil login, maaka akan ada output Selamat datang yang berbeda antara admin dan user/pengguna.




# Admin
Admin akan ditampilkan menu seperti dibawah ini.

<img width="548" height="197" alt="Cuplikan layar 2025-09-28 104152" src="https://github.com/user-attachments/assets/3345582e-9813-4bb1-ade7-84f3e5a11a9f" />


# Kondisi 1.
<img width="535" height="408" alt="Cuplikan layar 2025-09-28 105110" src="https://github.com/user-attachments/assets/e5e5e0c4-4e03-4476-8552-d20fc4a870a2" />

Terdapat beberapa pilihan menu. Pada kondisi pertama ini, jika admin menginput 1, maka output yang keluar adalah nama, harga, stok, dan kategori barang yang ada. Setelah itu, terdapat pilihan bahwa ingin melanjutkan dengan memilih menu lain atau tidak. Jika ya, maka admin akan diarahkan untuk memilih menu lain lagi. Dan jika tidak, maka program diselesaikan.

# Kondisi 2.
<img width="433" height="515" alt="Cuplikan layar 2025-09-28 110333" src="https://github.com/user-attachments/assets/92d9d1a6-e3ce-400d-87ff-aed971160065" />

Pada kondisi ini, admin menginput 2 pada pilihan menu. Maka admin dapat menambahkan produk. Admin dapat menginput nama barang, harga barang, stok barang, dan kategori barang. Jika sudah, maka barang yang telah ditambahkan akan masuk ke nomor barang selanjutnya. Disini ada pilihan lagi, apakah ingin melanjutkan untuk memilih menu lain lagi atau tidak? . Jika admin memilih ya, maka admin dapat memilih menu lain lagi yang tersedia. Jika tidak, maka program diselesaikan.  

# Kondisi 3.
<img width="443" height="388" alt="Cuplikan layar 2025-09-28 111824" src="https://github.com/user-attachments/assets/11db6b5c-81fc-4b30-81b6-7bb67b1c1d52" />

Pada kondisi ini, admin menginput 3 pada menu pilihan. Jika nomor barang yang dimasukkan oleh admin tersedia dalam daftar barang, maka admin dapat mengedit barang. Mulai dari nama barang, harga barang, jumlah stok, dan kategori barang. Sebaliknya, jika nomor barang yang dimasukkan tidak ada dalam daftar barang, maka akan mengasilkan input nomor barang tidak ditemukan.  Disini ada pilihan lagi, apakah ingin melanjutkan untuk memilih menu lain lagi atau tidak? . Jika admin memilih ya, maka admin dapat memilih menu lain lagi yang tersedia. Jika tidak, maka program diselesaikan. 

# Kondisi 4.
<img width="443" height="315" alt="Cuplikan layar 2025-09-28 112456" src="https://github.com/user-attachments/assets/158009d5-89f6-4190-b527-6209d3f3045c" />

Pada kondisi ini, admin menginput 4 pada menu pilihan, yaitu hapus barang. Admin akan diminta untuk memasukkan nomor barang yang ingin dihapus dari daftar. jika nomor barang tersedia, maka barang dengan nomor barang tersebut akan dihapus dari daftar barang. Sebaliknya, jika nomor barang tidak ditemukan pada daftar barang, maka akan muncul output nomor barang tidak ditemukan. Disini ada pilihan lagi, apakah ingin melanjutkan untuk memilih menu lain lagi atau tidak? . Jika admin memilih ya, maka admin dapat memilih menu lain lagi yang tersedia. Jika tidak, maka program diselesaikan. 

# Kondisi 5.
<img width="438" height="390" alt="Cuplikan layar 2025-09-28 112939" src="https://github.com/user-attachments/assets/7bb48fa4-1d18-43eb-9246-f294ee9154a6" />

Pada kondisi ini, admin menginput 5, yaitu menu logout. Maka admin akan di logoutkan dari program. Kemudian disini diberikan pilihan lagi, apakah admin ingin login lagi atau tidak. Jika admin memilih untuk login lagi, maka admin diminta untuk memasukkan username dan password kembali. Dan jika tidak, maka program diberhentikan.

# User/pengguna.
User/pengguna akan ditampilkan menu seperti dibawah ini.

<img width="410" height="188" alt="Cuplikan layar 2025-09-28 113858" src="https://github.com/user-attachments/assets/1e7d189d-b92e-4213-a55a-6843b807c5a5" />

# Kondisi 1.
<img width="450" height="294" alt="Cuplikan layar 2025-09-28 114003" src="https://github.com/user-attachments/assets/ec320234-d9e8-4576-a654-99c01317ef98" />

Pada kondisi ini, user menginput 1 pada pilihan menu. Maka output yang muncul adalah daftar barang yang tersedia. Selanjutnya, terdapat pilihan bahwa ingin melanjutkan dengan memilih menu lain atau tidak. Jika ya, maka admin akan diarahkan untuk memilih menu lain lagi. Dan jika tidak, maka program diselesaikan.

# Kondisi 2.
<img width="430" height="339" alt="Cuplikan layar 2025-09-28 114526" src="https://github.com/user-attachments/assets/714905a9-1d04-4a03-b9a3-a6ff81a0d3df" />

Setelah user melihat produk tersedia, kemudian user menginput 2 pada pilihan menu, yaitu tambah produk. Disini, user dapat menambahkan barang ke keranjang user. Selanjutnya, terdapat pilihan bahwa ingin melanjutkan dengan memilih menu lain atau tidak. Jika ya, maka admin akan diarahkan untuk memilih menu lain lagi. Dan jika tidak, maka program diselesaikan.

# Kondisi 3.
<img width="434" height="273" alt="Cuplikan layar 2025-09-28 114938" src="https://github.com/user-attachments/assets/5b531420-ae41-4661-a5c7-2db47a10fa54" />

Pada kondisi ini, user menginput 3, yaitu menu logout. Maka user akan di logoutkan dari program. Kemudian disini diberikan pilihan lagi, apakah user ingin login lagi atau tidak. Jika uder memilih untuk login lagi, maka user diminta untuk memasukkan username dan password kembali. Dan jika tidak, maka program diberhentikan.


