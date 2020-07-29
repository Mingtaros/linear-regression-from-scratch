# Linear Regression from Scratch
Tugas Seleksi Ca-IRK 2018

Membuat algoritma linear regression dari 0.

## Deskripsi Persoalan
Seperti yang telah kalian pelajari pada mata kuliah Probabilitas dan Statistika, terdapat suatu algoritma yang bernama <b>Regresi Linier (Linear Regression)</b>. Buatlah algoritma Regresi Linear versi kalian sendiri dan cobalah memakai algoritma tersebut untuk memproses dataset!

## Identitas diri
M. Irfaan Dzakiy 13518145

## Dasar Teori
Multiple regression model dihasilkan apabila suatu variabel dependen (y) dipengaruhi oleh lebih dari satu variabel independen (x0, x1, ..., xk) dengan hubungan linier. Model regresi dapat ditulis sebagai berikut

<img src=https://latex.codecogs.com/gif.latex?%5Chat%7By%7D%20%3D%20b_%7B0%7D%20&plus;%20b_%7B1%7Dx_%7B1%7D%20&plus;%20...%20&plus;%20b_%7Bk%7Dx_%7Bk%7D>

Dalam menentukan model regresi, variabel dapat disimpan pada matriks X untuk variabel independen dan matriks y untuk variabel dependen. Koefisien dan konstanta pada model regresi dapat ditentukan dengan mencari vektor b pada persamaan berikut

<img src=https://latex.codecogs.com/gif.latex?%28X%5E%7Bt%7DX%29b%20%3D%20X%5E%7Bt%7Dy>

## Penjelasan Kode
Modul linreg menyediakan fungsi dan prosedur yang dibutuhkan untuk:
- membaca data dalam bentuk file csv
- melakukan splitting data untuk train dan test (dengan pembagian 80%-29% secara default)
- melakukan multiple linear regression dengan memanfaatkan struktur data matriks
- menentukan quality of fit (RSquare) model yang dihasilkan
- melakukan visualisasi hasil regresi dalam bentuk scatter plot (actual data) dan garis regresi (predicted model) 
    
## Referensi
Walpole, R. E., Myers, R. H., Myers, S. L., & Ye, K. (1993). Probability and statistics for engineers and scientists (Vol. 5). New York: Macmillan.