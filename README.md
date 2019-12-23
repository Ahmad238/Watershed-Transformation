# Watershed Transformation

Bentuk implementasi dari algoritma Transformasi Watershed

Ini adalah bagian kecil dari implementasi Transformasi Watershed. Dalam implementasi yang saya buat, saya membut dua Class yaitu Pixel, dan ImageGrayscale. Pixel memiliki atribut seperti nilai grayscale, label, dan list yang berisi 8-Connectivity-Neighboring-Pixels, sedangkan ImageGrayscale memiliki atribut kumpulan pixel yang berbentuk list2d. Selain itu juga, dalam Class ImageGrayscale memiliki method yang bernama watershedVS yang bertugas memberikan label pada tiap pixel berdasarkan definisi Immersion Watershed.

Program yang saya buat ini belum bisa dijalankan, karena masih harus membuat codingan dari algoritma sebelumnya dan harus menyesuaikannya.

fungsi ini diawali dengan INIT yang berarti nilai awal untuk label, kemudian variabel label yang berisi list kosong. dilanjutkan pendefinisian label[p] dengan nilai INIT, lalu mendefinisikan curent_label = 1. fifo_init(queue) --> fungsi dari algoritma sebelumnya yang harus didefinisikan terlebih dahulu. 

Berikutnya adalah langkah untuk mengubah label[p], label[p] berubah apabila nilainya sama dengan INIT, kemudian dirubah ke nilai curent_value lalu p dimasukkan ke queue. Jika queue tidak kosong, kita akan mengubah Neighbor dari nilai q kemudian, label[q] dimasukkan ke dalam queue.

Output dari fungsi ini adalah gambar yang sudah berlabel
