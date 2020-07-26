# Linear Regression from Scratch
Tugas Seleksi Ca-IRK 2018

Membuat algoritma linear regression dari 0.

## Author
Taufiq Husada Daryanto<br>
NIM: 13518058

## Deskripsi Persoalan
Seperti yang telah kalian pelajari pada mata kuliah Probabilitas dan Statistika, terdapat suatu algoritma yang bernama <b>Regresi Linier (Linear Regression)</b>. Buatlah algoritma Regresi Linear versi kalian sendiri dan cobalah memakai algoritma tersebut untuk memproses dataset!

## Dasar Teori Regresi
Regresi linear adalah suatu pendekatan yang memodelkan hubungan antara variabel terikat Y dengan satu atau lebih variabel bebas X. Sehingga, dengan menggunakan regresi linier, kita bisa memprediksi nilai variabel Y dengan menggunakan variabel X.<br>
Regresi linier memiliki persamaan sebagai berikut
$$\hat{Y} = \theta_0 + \theta_1 X_i + ... + \theta_1 X_n$$
dimana:
$$\hat{Y}$$: predicted value
n: jumlah feature nya
$$X_i$$: value dari feature nya
$$\theta_i$$: weight dari featurenya
$$\theta_0$$: bias
<br>
Untuk mencari nilai $$\theta$$ bisa dengan menggunakan normal equation sebagai berikut
<img src="https://eli.thegreenplace.net/images/math/20baabd9d33dcd26003bc44c7d81ba39e1ad4caa.png" alt="normal-equation-img">
yang pembuktiannya bisa dilihat dari artikel ini https://eli.thegreenplace.net/2014/derivation-of-the-normal-equation-for-linear-regression

## Penjelasan Kode Sumber
Implementasi class LinearRegression ada di file mylib.py <br>
cara penggunaanya sebagai berikut <br>

`from mylib import MyLinearRegression` <br>
`myLinearRegression = new MyLinearRegression()` <br>
`myLinearRegression.fit(X_train, y_train)`        # fit training dataset <br>
`myLinearRegression.predict(X_test)`              # predict test dataset <br>
