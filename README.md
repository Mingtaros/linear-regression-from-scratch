# Linear Regression from Scratch
Tugas Seleksi Ca-IRK 2018

Membuat algoritma linear regression dari 0.

## PENGUMPULAN

1. Nama/Nim : Aqil Abdul Aziz/13518002

2. Regresi Linier
<br>
Regresi Linier merupakan pendekatan linier pemodelan hubungan antara suatu variabel yang dependen, terhadap kumpulan variabel lain yang independen. Rumus dasar Regresi Linier berupa : 
<br>
<b>Y = C + M1X1 + M2X2 + .... + MNXN </b>
<br>
Disini, N merupakan jumlah variabel independen yang akan memengaruhi variabel dependen(Y) yang akan diprediksi, C merupakan intercept, X merupakan variabel independen, dan M merupakan weight atau koefisien regresi.
<br>
Koefisien regresi didapat dari regresi terus menerus terhadap set data yang ada, dengan melibatkan Loss Function untuk estimasi jarak antara koefisien regresi sekarang dan koefisien regresi yang lebih sesuai dengan data yang dipakai untuk regresi
<br>
Regresi linier diaplikasikan dalam finance, ekonomiks, dan merupakan salah satu fondasi machine learning

3. Penjelasan Kode <br> 
Pada linearreg.py dan linearreg.jl , terdapat class/struct yang merepresentasikan sebuah regressor yang diinitiate dengan jumlah variabel independen dan dimensi variabel dependen yang akan diprediksi. Terdapat juga method/fungsi train untuk para regressor, yang menerima sebuah data berbentuk matriks dengan dimensi yang sesuai beserta jumlah iterasi training yang akan dilakukan. Train() bisa dibilang akan meregresikan weight dan koefisien yang sudah ada terhadap data yang disediakan terus menerus sejumlah iterasi yang diinginkan oleh pemakai. Setelah training selesai, perubahan akan terlihat pada weight regressor yang sudah disesuaikan dengan data. Kode memiliki komentar sehingga bisa dibaca langsung.
<br>
Pada .ipynb adalah pemrosesan data yang ada di 'car data.csv', lalu dihantamkannya data tersebut pada regressor yang diimport dari file .jl dan .py, lalu plotting hasil prediksi data terhadap data aktual
<br>

4. Referensi
    1. NANYA ABANG (beneran ga boong)
    2. https://docs.julialang.org/




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
    
## Bonus
- Gunakan bahasa [Julia](https://julialang.org/) (.jl) (Julia juga dapat digunakan pada Jupyter Notebook)

## Panduan
Untuk mengerjakan bonus:<br>
- Julia Documentation: https://docs.julialang.org/
- Julia Cheatsheet: https://cheatsheets.quantecon.org/julia-cheatsheet.html

## Points Granted
Max Point: 2000<br>
Bonus: + 750

<br>
==================================================================<br>
<i>*Segala pertanyaan dapat ditanyakan melalui LINE Group Ca-IRK 2018 atau dapat melalui pc langsung.</i>
