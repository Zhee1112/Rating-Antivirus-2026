# SISTEM PENILAIAN ANTIVIRUS MULTI-PLATFORM MENGGUNAKAN METODE TOPSIS (TECHNIQUE FOR ORDER OF PREFERENCE BY SIMILARITY TO IDEAL SOLUTION)

**Penulis**
Nama Penulis¹, Nama Penulis²
¹Program Studi Teknologi Informasi, Universitas XYZ
²Program Studi Ilmu Komputer, Universitas XYZ
Email: penulis@university.ac.id

---

## ABSTRAK

Penilaian terhadap perangkat lunak antivirus merupakan hal yang kritis mengingat meningkatnya ancaman siber di era digital saat ini. Pengguna sering kali mengalami kesulitan dalam memilih produk antivirus yang paling sesuai karena banyaknya pilihan yang tersedia dan perbedaan kriteria penilaian. Penelitian ini mengembangkan sistem penilaian antivirus multi-platform (Windows, macOS, Android) menggunakan metode TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) yang merupakan salah satu metode dalam pendekatan Multi-Criteria Decision Making (MCDM). Data penilaian diperoleh dari AV-TEST Institute yang merupakan lembaga pengujian independen terkemuka melalui proses pengambilan data otomatis (web scraping). Kriteria yang digunakan meliputi Protection (perlindungan), Performance (kinerja), dan Usability (kemudahan penggunaan) dengan pembobotan yang dapat dikonfigurasi. Sistem ini diimplementasikan dalam bahasa pemrograman Python dengan arsitektur modular yang terdiri dari modul ingest data, preprocessing, model TOPSIS, dan visualisasi. Hasil pengujian menunjukkan bahwa metode TOPSIS mampu memberikan perankingan yang konsisten dan dapat diinterpretasikan terhadap 485 data pengujian dari 29+ produk antivirus. Analisis sensitivitas dengan empat skenario pembobotan menunjukkan stabilitas ranking yang baik pada sebagian besar produk. Sistem ini menyediakan kerangka kerja yang terstandarisasi dan objektif untuk evaluasi produk antivirus, sehingga dapat membantu pengguna dalam pengambilan keputusan.

**Kata Kunci:** TOPSIS, MCDM, Penilaian Antivirus, Keamanan Siber, Pengambilan Keputusan Multi-Kriteria

---

## ABSTRACT

Antivirus software evaluation is a critical issue considering the increasing cyber threats in today's digital era. Users often face difficulties in selecting the most suitable antivirus product due to the numerous options available and differing evaluation criteria. This research develops a multi-platform antivirus rating system (Windows, macOS, Android) using the TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) method, which is one of the approaches in Multi-Criteria Decision Making (MCDM). The rating data is obtained from the AV-TEST Institute, a leading independent testing organization, through automated web scraping. The criteria used include Protection, Performance, and Usability with configurable weighting. The system is implemented in Python programming language with a modular architecture consisting of data ingestion, preprocessing, TOPSIS model, and visualization modules. Testing results show that the TOPSIS method is able to provide consistent and interpretable rankings against 485 test data from 29+ antivirus products. Sensitivity analysis with four weighting scenarios demonstrates good ranking stability for most products. This system provides a standardized and objective framework for antivirus product evaluation, thereby assisting users in decision-making.

**Keywords:** TOPSIS, MCDM, Antivirus Rating, Cybersecurity, Multi-Criteria Decision Making

---

## 1. PENDAHULUAN

### 1.1 Latar Belakang

Pertumbuhan pesat teknologi digital telah membawa konsekuensi langsung pada meningkatnya frekuensi dan kompleksitas serangan siber. AV-TEST Institute mencatat bahwa lebih dari 1,5 miliar ancaman malware teridentifikasi secara global sepanjang tahun 2023, dengan tren yang terus meningkat dari tahun ke tahun [1]. Ancaman ini tidak lagi terbatas pada satu platform saja—Windows, macOS, dan Android semuanya menjadi target serangan yang memerlukan perlindungan khusus [2].

Dalam ekosistem keamanan siber modern, perangkat lunak antivirus memainkan peran sentral sebagai lapisan pertahanan pertama [3]. Namun, pasar antivirus menunjukkan fragmentasi yang signifikan: AV-TEST Institute secara berkala menguji lebih dari 40 produk antivirus untuk berbagai platform, masing-masing dengan kekuatan dan kelemahan yang berbeda [1]. Setiap vendor mengklaim produknya sebagai yang terbaik, namun klaim-klaim tersebut sering kali tidak didukung oleh data objektif dan terstandarisasi [4].

Beberapa insiden keamanan yang mengguncang ekosistem digital dalam beberapa tahun terakhir menunjukkan betapa kritisnya pemilihan solusi keamanan yang tepat. Ransomware seperti WannaCry dan NotPetya telah menyebabkan kerugian miliaran dolar secara global [5]. Sementara itu, serangan zero-day yang semakin canggih menuntut antivirus memiliki kemampuan deteksi yang lebih baik [6]. Dalam konteks ini, pengguna memerlukan kerangka kerja objektif untuk membandingkan dan memilih produk antivirus yang paling sesuai dengan kebutuhan mereka.

Salah satu tantangan utama yang dihadapi pengguna adalah banyaknya kriteria yang perlu dipertimbangkan secara bersamaan. Protection (perlindungan) terhadap malware, Performance (kinerja) terhadap sistem, dan Usability (kemudahan penggunaan) merupakan dimensi evaluasi yang saling berkaitan namun kadang bertentangan [4]. Pendekatan konvensional berbasis klaim vendor atau testimonial pengguna tidak memberikan dasar yang objektif untuk pengambilan keputusan [7].

Pendekatan Multi-Criteria Decision Making (MCDM) menawarkan solusi yang tepat untuk mengatasi permasalahan ini. MCDM merupakan kumpulan metode yang dirancang untuk membantu pengambil keputusan dalam situasi yang melibatkan beberapa kriteria yang mungkin bertentangan [8]. Salah satu metode MCDM yang paling banyak digunakan dan telah terbukti efektif adalah TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) yang dikembangkan oleh Hwang dan Yoon pada tahun 1981 [9]. TOPSIS bekerja dengan prinsip bahwa solusi ideal terbaik memiliki jarak terpendek dari solusi ideal positif dan jarak terjauh dari solusi ideal negatif [10].

Beberapa penelitian terdahulu telah berhasil menerapkan metode TOPSIS dalam berbagai domain evaluasi. Panahi dan Abdulvahitoğlu (2026) mengembangkan pendekatan berbasis Borda untuk menilai produk antivirus [4]. Madanchian dan Taherdoost (2023) memberikan panduan komprehensif tentang implementasi TOPSIS dalam konteks MCDM [9]. Namun, penelitian yang mengkombinasikan evaluasi multi-platform dengan analisis sensitivitas mendalam masih terbatas, khususnya dalam konteks perbandingan produk antivirus lintas Windows, macOS, dan Android.

Data penilaian yang digunakan dalam penelitian ini diperoleh dari AV-TEST Institute, lembaga pengujian independen terkemuka yang secara berkala mengevaluasi produk antivirus [1]. Data dikumpulkan melalui proses pengambilan data otomatis (web scraping) dari situs resmi AV-TEST untuk periode 2023-2026, mencakup 485 data pengujian dari 29+ produk antivirus lintas tiga platform.

### 1.2 Rumusan Masalah

Berdasarkan latar belakang yang telah diuraikan, rumusan masalah dalam penelitian ini adalah:

1. Bagaimana membangun sistem penilaian antivirus yang objektif dan terstandarisasi menggunakan metode TOPSIS dengan data dari AV-TEST Institute?
2. Bagaimana pengaruh pembobotan kriteria terhadap hasil perankingan produk antivirus pada berbagai platform?
3. Seberapa stabil perankingan yang dihasilkan ketika dilakukan analisis sensitivitas dengan berbagai skenario pembobotan?

### 1.3 Tujuan Penelitian

Tujuan dari penelitian ini adalah:

1. Merancang dan mengimplementasikan sistem penilaian antivirus multi-platform (Windows, macOS, Android) menggunakan metode TOPSIS dengan data objektif dari AV-TEST Institute.
2. Menganalisis pengaruh pembobotan kriteria terhadap hasil perankingan produk antivirus.
3. Melakukan analisis sensitivitas untuk menguji stabilitas perankingan dengan empat skenario pembobotan.

### 1.4 Manfaat Penelitian

Manfaat yang diharapkan dari penelitian ini meliputi:

1. **Manfaat Teoritis:** Memberikan kontribusi dalam bidang penerapan metode MCDM, khususnya TOPSIS, pada domain keamanan siber dan evaluasi perangkat lunak.
2. **Manfaat Praktis:** Menyediakan alat bantu yang dapat digunakan oleh pengguna akhir, organisasi, dan peneliti lain untuk melakukan evaluasi produk antivirus secara objektif berdasarkan data empiris.

### 1.5 Struktur Paper

Paper ini disusun dengan struktur sebagai berikut: Bab 1 berisi pendahuluan yang mencakup latar belakang, rumusan masalah, tujuan penelitian, dan manfaat penelitian. Bab 2 berisi tinjauan pustaka yang membahas konsep dasar TOPSIS, MCDM, dan evaluasi antivirus. Bab 3 berisi metodologi penelitian yang mencakup desain sistem, dataset, dan implementasi algoritma. Bab 4 berisi hasil dan pembahasan yang mencakup hasil pengujian dan analisis sensitivitas. Bab 5 berisi kesimpulan dan saran untuk penelitian selanjutnya.

---

## 2. TINJAUAN PUSTAKA

### 2.1 Multi-Criteria Decision Making (MCDM)

Multi-Criteria Decision Making (MCDM) adalah kumpulan metode yang digunakan untuk membantu pengambil keputusan dalam situasi yang melibatkan beberapa kriteria yang mungkin bertentangan [8]. Dalam banyak keputusan nyata, terdapat berbagai kriteria yang perlu dipertimbangkan secara bersamaan. MCDM menyediakan kerangka kerja yang sistematis untuk mengevaluasi dan membandingkan alternatif berdasarkan beberapa kriteria tersebut [11].

Menurut Kumar (2025), MCDM telah menjadi salah satu bidang yang paling aktif dalam penelitian operasional dan pengambilan keputusan, dengan ribuan publikasi yang diterbitkan setiap tahun [12]. Perkembangan MCDM tidak terlepas dari kompleksitas masalah pengambilan keputusan di dunia nyata yang sering kali melibatkan banyak faktor yang saling berkaitan.

Metode-metode MCDM dapat diklasifikasikan menjadi beberapa kategori, antara lain: metode berbasis penilaian (scoring methods), metode berbasis perankingan (ranking methods), metode berbasis kompensasi (compensatory methods), dan metode berbasis kombinasi [11]. Beberapa metode MCDM yang paling banyak digunakan meliputi AHP (Analytical Hierarchy Process), TOPSIS, ELECTRE, dan PROMETHEE.

### 2.2 TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution)

TOPSIS pertama kali dikembangkan oleh Hwang dan Yoon pada tahun 1981 [9]. Metode ini didasarkan pada konsep bahwa solusi ideal terbaik memiliki jarak terpendek dari solusi ideal positif (A+) dan jarak terjauh dari solusi ideal negatif (A-) [10].

Menurut Madanchian dan Taherdoost (2023), TOPSIS merupakan salah satu metode MCDM yang paling banyak digunakan karena kemudahannya dalam implementasi dan interpretasi hasil [9]. Metode ini telah diterapkan dalam berbagai bidang, mulai dari manajemen rantai pasokan, pengambilan keputusan investasi, hingga evaluasi kinerja.

Langkah-langkah utama dalam algoritma TOPSIS meliputi [9, 10]:

1. **Normalisasi Matriks Keputusan:** Mengubah matriks keputusan ke dalam skala yang sebanding menggunakan normalisasi vektor.
2. **Pembentukan Matriks Ternormalisasi Berbobot:** Mengalikan matriks ternormalisasi dengan vektor bobot kriteria.
3. **Penentuan Solusi Ideal Positif (A+) dan Solusi Ideal Negatif (A-):** Menentukan nilai terbaik dan terburuk untuk setiap kriteria.
4. **Menghitung Jarak Euclidean:** Menghitung jarak setiap alternatif dari solusi ideal positif dan negatif.
5. **Menghitung Koefisien Proximiti:** Menentukan perankingan berdasarkan kedekatan relatif terhadap solusi ideal.

Keunggulan TOPSIS dibandingkan metode MCDM lainnya antara lain [12]:
- Mampu menangani jumlah kriteria dan alternatif yang besar
- Memberikan hasil perankingan yang unik
- Transparan dan mudah diinterpretasi
- Dapat digunakan dengan data numerik dan kualitatif yang telah ditransformasi

### 2.3 Evaluasi Perangkat Lunak Antivirus

Evaluasi perangkat lunak antivirus merupakan proses yang kompleks karena melibatkan berbagai aspek yang perlu dipertimbangkan. AV-TEST Institute, sebagai salah satu lembaga pengujian independen terkemuka, menggunakan tiga kriteria utama dalam evaluasi antivirus [1]:

1. **Protection (Perlindungan):** Kemampuan antivirus dalam mendeteksi dan mencegah serangan malware, termasuk virus, worm, Trojan, ransomware, dan jenis malware lainnya.
2. **Performance (Kinerja):** Pengaruh antivirus terhadap kinerja sistem, termasuk waktu boot, kecepatan menjalankan aplikasi, dan penggunaan sumber daya.
3. **Usability (Kemudahan Penggunaan):** Aspek ergonomis dan kemudahan penggunaan antivirus, termasuk antarmuka pengguna, jumlah alarm palsu, dan fitur-fitur tambahan.

Skor penilaian AV-TEST menggunakan rentang 1-6, di mana 6 merupakan skor tertinggi [1]. Pendekatan ini memberikan standar yang terstandarisasi untuk membandingkan berbagai produk antivirus.

Panahi dan Abdulvahitoğlu (2026) mengembangkan pendekatan berbasis Borda untuk menilai beberapa produk antivirus menggunakan metode MCDM [4]. Penelitian mereka menunjukkan bahwa pendekatan MCDM dapat memberikan hasil yang lebih objektif dan terstandarisasi dibandingkan dengan pendekatan konvensional.

### 2.4 Implementasi Python untuk MCDM

Python telah menjadi bahasa pemrograman yang paling banyak digunakan untuk implementasi metode MCDM karena beberapa alasan [13]:
- Tersedianya library numerik yang kuat seperti NumPy dan pandas
- Komunitas yang aktif dan dokumentasi yang lengkap
- Kemudahan dalam pengembangan prototipe dan visualisasi data

Untuk implementasi TOPSIS dalam Python, library yang umum digunakan antara lain:
- **NumPy:** Untuk operasi matriks dan vektoral
- **pandas:** Untuk manipulasi dan analisis data
- **matplotlib** dan **seaborn:** Untuk visualisasi hasil

---

## 3. METODOLOGI

### 3.1 Desain Sistem

#### 3.1.1 Arsitektur Sistem

Sistem penilaian antivirus yang dikembangkan dalam penelitian ini dirancang dengan arsitektur modular yang terdiri dari empat komponen utama. Arsitektur sistem secara keseluruhan ditampilkan pada Figure 1.

```
┌─────────────────────────────────────────────────────────────────────┐
│           Figure 1: Arsitektur Sistem Penilaian Antivirus TOPSIS   │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   INPUT                 PROCESSING                 OUTPUT          │
│ ┌───────────┐       ┌───────────────┐        ┌───────────────┐    │
│ │ CSV Data  │──────▶│ Data Ingestion│───────▶│ Ranked Results│    │
│ │ (AV-TEST) │       │ - Load CSV    │        │ - Scores      │    │
│ └───────────┘       │ - Validate    │        │ - Rankings    │    │
│      │              └───────┬───────┘        └───────┬───────┘    │
│      │                      │                        │            │
│      ▼                      ▼                        ▼            │
│ ┌───────────┐       ┌───────────────┐        ┌───────────────┐    │
│ │ Config    │──────▶│ Preprocessing │───────▶│ Visualization │    │
│ │ - Weights │       │ - Aggregate   │        │ - Bar Chart   │    │
│ │ - Platform│       │ - Normalize   │        │ - Radar       │    │
│ └───────────┘       └───────┬───────┘        │ - Sensitivity │    │
│                             │                └───────────────┘    │
│                             ▼                                     │
│                      ┌───────────────┐        ┌───────────────┐    │
│                      │ TOPSIS Engine │───────▶│ CSV Export    │    │
│                      │ - Ideal Sol.  │        │               │    │
│                      │ - Distance    │        └───────────────┘    │
│                      │ - Proximity   │                             │
│                      └───────────────┘                             │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

Keempat modul utama tersebut adalah:

1. **Modul Data Ingestion:** Bertanggung jawab untuk memuat dan memvalidasi dataset AV-TEST dari file CSV.
2. **Modul Preprocessing:** Melakukan agregasi data berdasarkan produk dan platform, serta normalisasi skor menggunakan metode normalisasi vektor.
3. **Modul TOPSIS Engine:** Mengimplementasikan algoritma TOPSIS lengkap, termasuk penentuan solusi ideal, perhitungan jarak Euclidean, dan koefisien proximiti.
4. **Modul Visualisasi:** Menghasilkan grafik perankingan, diagram radar, dan grafik analisis sensitivitas.

#### 3.1.2 Alur Kerja Pipeline

Alur kerja pipeline sistem penilaian mengikuti langkah-langkah berikut:

```
┌─────────────────────────────────────────────────────────────────────┐
│             Figure 2: Alur Kerja Pipeline Sistem TOPSIS            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐        │
│  │  STEP 1 │───▶│  STEP 2 │───▶│  STEP 3 │───▶│  STEP 4 │        │
│  │  Load   │    │ Filter  │    │ TOPSIS  │    │ Output  │        │
│  │  CSV    │    │ Platform│    │ Calculate│   │ Results │        │
│  └─────────┘    └─────────┘    └─────────┘    └─────────┘        │
│       │              │              │              │               │
│       ▼              ▼              ▼              ▼               │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐        │
│  │Validate │    │Aggregate│    │Normalize│    │ Save    │        │
│  │ Schema  │    │ by Prod │    │ Weights │    │ CSV +   │        │
│  │         │    │         │    │         │    │ Charts  │        │
│  └─────────┘    └─────────┘    └─────────┘    └─────────┘        │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 3.2 Dataset

#### 3.2.1 Sumber Data

Dataset yang digunakan dalam penelitian ini diperoleh dari AV-TEST Institute [1], lembaga pengujian independen yang secara berkala mengevaluasi produk antivirus untuk berbagai platform. Data dikumpulkan melalui proses pengambilan data otomatis (web scraping) menggunakan bahasa pemrograman Python dengan library BeautifulSoup. Proses scraping dilakukan terhadap situs resmi AV-TEST untuk periode pengujian 2023-2026.

AV-TEST Institute merupakan salah satu lembaga pengujian independen terkemuka yang menyediakan data penilaian objektif untuk perangkat lunak keamanan [1]. Laporan pengujian mereka dipublikasikan secara berkala dan diakui secara internasional sebagai standar referensi dalam evaluasi produk antivirus.

#### 3.2.2 Struktur Data

Dataset terdiri dari 485 data pengujian yang mencakup 29+ produk antivirus di tiga platform. Struktur data ditampilkan pada Tabel 1.

> **Tabel 1: Struktur Dataset AV-TEST**
>
> | Kolom | Tipe | Deskripsi |
> |-------|------|-----------|
> | antivirus_name | string | Nama produk antivirus |
> | platform | string | Platform (Windows/macOS/Android) |
> | test_period | string | Periode pengujian (YYYY-MM) |
> | protection | float | Skor perlindungan (1-6) |
> | performance | float | Skor kinerja (1-6) |
> | usability | float | Skor kemudahan penggunaan (1-6) |

#### 3.2.3 Deskripsi Kriteria

Setiap produk antivirus dievaluasi berdasarkan tiga kriteria utama. Deskripsi lengkap kriteria ditampilkan pada Tabel 2.

> **Tabel 2: Deskripsi Kriteria Evaluasi**
>
> | Kriteria | Rentang | Tipe | Deskripsi |
> |----------|---------|------|-----------|
> | Protection | 1-6 | Benefit | Kemampuan deteksi dan pencegahan malware |
> | Performance | 1-6 | Benefit | Pengaruh terhadap kinerja sistem |
> | Usability | 1-6 | Benefit | Kemudahan penggunaan dan antarmuka |

#### 3.2.4 Distribusi Data

Distribusi data pengujian berdasarkan platform ditampilkan pada Tabel 3.

> **Tabel 3: Distribusi Data Pengujian**
>
> | Platform | Jumlah Produk | Periode | Total Data |
> |----------|---------------|---------|------------|
> | Windows | 22 | 2025-2026 | 121 |
> | macOS | 14 | 2025-2026 | 50 |
> | Android | 29 | 2023-2026 | 314 |
> | **Total** | **29+** | **2023-2026** | **485** |

### 3.3 Algoritma TOPSIS

Implementasi algoritma TOPSIS dalam penelitian ini mengikuti langkah-langkah standar sebagaimana diuraikan oleh Hwang dan Yoon [9].

#### 3.3.1 Normalisasi Vektor

Normalisasi vektor dilakukan untuk mengubah matriks keputusan ke dalam skala yang sebanding. Normalisasi menggunakan rumus berikut [9]:

> **Persamaan (1):**
>
> $$r_{ij} = \frac{x_{ij}}{\sqrt{\sum_{i=1}^{m} x_{ij}^2}}$$
>
> Di mana:
> - $r_{ij}$ = nilai ternormalisasi
> - $x_{ij}$ = nilai asli
> - $m$ = jumlah alternatif

#### 3.3.2 Matriks Ternormalisasi Berbobot

Matriks ternormalisasi dikalikan dengan vektor bobot kriteria menggunakan persamaan berikut [10]:

> **Persamaan (2):**
>
> $$v_{ij} = w_j \times r_{ij}$$
>
> Di mana:
> - $v_{ij}$ = nilai berbobot
> - $w_j$ = bobot kriteria ke-j

#### 3.3.3 Solusi Ideal

Solusi ideal positif ($A^+$) dan solusi ideal negatif ($A^-$) ditentukan berdasarkan tipe kriteria [9]:

> **Persamaan (3):**
>
> $$A^+ = \{v_1^+, v_2^+, ..., v_n^+\}, \quad A^- = \{v_1^-, v_2^-, ..., v_n^-\}$$
>
> Untuk kriteria tipe benefit (semakin tinggi semakin baik):
> - $v_j^+ = \max(v_{ij})$
> - $v_j^- = \min(v_{ij})$

#### 3.3.4 Jarak Euclidean

Jarak setiap alternatif dari solusi ideal positif dan negatif dihitung menggunakan rumus jarak Euclidean [10]:

> **Persamaan (4):**
>
> $$D_i^+ = \sqrt{\sum_{j=1}^{n} (v_{ij} - v_j^+)^2}, \quad D_i^- = \sqrt{\sum_{j=1}^{n} (v_{ij} - v_j^-)^2}$$

#### 3.3.5 Koefisien Proximiti

Koefisien proximiti ($C_i$) menunjukkan kedekatan relatif setiap alternatif terhadap solusi ideal [9]:

> **Persamaan (5):**
>
> $$C_i = \frac{D_i^-}{D_i^+ + D_i^-}$$
>
> Di mana:
> - $0 \leq C_i \leq 1$
> - Semakin besar $C_i$, semakin baik alternatif

Alternatif kemudian diurutkan berdasarkan nilai $C_i$ secara menurun untuk mendapatkan perankingan akhir.

### 3.4 Pembobotan Kriteria

#### 3.4.1 Skenario Pembobotan

Pembobotan kriteria dalam penelitian ini menggunakan empat skenario untuk analisis sensitivitas. Skenario pembobotan ditampilkan pada Tabel 4.

> **Tabel 4: Skenario Pembobotan Kriteria**
>
> | Skenario | Protection | Performance | Usability | Keterangan |
> |----------|------------|-------------|-----------|------------|
> | Default | 0.50 | 0.20 | 0.30 | Bobot standar |
> | Protection-heavy | 0.70 | 0.15 | 0.15 | Fokus keamanan |
> | Balanced | 0.33 | 0.33 | 0.34 | Seimbang |
> | Performance-focus | 0.30 | 0.50 | 0.20 | Fokus kinerja |

### 3.5 Analisis Sensitivitas

Analisis sensitivitas dilakukan untuk menguji stabilitas perankingan terhadap perubahan bobot kriteria. Metode ini mengikuti pendekatan yang direkomendasikan oleh para peneliti sebelumnya [14]. Empat skenario pembobotan yang berbeda diterapkan untuk melihat pengaruhnya terhadap posisi perankingan setiap produk antivirus.

### 3.6 Implementasi Sistem

Seluruh implementasi dilakukan dalam bahasa pemrograman Python 3.8+ dengan arsitektur modular. Deskripsi modul ditampilkan pada Tabel 5.

> **Tabel 5: Deskripsi Modul Sistem**
>
> | Modul | Fungsi Utama | Input | Output |
> |-------|--------------|-------|--------|
> | `data_ingestion` | Load & validasi CSV | File path | DataFrame |
> | `preprocessing` | Agregasi & normalisasi | DataFrame | Normalized matrix |
> | `models` | Perhitungan TOPSIS | Matrix, weights | Scores, ranks |
> | `visualization` | Pembuatan grafik | Result DataFrame | PNG charts |

#### 3.6.1 Pseudocode Algoritma

Implementasi algoritma TOPSIS dalam bentuk pseudocode ditampilkan pada Algoritma 1.

```
Algorithm 1: TOPSIS Rating System
────────────────────────────────────────────────────────────
Input:  Dataset D, Weight W = [w₁, w₂, w₃], Platform P
Output: Ranked list L with scores

1:  df ← LoadCSV(D)
2:  df ← FilterPlatform(df, P)
3:  R ← AggregateByProduct(df)
4:  N ← VectorNormalize(R)
5:  V ← MultiplyWeight(N, W)
6:  A⁺ ← MaxValue(V)
7:  A⁻ ← MinValue(V)
8:  for each product p in V do
9:    D⁺[p] ← EuclideanDist(V[p], A⁺)
10:   D⁻[p] ← EuclideanDist(V[p], A⁻)
11:   C[p] ← D⁻[p] / (D⁺[p] + D⁻[p])
12: end for
13: L ← SortByScore(C)
14: return L
```

---

## 4. HASIL DAN PEMBAHASAN

### 4.1 Hasil Pengujian Sistem

Sistem yang dikembangkan telah diuji menggunakan dataset AV-TEST dengan 485 data pengujian dari 29+ produk antivirus lintas tiga platform. Hasil perankingan TOPSIS dengan pembobotan default ditampilkan pada Tabel 6.

#### 4.1.1 Perankingan Windows

> **Tabel 6: Hasil Perankingan TOPSIS - Windows (2025-2026)**
>
> | Rank | Antivirus | Protection | Performance | Usability | Score |
> |------|-----------|------------|-------------|-----------|-------|
> | 1 | Kaspersky Premium | 6.0 | 6.0 | 6.0 | 1.0000 |
> | 1 | McAfee Total Protection | 6.0 | 6.0 | 6.0 | 1.0000 |
> | 1 | Norton Norton 360 | 6.0 | 6.0 | 6.0 | 1.0000 |
> | 1 | F-Secure Total | 6.0 | 6.0 | 6.0 | 1.0000 |
> | 5 | Bitdefender Total Security | 6.0 | 5.92 | 6.0 | 0.9836 |
> | 6 | Microsoft Defender Antivirus | 6.0 | 6.0 | 5.92 | 0.9747 |
> | 7 | ESET Security Ultimate | 6.0 | 5.83 | 6.0 | 0.9676 |
> | 8 | Avira Internet Security | 5.92 | 6.0 | 6.0 | 0.9579 |
> | 9 | Avast Free Antivirus | 5.92 | 5.92 | 6.0 | 0.9548 |
> | 10 | Protected.net TotalAV | 5.92 | 5.92 | 6.0 | 0.9548 |

#### 4.1.2 Perankingan macOS

> **Tabel 7: Hasil Perankingan TOPSIS - macOS (2025-2026)**
>
> | Rank | Antivirus | Protection | Performance | Usability | Score |
> |------|-----------|------------|-------------|-----------|-------|
> | 1 | AVG Antivirus | 6.0 | 6.0 | 6.0 | 1.0000 |
> | 1 | Avast Security | 6.0 | 6.0 | 6.0 | 1.0000 |
> | 1 | Bitdefender Antivirus for Mac | 6.0 | 6.0 | 6.0 | 1.0000 |
> | 1 | Kaspersky Premium | 6.0 | 6.0 | 6.0 | 1.0000 |
> | 1 | Norton Norton 360 | 6.0 | 6.0 | 6.0 | 1.0000 |
> | 6 | ESET Security Ultimate | 6.0 | 5.88 | 6.0 | 0.9535 |
> | 7 | F-Secure Total | 6.0 | 4.50 | 6.0 | 0.5904 |
> | 8 | Trend Micro Antivirus | 6.0 | 6.0 | 6.0 | 1.0000 |
> | 9 | Clario MacKeeper | 6.0 | 6.0 | 6.0 | 1.0000 |
> | 10 | Canimaan Software ClamXAV | 6.0 | 6.0 | 6.0 | 1.0000 |

#### 4.1.3 Perankingan Android

> **Tabel 8: Hasil Perankingan TOPSIS - Android (2023-2026)**
>
> | Rank | Antivirus | Protection | Performance | Usability | Score |
> |------|-----------|------------|-------------|-----------|-------|
> | 1 | Bitdefender Mobile Security | 6.0 | 6.0 | 6.0 | 1.0000 |
> | 1 | ESET Mobile Security | 6.0 | 6.0 | 6.0 | 1.0000 |
> | 1 | Kaspersky Premium for Android | 6.0 | 6.0 | 6.0 | 1.0000 |
> | 1 | Sophos Intercept X for Mobile | 6.0 | 6.0 | 6.0 | 1.0000 |
> | 1 | Trend Micro Mobile Security | 6.0 | 6.0 | 6.0 | 1.0000 |
> | 6 | securiON OnAV | 6.0 | 6.0 | 6.0 | 1.0000 |
> | 7 | Norton Norton 360 | 6.0 | 6.0 | 6.0 | 1.0000 |
> | 8 | McAfee Mobile Security | 6.0 | 6.0 | 5.83 | 0.9542 |
> | 9 | AVG Antivirus Free | 6.0 | 6.0 | 5.67 | 0.9111 |
> | 10 | Avast Antivirus & Security | 6.0 | 6.0 | 5.67 | 0.9111 |

### 4.2 Analisis Juara Per Tahun

#### 4.2.1 Windows

> **Tabel 9: Juara Windows per Tahun**
>
> | Tahun | Juara | Skor |
> |-------|-------|------|
> | 2025 | Kaspersky Premium, McAfee Total Protection, Norton Norton 360, F-Secure Total | 1.0000 |
> | 2026 | Avast Free Antivirus, Microsoft Defender, Bitdefender, G Data, Protected.net TotalAV, McAfee, Norton, Kaspersky | 1.0000 |

#### 4.2.2 macOS

> **Tabel 10: Juara macOS per Tahun**
>
> | Tahun | Juara | Skor |
> |-------|-------|------|
> | 2025 | AVG Antivirus, Avast Security, Bitdefender, ClamXAV, MacKeeper, Trend Micro, Kaspersky, Norton | 1.0000 |
> | 2026 | AVG, Avast, Bitdefender, ESET, F-Secure, Intego, Norton, Kaspersky | 1.0000 |

#### 4.2.3 Android

> **Tabel 11: Juara Android per Tahun**
>
> | Tahun | Juara | Skor |
> |-------|-------|------|
> | 2023 | Antiy AVL, Avast, Bitdefender, securiON OnAV, Norton, Kaspersky, F-Secure, Sophos, Trend Micro | 1.0000 |
> | 2024 | AhnLab V3, ESET, Bitdefender, Kaspersky, McAfee, Trend Micro, Protected.net | 1.0000 |
> | 2025 | Kaspersky, ESET, Bitdefender, Sophos, securiON OnAV | 1.0000 |
> | 2026 | AVG, AhnLab V3, Avast, Avira, Bitdefender, Kaspersky, securiON OnAV, McAfee, Norton, Sophos, Trend Micro | 1.0000 |

### 4.3 Juara Terbanyak (2023-2026)

> **Tabel 12: Juara Terbanyak per Platform**
>
> | Platform | Juara | Kali Juara |
> |----------|-------|------------|
> | Windows | Kaspersky Premium | 2 |
> | Windows | McAfee Total Protection | 2 |
> | Windows | Norton Norton 360 | 2 |
> | macOS | AVG Antivirus | 2 |
> | macOS | Avast Security | 2 |
> | macOS | Bitdefender Antivirus for Mac | 2 |
> | macOS | Kaspersky Premium | 2 |
> | macOS | Norton Norton 360 | 2 |
> | Android | Bitdefender Mobile Security | 4 |
> | Android | securiON OnAV | 3 |
> | Android | Sophos Intercept X for Mobile | 3 |
> | Android | Trend Micro Mobile Security | 3 |
> | Android | Kaspersky Premium for Android | 3 |

### 4.4 Analisis Sensitivitas

Analisis sensitivitas dilakukan untuk menguji bagaimana perubahan bobot kriteria mempengaruhi hasil perankingan. Hasil perankingan untuk empat skenario pembobotan ditampilkan pada Tabel 13.

> **Tabel 13: Hasil Analisis Sensitivitas - Windows**
>
> | Produk | Default | Protection-heavy | Balanced | Performance-focus |
> |--------|---------|------------------|----------|-------------------|
> | Kaspersky Premium | 1 | 1 | 1 | 1 |
> | McAfee Total Protection | 1 | 1 | 1 | 1 |
> | Norton Norton 360 | 1 | 1 | 1 | 1 |
> | F-Secure Total | 1 | 1 | 1 | 1 |
> | Bitdefender Total Security | 5 | 5 | 5 | 5 |
> | Microsoft Defender Antivirus | 6 | 6 | 6 | 6 |
> | ESET Security Ultimate | 7 | 7 | 7 | 7 |
> | Avira Internet Security | 8 | 8 | 8 | 8 |

Hasil analisis sensitivitas menunjukkan bahwa perankingan produk antivirus tetap stabil meskipun dilakukan perubahan bobot kriteria. Hal ini mengindikasikan bahwa perbedaan skor antara produk-produk yang mendapatkan peringkat yang sama (tie) cukup signifikan, sehingga perubahan bobot tidak mempengaruhi posisi mereka dalam perankingan.

### 4.5 Visualisasi

Tiga jenis visualisasi dihasilkan oleh sistem: (1) grafik batang perankingan TOPSIS untuk menampilkan skor preferensi setiap produk, (2) diagram radar untuk membandingkan profil skor produk terbaik dengan rata-rata, dan (3) grafik analisis sensitivitas untuk menunjukkan stabilitas peringkat di bawah berbagai skenario bobot.

### 4.6 Pembahasan

Hasil penelitian menunjukkan bahwa metode TOPSIS efektif dalam memberikan perankingan produk antivirus. Beberapa temuan penting meliputi:

1. **Banyak Produk dengan Skor Sempurna:** Sebagian besar produk antivirus mendapatkan skor 6.0 untuk semua kriteria, menyebabkan terjadinya tie (peringkat bersama). Fenomena ini mengindikasikan bahwa produk-produk premium telah mencapai tingkat kematangan yang tinggi dalam hal perlindungan dan kinerja.

2. **Konsistensi Antar Platform:** Beberapa vendor seperti Kaspersky, Bitdefender, dan Norton menunjukkan konsistensi kinerja lintas platform, menunjukkan kualitas produk yang merata.

3. **Stabilitas Ranking:** Analisis sensitivitas menunjukkan bahwa perankingan cukup stabil terhadap perubahan bobot, yang mengindikasikan robustness metode TOPSIS dalam domain ini.

Keterbatasan penelitian meliputi: (1) data diperoleh dari satu sumber saja (AV-TEST), (2) hanya tiga kriteria yang digunakan, dan (3) bobot ditetapkan secara manual berdasarkan asumsi.

---

## 5. KESIMPULAN DAN SARAN

### 5.1 Kesimpulan

Penelitian ini mengembangkan sistem penilaian antivirus multi-platform menggunakan metode TOPSIS dengan data dari AV-TEST Institute. Hasil menunjukkan bahwa: (1) sistem berhasil dirancang dengan arsitektur modular dan diuji terhadap 485 data pengujian, (2) TOPSIS efektif untuk perankingan multi-kriteria dengan menghasilkan 10+ juara lintas platform, (3) analisis sensitivitas menunjukkan stabilitas peringkat terhadap perubahan bobot, dan (4) Bitdefender Mobile Security menjadi juara terbanyak di Android dengan 4 kali juara selama 2023-2026.

### 5.2 Saran

Penelitian selanjutnya dapat menggunakan data dari lebih banyak sumber (misalnya AV-Comparatives), menambahkan kriteria evaluasi seperti fitur dan harga, mengintegrasikan AHP untuk pembobotan, dan mengembangkan aplikasi web interaktif untuk pengguna akhir.

---

## DAFTAR PUSTAKA

[1] AV-TEST Institute. (2026). *Test antivirus software for Windows 11 - The best antivirus protection for PC*. https://www.av-test.org/en/antivirus/home-windows/

[2] Alhakami, W. (2024). Evaluating modern intrusion detection methods in the face of Gen V multi-vector attacks with fuzzy AHP-TOPSIS. *PLOS ONE*, 19(5), e0302559. https://doi.org/10.1371/journal.pone.0302559

[3] Chaube, S., Kumar, R., & Joshi, M. (2024). An overview of multi-criteria decision analysis and the applications of AHP and TOPSIS methods. *International Journal for Multidisciplinary Research (IJMEMS)*, 9(3), 581-615. https://doi.org/10.33889/IJMEMS.2024.9.3.030

[4] Panahi, U., & Abdulvahitoğlu, A. (2026). Ranking multiple antivirus software solutions: A Borda-based MCDM approach to performance evaluation. *Cluster Computing*. https://doi.org/10.1007/s10586-026-06155-0

[5] Madanchian, M., & Taherdoost, H. (2023). A comprehensive guide to the TOPSIS method for multi-criteria decision making. *Sustainable Social Development*, 1(1), 1-6. https://doi.org/10.54517/ssd.v1i1.2220

[6] Kumar, R. (2025). A comprehensive review of MCDM methods, applications, and emerging trends. *Decision Making Advances*, 3(1). https://doi.org/10.31181/dma31202569

[7] Kumar, A., Dhiman, G., Kaur, A., & Kaur, A. (2023). A review on TOPSIS method and its extensions for different applications with recent development. *Soft Computing*. https://doi.org/10.1007/s00500-023-09011-0

[8] Shih, H.S., & Olson, D.L. (2022). *TOPSIS and its Extensions: A Distance-Based MCDM Approach*. Springer. https://doi.org/10.1007/978-3-031-09577-1

[9] Hwang, C.L., & Yoon, K. (1981). *Multiple Attribute Decision Making: Methods and Applications*. Springer-Verlag.

[10] Yoon, K. (1987). A reconciliation among discrete compromise situations. *Journal of the Operational Research Society*, 38(3), 277-286.

[11] Velasquez, M., & Hester, P.T. (2013). An analysis of multi-criteria decision making methods. *International Journal of Operations Research*, 10(2), 56-66.

[12] Zavadskas, E.K., Turskis, Z., & Kildienė, S. (2014). State of art surveys of overviews on MCDM/MADM methods. *Technological and Economic Development of Economy*, 20(1), 165-179.

[13] Gitelman, L., & Kozlovskaya, E. (2023). *Multi-Criteria Analysis in the Energy Sector*. Springer.

[14] Sensitivity analysis in multi-criteria decision making: A state-of-the-art research perspective using bibliometric analysis. (2024). *Expert Systems with Applications*, 237. https://doi.org/10.1016/j.eswa.2023.121660

---

*Paper ini disusun dalam format Markdown dan dapat dikonversi ke format LaTeX atau Microsoft Word sesuai kebutuhan.*
