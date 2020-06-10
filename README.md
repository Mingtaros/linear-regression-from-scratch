# Linear Regression from Scratch
Tugas Seleksi Ca-IRK 2018

Membuat algoritma linear regression dari 0.

## Identitas
Anna Elvira Hartoyo / 13518045

## Deskripsi Persoalan
Seperti yang telah kalian pelajari pada mata kuliah Probabilitas dan Statistika, terdapat suatu algoritma yang bernama <b>Regresi Linier (Linear Regression)</b>. Buatlah algoritma Regresi Linear versi kalian sendiri dan cobalah memakai algoritma tersebut untuk memproses dataset!

## Spesifikasi Tugas
1. Buatlah algoritma Linear Regression FROM SCRATCH
2. Program ditulis dalam bahasa <b>Python</b> dengan menggunakan kakas [Jupyter Notebook](https://jupyter.org/)


## Dasar Teori Regresi Linear
Dalam dunia statistika, regresi linear adalah pendeketan yang digunakan untuk melekukan pemodelan hubungan antara variable terikat Y dan satu atau lebih variable bebas X. Kegunaan dari regresi linear adalah melakukan prediksi berdasarkan data-data yang telah dimiliki sebelumnya.<br> 
Berdasarkan jumlah penggunaan variable bebas, regresi linear dapat dikategorikan menjadi dua, yaitu regresi linear univariate (simple linear regression) dan regresi linear multivariate (multiple linear regression). Simple lienar regression digunakan untuk mengetahui pengaruh antara **satu buah variabel bebas terhadap satu buah variabel terikat**. Sedangkan pada multiple linear regression, variable bebas yang terlibat tidak hanya satu saja melainkan **beberapa variable bebas**. Persamaan untuk memodelkan multiple linear regression sebagai berikut:<br>
<image src = "pic/f_MLR.png">
<br>


## Penjelasan Source Code
Algoritma untuk memodelkan multiple linear regression dibuat dengan bahasa Julia (.jl) dan terdapat pada file linear_regression.jl yang memuat module linearRegression.<br>
Modul ini memiliki sebuah struct regression yang terdiri atas <br>
1. xdata : data untuk variable x
2. ydata : data untuk variable y
3. num_data : banyaknya baris data
4. num_free_var : banyaknya variable bebas(x)
5. xmatrix : matrix untuk menyimpan nilai variable x
6. ymatrix : matrix untuk menyimpan nilai variable y
7. bmatrix : matrix untuk menyimpan nilai B hasil perhitungan

<br>
Modul ini juga memuat berbagai fungsi untuk melakukan perhitungan terhadap data train dan test. Untuk data train terdapat pada fungsi train yang akan dicari persamaan model regresi liear dengan menggunakan perkalian antar matriks, sehingga diperoleh nilai untuk b0, b1, b2, ... bk. Untuk melakukan prediksi data, terdapat fungsi test yang memanfaatkan hasil persamaan model sebelmunya untuk menentukan nilai y hasil prediksi dan menampilkan nilai akurasi perhitungan dalam MSE, RMSE, dan R<sup>2.


## Referensi
- Data set: https://www.kaggle.com/nehalbirla/vehicle-dataset-from-cardekho 
- Julia Documentation: https://docs.julialang.org/
- Julia Cheatsheet: https://cheatsheets.quantecon.org/julia-cheatsheet.html
- Multiple linear regression: https://slideplayer.com/slide/4238175/ and Probability & Statistics for Engineers & Scientits 9th ed., Ronald E. Walpole et al.
