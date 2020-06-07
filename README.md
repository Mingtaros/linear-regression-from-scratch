# Linear Regression from Scratch
Tugas Seleksi Ca-IRK 2018

Membuat algoritma linear regression dari 0.

## Deskripsi Persoalan
Seperti yang telah kalian pelajari pada mata kuliah Probabilitas dan Statistika, terdapat suatu algoritma yang bernama <b>Regresi Linier (Linear Regression)</b>. Buatlah algoritma Regresi Linear versi kalian sendiri dan cobalah memakai algoritma tersebut untuk memproses dataset!

## Nama / NIM
Yahya / 13518029

## Dasar Teori Regresi Linier
Regresi Linier yang dilakukan pada tugas ini menggunakan Multiple Linear Regression. Multiple Linear Regression akan melakukan regresi berdasarkan beberapa variable x terhadap y. Akurasi algoritma regresi linier dilakukan dengan menggunakan dua metode yaitu Mean Absolute Error(MAE) dan Root Mean Square Error(RMSE). Mean Absolute Error akan menghitung akurasi Regresi Linier yang dilakukan dengan menghitung rata rata dari nilai absolut selisih antara hasil prediksi dengan data aktual pada data test. Sedangkan, Root Mean Square Error akan menghitung akar kuadrat dari rata rata selisih hasil prediksi dengan data aktual yang dikuadratkan. 

## Penjelasan Kode Sumber
Pada tugas ini, saya menggunakan bahasa pemrograman Julia. Pada julia, tidak dapat membuat class dengan method khusus class tersebut. Oleh karena itu, akan dibuat file "regression.jl" yang mendeklarasikan modul LinearRegression. Pada modul tersebut akan dideklarasikan tipe data bentukan yang bernama Regression yang terdiri dari data sebagai data train, attribute sebagai list dari attribute pada variabel x, target sebagai variabel y yang akan di prediksi, model sebagai hasil regresi, dan dataTest sebagai data yang akan di prediksi dan di test akurasi algoritma nya. Kemudian akan dibuat setter untuk tiap property dari tipe data bentukan tersebut. 

Pada modul LinearRegression juga akan dideklarasikan beberapa fungsi terkait yang akan memudahkan perhitungan untuk training model serta prediksi seperti sumByAttribute dan sumProd. Kemudian, pada fungsi train akan melakukan multiple linear regression dan mengisi value dari hasil regresi tersebut ke property model yang ada pada tipe data bentukan. Setelah itu, terdapat fungsi predict yang akan melakukan prediksi terhadap dataTest pada tipe data bentukan, dan kemudian akan mengevaluasi akurasi dari algoritma menggunakan MAE dan RMSE. Hasil prediksi tersebut akan di return, karna selanjutnya akan dapat digunakan untuk visualisasi scatter plot dan line plot. 

## Referensi
1. Probability & Statistics for Engineers & Scientits 9th ed., Ronald E. Walpole et al.

