# Linear Regression from Scratch
Tugas Seleksi Ca-IRK 2018

Muhammad Ayyub Abdurrahman - 13518076 - Calon Asisten Lab IRK
Membuat algoritma linear regression dari 0.

## Deskripsi Persoalan
Seperti yang telah kalian pelajari pada mata kuliah Probabilitas dan Statistika, terdapat suatu algoritma yang bernama <b>Regresi Linier (Linear Regression)</b>. Buatlah algoritma Regresi Linear versi kalian sendiri dan cobalah memakai algoritma tersebut untuk memproses dataset!

## Spesifikasi Tugas
1. Buatlah algoritma Linear Regression FROM SCRATCH
2. Program ditulis dalam bahasa <b>Python</b> dengan menggunakan kakas [Jupyter Notebook](https://jupyter.org/)
    1. Class Linear Regression ditulis pada file Python (.py) (Jangan lupa untuk didokumentasikan dengan baik).
    2. Class Linear Regression yang dibuat tadi lalu di-<i>import</i> dan digunakan pada <i>Notebook</i> (.ipynb).
3. Program pada <i>Notebook</i> melakukan hal-hal dibawah ini:
    1. Mengambil data CSV (link ada di bawah)
    2. Memproses data mentah
    3. Melakukan <i>splitting</i> dataset (yang telah diproses) untuk <i>Train</i> dan <i>Test</i>.
    4. Memasukkan data Train ke algoritma Linear Regression yang sudah kalian buat.
    5. Melakukan prediksi terhadap data Test.
    6. Menunjukkan akurasi dari algoritma yang telah dibuat terhadap dataset yang diberikan.
    7. Memvisualisasikan hasil prediksi dengan scatter plot (untuk datanya) + line plot (untuk modelnya).

## Pengumpulan
1. Fork repository ini.
2. Tambahkan <i>source code</i> kalian.
3. Ubah README ini menjadi berisikan:
    - Nama / NIM
    - Dasar Teori Regresi Linier
    - Penjelasan singkat kode sumber
    - Referensi
4. Lakukan Pull Request dengan Format: Nama - NIM
5. <i>Personal Chat</i> Leonardo W. (kontak ada di grup Ca-IRK 2018), merundingkan jadwal demo tugas.
    - Demo berlangsung selama 15 menit.
    - Demo dilakukan di Google Meet.

## Batasan-batasan
1. Boleh menggunakan Library <b>apapun</b> asalkan bukan implementasi Linear Regression yang sudah ada (cth: Scikit-Learn).
2. Algoritma Linear Regression dapat digunakan untuk jumlah atribut berapapun (kecuali 0).
3. Algoritma Linear Regression hanya dapat menerima atribut-atribut numerik (`float` / `int`).
    - Apabila terdapat atribut non-numerik, diharapkan untuk diproses terlebih dahulu.
4. Data CSV yang dipakai dapat di-download pada link [berikut](https://www.kaggle.com/nehalbirla/vehicle-dataset-from-cardekho).
    - <b>AKAN TETAPI</b> diperbolehkan menggunakan dataset lain.
    
## Dasar Teori Regresi Linier
Multiple regression model dihasilkan apabila suatu variabel dependen (y) dipengaruhi oleh lebih dari satu variabel independen (x0, x1, ..., xk) dengan hubungan linier. Model regresi dapat ditulis sebagai berikut

Y = b0 + b1x1 + b2x2 + .. + bnxn

Dalam menentukan model regresi, variabel dapat disimpan pada matriks X untuk variabel independen dan matriks y untuk variabel dependen. Koefisien dan konstanta pada model regresi dapat ditentukan dengan mencari vektor b pada persamaan berikut

b = (invers(X'X))*(X'Y)

## Penjelasan singkat kode sumber

Kode saya ini sangat sederhana. Terdapat file linearregression sebagai pendukung utama dari program yang berisikan algoritma-algoritma penting seperti mencari nilai prediksi Y, nilai koefisien B, nilai SSE, SST dan RSquare. Terdapat juga file notebook yang menjelaskan bagaimana cara meregresi suatu data mobil yang memiliki fitur:
   1. Menambahkan Data
   2. Melakukan Splitting Data
   3. Melakukan Multiple Linear Regression beserta Kualitas Regresinya dengan R Square
   4. Melakukan Plotting hubungan antar data (soon)
   
## Referensi
1. Stackoverflow
2. https://www.youtube.com/watch?v=qdOG7YMolmA
3. https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html
4. Dosen Probstat Tercinta
