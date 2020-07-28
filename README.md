# Linear Regression from Scratch
Tugas Seleksi Ca-IRK 2018
Membuat algoritma linear regression dari 0.

* Felicia Gillian Tekad Tuerah
* 13518070

## Deskripsi Persoalan
Seperti yang telah dipelajari pada mata kuliah Probabilitas dan Statistika, terdapat suatu algoritma yang bernama <b>Regresi Linier (Linear Regression)</b>. Akan dibuat sebuah algoritma Regresi Linear versi saya sendiri dan algoritma tersebut akan digunakan untuk memproses dataset!

## Library
Pada pengerjaan tugas ini, saya menggunakan beberapa library yakni 
1. **numpy** (untuk memproses operasi array)
2. **pandas** (untuk memproses dataframe)
3. **matplotlib** (untuk melakukan plotting)
4. **sklearn** (untuk memisahkan data menjadi data test dan data train)

## Dasar Teori Regresi Linier
Pada pembuatan algoritma regresi linier ini, saya menggunakan prinsip <b>Least Squares for Multiple Regression</b>. 
Diberikan sebuah persamaan linear sebagai berikut:

<img src="/img/persamaan.jpg"/>

Keterangan : 
- y : variabel tak bebas
- xi : variabel bebas
- Bi : koefisien regresi dari variabel bebas ke-i
- E : error

Persamaan linear di atas, bisa diubah menjadi persamaan matriks sebagai berikut :
<img src="/img/matriks.gif"/>

Sehingga bisa dipisah menjadi tiga buah matriks sebagai berikut:
<img src="/img/matriks2.png"/>

Dengan menggunakan rumus dan kaidah matriks diperoleh hasil dari koefisien regresi dari variabel bebas ke-i adalah sebagai berikut:

<img src="/img/rumus.png"/>

Dengan mengetahui hasil dari koefisien regresi tiap variabel bebas, maka kita bisa melakukan estimasi terhadap nilai y sesuai dengan masukan x yang merupakan variabel bebas.

## Penjelasan Kode
Kode saya terbagi atas dua buah modularitas yakni :
1. **regression.py**
Modul ini, terdiri atas tiga buah methods yang membantu dalam perhitungan koefisien regresi dan juga melakukan estimasi terhadap variabel bebas.
- multiplyMatrix digunakan untuk melakukan operasi perkalian terhadap dua buah matriks.
- koefRegression digunakan untuk mengembalikan array of koefisien (B)
- multipleLinearRegression digunakan untuk mengembalikan hasil prediksi dari masukan variabel bebas x.
2. **Regresi.ipynb**
Modul ini memanggil fungsi multipleLinearRegression yang terdapat dalam modul pertama dan menampilkan proses-proses pengolahan data-set serta menampilkan perbandingan antara data hasil estimasi dengan data sesungguhnya dan juga garis regresi linear yang terbentuk.

## Referensi

1. Data CSV yang dipakai diambil dari link [berikut](https://www.kaggle.com/nehalbirla/vehicle-dataset-from-cardekho).
2. Prinsip yang mendasari algoritma di atas dipelajari dari link [berikut](https://www.youtube.com/watch?v=qdOG7YMolmA)
