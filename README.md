# Watershed-Transformation

Pengimplementasian dari algoritma Watershed Transform

Ini adalah bagian kecil dari implementasi Transformasi Immersion Watershed versi algoritma Vincent-Soille. Adapun bagian yang luput dari implementasi yang saya buat adalah, grayscale-pixels-nya tidak berdasarkan pada gambar nyata melainkan menggunakan numpy random list2d yang dianggap sebagai gambar dengan grayscale pixels.

Dalam implementasi yang saya buat, saya membut dua Class yaitu Pixel, dan ImageGrayscale. Pixel memiliki atribut seperti nilai grayscale, label, dan list yang berisi 8-Connectivity-Neighboring-Pixels, sedangkan ImageGrayscale memiliki atribut kumpulan pixel yang berbentuk list2d. Selain itu juga, dalam Class ImageGrayscale memiliki method yang bernama watershedVS yang bertugas memberikan label pada tiap pixel berdasarkan definisi Immersion Watershed.
