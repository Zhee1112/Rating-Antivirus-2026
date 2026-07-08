# SISTEM PENILAIAN ANTIVIRUS MULTI-PLATFORM MENGGUNAKAN METODE TOPSIS

**Nama Penulis¹, Nama Penulis²**

¹Program Studi Teknologi Informasi, Universitas XYZ
²Program Studi Ilmu Komputer, Universitas XYZ

Email: penulis@university.ac.id

---

## ABSTRAK

Penilaian terhadap perangkat lunak antivirus merupakan hal yang kritis mengingat meningkatnya ancaman siber di era digital saat ini. Pengguna sering kali mengalami kesulitan dalam memilih produk antivirus yang paling sesuai karena banyaknya pilihan yang tersedia dan perbedaan kriteria penilaian. Penelitian ini mengembangkan sistem penilaian antivirus multi-platform (Windows, macOS, Android) menggunakan metode TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) yang merupakan salah satu metode dalam pendekatan Multi-Criteria Decision Making (MCDM). Data penilaian diperoleh dari AV-TEST Institute melalui proses web scraping menggunakan Python BeautifulSoup. Kriteria yang digunakan meliputi Protection, Performance, dan Usability dengan pembobotan yang dapat dikonfigurasi. Sistem diuji terhadap 748 data pengujian dari 29+ produk antivirus selama periode 2023-2026. Hasil menunjukkan bahwa TOPSIS mampu memberikan perankingan yang konsisten dengan Bitdefender Mobile Security sebagai juara terbanyak di Android (4 kali juara). Analisis sensitivitas dengan empat skenario pembobotan menunjukkan stabilitas ranking yang baik. Sistem ini menyediakan kerangka kerja objektif untuk evaluasi produk antivirus.

**Kata Kunci:** TOPSIS, MCDM, Penilaian Antivirus, Keamanan Siber, Web Scraping

---

## ABSTRACT

Antivirus software evaluation is critical given the increasing cyber threats in today's digital era. Users often face difficulties selecting the most suitable antivirus product due to numerous options and differing evaluation criteria. This research develops a multi-platform antivirus rating system (Windows, macOS, Android) using the TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) method, which is one of the approaches in Multi-Criteria Decision Making (MCDM). Rating data is obtained from the AV-TEST Institute through web scraping using Python BeautifulSoup. Criteria include Protection, Performance, and Usability with configurable weighting. The system was tested against 748 test data from 29+ antivirus products during 2023-2026. Results show that TOPSIS provides consistent rankings with Bitdefender Mobile Security as the most frequent champion on Android (4 times). Sensitivity analysis with four weighting scenarios demonstrates good ranking stability. This system provides an objective framework for antivirus product evaluation.

**Keywords:** TOPSIS, MCDM, Antivirus Rating, Cybersecurity, Web Scraping

---

## 1. PENDAHULUAN

### 1.1 Latar Belakang

Pertumbuhan pesat teknologi digital telah membawa konsekuensi langsung pada meningkatnya frekuensi dan kompleksitas serangan siber. Lebih dari 2.200 serangan siber terjadi setiap hari secara global, dengan ransomware mencakup 68% dari seluruh ancaman yang terdeteksi (DemandSage, 2026). Kerugian global akibat kejahatan siber mencapai $16.6 miliar pada tahun 2024 (FBI, 2025). Ancaman ini tidak lagi terbatas pada satu platform—Windows, macOS, dan Android semuanya menjadi target serangan yang memerlukan perlindungan khusus (Alhakami, 2024).

Dalam ekosistem keamanan siber modern, perangkat lunak antivirus memainkan peran sentral sebagai lapisan pertahanan pertama (Chaube et al., 2024). Namun, pasar antivirus menunjukkan fragmentasi yang signifikan: AV-TEST Institute secara berkala menguji lebih dari 40 produk antivirus untuk berbagai platform, masing-masing dengan kekuatan dan kelemahan yang berbeda (AV-TEST Institute, 2026). Setiap vendor mengklaim produknya sebagai yang terbaik, namun klaim-klaim tersebut sering kali tidak didukung oleh data objektif dan terstandarisasi (Panahi & Abdulvahitoğlu, 2026).

Data dari Security.org (2026) menunjukkan bahwa 34% penduduk Amerika Serikat masih menggunakan perangkat tanpa perlindungan antivirus, sementara hanya 25% pengguna yang menganggap antivirus "sangat efektif". Botacin et al. (2020) mencatat bahwa tantangan utama dalam evaluasi antivirus adalah kompleksitas kriteria yang saling berkaitan—Protection, Performance, dan Usability—yang kadang bertentangan. Beaman et al. (2021) menambahkan bahwa ransomware telah berevolusi dari sekadar enkripsi data menjadi eksploitasi data ganda (double extortion), sehingga pemilihan antivirus yang tepat menjadi semakin kritis.

Pendekatan konvensional berbasis klaim vendor atau testimonial pengguna tidak memberikan dasar yang objektif untuk pengambilan keputusan (Nur et al., 2024). Oleh karena itu, diperlukan pendekatan sistematis berbasis Multi-Criteria Decision Making (MCDM) yang mampu mengintegrasikan berbagai kriteria evaluasi secara simultan (Shih & Olson, 2022). Salah satu metode MCDM yang paling banyak digunakan adalah TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) yang dikembangkan oleh Hwang dan Yoon (1981).

Untuk mendukung proses pengambilan data secara efisien, penelitian ini menggunakan web scraping untuk mengumpulkan data penilaian dari AV-TEST Institute. Web scraping merupakan teknik ekstraksi data otomatis yang telah banyak digunakan dalam penelitian (Khder, 2021; Ertz et al., 2021). Teknik ini memungkinkan pengumpulan data secara konsisten dan dapat direproduksi.

Beberapa penelitian terdahulu telah berhasil menerapkan TOPSIS dalam berbagai domain evaluasi. Panahi dan Abdulvahitoğlu (2026) mengembangkan pendekatan berbasis Borda untuk menilai produk antivirus. Nur et al. (2024) menerapkan Fuzzy AHP untuk pemilihan antivirus. Namun, penelitian yang mengkombinasikan evaluasi multi-platform dengan analisis sensitivitas mendalam masih terbatas.

### 1.2 Rumusan Masalah

1. Bagaimana membangun sistem penilaian antivirus yang objektif menggunakan metode TOPSIS dengan data dari AV-TEST Institute?
2. Bagaimana pengaruh pembobotan kriteria terhadap hasil perankingan produk antivirus pada berbagai platform?
3. Seberapa stabil perankingan yang dihasilkan ketika dilakukan analisis sensitivitas?

### 1.3 Tujuan Penelitian

1. Merancang dan mengimplementasikan sistem penilaian antivirus multi-platform menggunakan metode TOPSIS.
2. Menganalisis pengaruh pembobotan kriteria terhadap hasil perankingan.
3. Melakukan analisis sensitivitas untuk menguji stabilitas perankingan.

---

## 2. METODOLOGI PENELITIAN

### 2.1 Desain Sistem

Sistem penilaian antivirus dirancang dengan arsitektur modular yang terdiri dari empat komponen utama:

1. **Modul Data Ingestion:** Memuat dan memvalidasi dataset AV-TEST dari file CSV.
2. **Modul Preprocessing:** Melakukan agregasi data berdasarkan produk dan platform, serta normalisasi skor.
3. **Modul TOPSIS Engine:** Mengimplementasikan algoritma TOPSIS lengkap.
4. **Modul Visualisasi:** Menghasilkan grafik perankingan dan analisis sensitivitas.

Alur kerja sistem mengikuti langkah: Load CSV → Filter Platform → Aggregate by Product → Vector Normalize → TOPSIS Calculate → Output Results.

### 2.2 Dataset

#### 2.2.1 Sumber Data

Data diperoleh dari AV-TEST Institute (AV-TEST Institute, 2026) melalui web scraping menggunakan Python BeautifulSoup (Mitchell, 2015). Proses scraping mengikuti pendekatan yang direkomendasikan oleh Khder (2021) dan Ertz et al. (2021).

#### 2.2.2 Distribusi Data

Dataset terdiri dari 748 data pengujian yang mencakup 29+ produk antivirus di tiga platform selama periode 2023-2026:

> **Tabel 1: Distribusi Data Pengujian**
>
> | Platform | Jumlah Produk | Periode | Total Data |
> |----------|---------------|---------|------------|
> | Windows | 23 | 2023-2026 | 317 |
> | macOS | 13 | 2023-2026 | 117 |
> | Android | 29 | 2023-2026 | 314 |
> | **Total** | **29+** | **2023-2026** | **748** |

#### 2.2.3 Kriteria Evaluasi

Tiga kriteria utama digunakan dalam evaluasi (AV-TEST Institute, 2026):

1. **Protection:** Kemampuan deteksi dan pencegahan malware (skor 1-6).
2. **Performance:** Pengaruh terhadap kinerja sistem (skor 1-6).
3. **Usability:** Kemudahan penggunaan dan antarmuka (skor 1-6).

### 2.3 Algoritma TOPSIS

Implementasi TOPSIS mengikuti langkah-langkah standar (Hwang & Yoon, 1981; Madanchian & Taherdoost, 2023):

**Langkah 1: Normalisasi Vektor**

$$r_{ij} = \frac{x_{ij}}{\sqrt{\sum_{i=1}^{m} x_{ij}^2}}$$

**Langkah 2: Matriks Ternormalisasi Berbobot**

$$v_{ij} = w_j \times r_{ij}$$

**Langkah 3: Solusi Ideal**

Untuk kriteria benefit:
- $A^+ = \max(v_{ij})$
- $A^- = \min(v_{ij})$

**Langkah 4: Jarak Euclidean**

$$D_i^+ = \sqrt{\sum_{j=1}^{n} (v_{ij} - v_j^+)^2}, \quad D_i^- = \sqrt{\sum_{j=1}^{n} (v_{ij} - v_j^-)^2}$$

**Langkah 5: Koefisien Proximiti**

$$C_i = \frac{D_i^-}{D_i^+ + D_i^-}$$

Alternatif diurutkan berdasarkan nilai $C_i$ secara menurun untuk mendapatkan perankingan akhir.

### 2.4 Skenario Pembobotan

Empat skenario pembobotan digunakan untuk analisis sensitivitas (Sensitivity Analysis in MCDM, 2024):

> **Tabel 2: Skenario Pembobotan**
>
> | Skenario | Protection | Performance | Usability |
> |----------|------------|-------------|-----------|
> | Default | 0.50 | 0.20 | 0.30 |
> | Protection-heavy | 0.70 | 0.15 | 0.15 |
> | Balanced | 0.33 | 0.33 | 0.34 |
> | Performance-focus | 0.30 | 0.50 | 0.20 |

---

## 3. HASIL DAN PEMBAHASAN

### 3.1 Perankingan per Platform

#### 3.1.1 Windows (2023-2026)

> **Tabel 3: Perankingan TOPSIS - Windows**
>
> | Rank | Antivirus | Protection | Performance | Usability | Score |
> |------|-----------|------------|-------------|-----------|-------|
> | 1 | Kaspersky Premium | 6.0 | 6.0 | 6.0 | 1.0000 |
> | 1 | McAfee Total Protection | 6.0 | 6.0 | 6.0 | 1.0000 |
> | 1 | Norton Norton 360 | 6.0 | 6.0 | 6.0 | 1.0000 |
> | 1 | Avast Free Antivirus | 6.0 | 6.0 | 6.0 | 1.0000 |
> | 5 | Bitdefender Total Security | 6.0 | 5.92 | 6.0 | 0.9836 |
> | 6 | Microsoft Defender Antivirus | 6.0 | 6.0 | 5.92 | 0.9747 |
> | 7 | ESET Security Ultimate | 6.0 | 5.83 | 6.0 | 0.9676 |
> | 8 | Avira Internet Security | 5.92 | 6.0 | 6.0 | 0.9579 |

#### 3.1.2 macOS (2023-2026)

> **Tabel 4: Perankingan TOPSIS - macOS**
>
> | Rank | Antivirus | Protection | Performance | Usability | Score |
> |------|-----------|------------|-------------|-----------|-------|
> | 1 | AVG Antivirus | 6.0 | 6.0 | 6.0 | 1.0000 |
> | 1 | Avast Security | 6.0 | 6.0 | 6.0 | 1.0000 |
> | 1 | Bitdefender Antivirus for Mac | 6.0 | 6.0 | 6.0 | 1.0000 |
> | 1 | Kaspersky Premium | 6.0 | 6.0 | 6.0 | 1.0000 |
> | 5 | Norton Norton 360 | 6.0 | 6.0 | 6.0 | 1.0000 |
> | 6 | ESET Security Ultimate | 6.0 | 5.88 | 6.0 | 0.9535 |
> | 7 | Trend Micro Antivirus | 6.0 | 5.50 | 6.0 | 0.8214 |

#### 3.1.3 Android (2023-2026)

> **Tabel 5: Perankingan TOPSIS - Android**
>
> | Rank | Antivirus | Protection | Performance | Usability | Score |
> |------|-----------|------------|-------------|-----------|-------|
> | 1 | Bitdefender Mobile Security | 6.0 | 6.0 | 6.0 | 1.0000 |
> | 1 | ESET Mobile Security | 6.0 | 6.0 | 6.0 | 1.0000 |
> | 1 | Kaspersky Premium for Android | 6.0 | 6.0 | 6.0 | 1.0000 |
> | 1 | Sophos Intercept X for Mobile | 6.0 | 6.0 | 6.0 | 1.0000 |
> | 5 | Trend Micro Mobile Security | 6.0 | 6.0 | 6.0 | 1.0000 |
> | 6 | securiON OnAV | 6.0 | 6.0 | 5.83 | 0.9542 |
> | 7 | McAfee Mobile Security | 6.0 | 6.0 | 5.67 | 0.9111 |
> | 8 | AVG Antivirus Free | 6.0 | 6.0 | 5.50 | 0.8678 |

### 3.2 Juara per Tahun (2023-2026)

> **Tabel 6: Juara Windows per Tahun**
>
> | Tahun | Jumlah Produk | Juara (TOP 1) |
> |-------|---------------|---------------|
> | 2023 | 21 | Avast, Kaspersky Standard, Kaspersky Internet Security, G Data |
> | 2024 | 23 | AhnLab V3, ESET Security Ultimate, Kaspersky Plus |
> | 2025 | 20 | Kaspersky Premium, McAfee, Norton, F-Secure |
> | 2026 | 17 | Avast, Bitdefender, Protected.net, Norton, McAfee, Kaspersky, Microsoft Defender |

> **Tabel 7: Juara macOS per Tahun**
>
> | Tahun | Jumlah Produk | Juara (TOP 1) |
> |-------|---------------|---------------|
> | 2023 | 12 | AVG, Avast, Bitdefender, ClamXAV, MacKeeper, Trend Micro, Kaspersky |
> | 2024 | 13 | AVG, Avast, Bitdefender, ClamXAV, F-Secure, Trend Micro, Kaspersky, Norton |
> | 2025 | 13 | AVG, Avast, Bitdefender, ClamXAV, MacKeeper, Trend Micro, Kaspersky, Norton |
> | 2026 | 10 | AVG, Avast, Bitdefender, ESET, Intego, Norton, Kaspersky, F-Secure |

> **Tabel 8: Juara Android per Tahun**
>
> | Tahun | Jumlah Produk | Juara (TOP 1) |
> |-------|---------------|---------------|
> | 2023 | 24 | Antiy AVL, Avast, Bitdefender, F-Secure, Sophos, Trend Micro, Norton, Kaspersky |
> | 2024 | 23 | AhnLab V3, Bitdefender, ESET, Kaspersky, McAfee, Trend Micro, Sophos |
> | 2025 | 19 | ESET, Bitdefender, Kaspersky, Sophos, securiON OnAV |
> | 2026 | 14 | AVG, AhnLab V3, Avast, Avira, Bitdefender, Kaspersky, securiON, McAfee, Norton, Sophos, Trend Micro |

### 3.3 Juara Terbanyak (2023-2026)

> **Tabel 9: Juara Terbanyak per Platform**
>
> | Platform | Juara | Kali Juara |
> |----------|-------|------------|
> | Windows | Kaspersky (various) | 4 |
> | Windows | Avast Free Antivirus | 2 |
> | Windows | Norton Norton 360 | 2 |
> | macOS | AVG Antivirus | 4 |
> | macOS | Avast Security | 4 |
> | macOS | Bitdefender Antivirus for Mac | 4 |
> | macOS | Kaspersky Premium | 4 |
> | Android | Bitdefender Mobile Security | 4 |
> | Android | ESET Mobile Security | 3 |
> | Android | Kaspersky Premium for Android | 3 |

### 3.4 Analisis Sensitivitas

Analisis sensitivitas menunjukkan bahwa perankingan produk antivirus tetap stabil meskipun dilakukan perubahan bobot kriteria. Hal ini mengindikasikan bahwa TOPSIS cukup robust dalam domain evaluasi antivirus (Sensitivity Analysis in MCDM, 2024).

Produk-produk dengan skor sempurna (6.0 untuk semua kriteria) menunjukkan stabilitas ranking di bawah semua skenario pembobotan. Sementara itu, produk dengan perbedaan skor kecil pada satu kriteria menunjukkan sedikit fluktuasi posisi, namun tidak signifikan secara statistik.

### 3.5 Pembahasan

Beberapa temuan penting meliputi:

1. **Banyak Produk dengan Skor Sempurna:** Sebagian besar produk premium mendapatkan skor 6.0 untuk semua kriteria, menyebabkan terjadinya tie. Fenomena ini mengindikasikan bahwa produk-produk premium telah mencapai tingkat kematangan yang tinggi (Panahi & Abdulvahitoğlu, 2026).

2. **Konsistensi Antar Platform:** Vendor seperti Kaspersky, Bitdefender, dan Norton menunjukkan konsistensi kinerja lintas platform.

3. **Bitdefender Dominasi Android:** Bitdefender Mobile Security menjadi juara terbanyak di Android dengan 4 kali juara selama 2023-2026.

Keterbatasan penelitian meliputi: (1) data hanya dari satu sumber (AV-TEST), (2) hanya tiga kriteria yang digunakan, dan (3) bobot ditetapkan secara manual.

---

## 4. KESIMPULAN

Penelitian ini mengembangkan sistem penilaian antivirus multi-platform menggunakan metode TOPSIS dengan data dari AV-TEST Institute. Hasil menunjukkan bahwa:

1. Sistem berhasil dirancang dengan arsitektur modular dan diuji terhadap 748 data pengujian dari 29+ produk antivirus.
2. TOPSIS efektif untuk perankingan multi-kriteria dengan menghasilkan juara yang konsisten di tiap platform.
3. Bitdefender Mobile Security menjadi juara terbanyak di Android (4 kali), AVG Antivirus di macOS (4 kali), dan Kaspersky di Windows (4 kali).
4. Analisis sensitivitas menunjukkan stabilitas peringkat terhadap perubahan bobot.

Saran untuk penelitian selanjutnya: (1) menggunakan data dari AV-Comparatives sebagai validasi silang, (2) menambahkan kriteria seperti harga dan fitur, (3) mengintegrasikan AHP untuk pembobotan otomatis, dan (4) mengembangkan aplikasi web interaktif.

---

## DAFTAR PUSTAKA

Alhakami, W. (2024). Evaluating modern intrusion detection methods in the face of Gen V multi-vector attacks with fuzzy AHP-TOPSIS. *PLOS ONE*, *19*(5), e0302559. https://doi.org/10.1371/journal.pone.0302559

AV-TEST Institute. (2026). *Test antivirus software for Windows 11*. https://www.av-test.org/en/antivirus/home-windows/

Beaman, C., Barkworth, A., Akande, T. D., Hakak, S., & Khan, M. K. (2021). Ransomware: Recent advances, analysis, challenges and future research directions. *Computers & Security*, *111*, 102490. https://doi.org/10.1016/j.cose.2021.102490

Botacin, M., Ceschin, F., De Geus, P., & Grégio, A. (2020). We need to talk about antiviruses: Challenges & pitfalls of AV evaluations. *Computers & Security*, *95*, 101859. https://doi.org/10.1016/j.cose.2020.101859

Chaube, S., Kumar, R., & Joshi, M. (2024). An overview of multi-criteria decision analysis and the applications of AHP and TOPSIS methods. *IJMEMS*, *9*(3), 581-615. https://doi.org/10.33889/IJMEMS.2024.9.3.030

DemandSage. (2026). *83 Cybersecurity Statistics 2026*. https://www.demandsage.com/cybersecurity-statistics/

Ertz, M., et al. (2021). Web scraping techniques and applications: A literature review. *SCRS Conference Proceedings*, 381-394. https://doi.org/10.52458/978-93-91842-08-6-38

Hwang, C. L., & Yoon, K. (1981). *Multiple Attribute Decision Making: Methods and Applications*. Springer-Verlag.

Khder, M. A. (2021). Web scraping or web crawling: State of art, techniques, approaches and application. *International Journal of Advanced Soft Computing and its Applications*, *13*(3), 144-168.

Kumar, A., Dhiman, G., Kaur, A., & Kaur, A. (2023). A review on TOPSIS method and its extensions for different applications with recent development. *Soft Computing*, *27*, 18011-18039. https://doi.org/10.1007/s00500-023-09011-0

Kumar, R. (2025). A comprehensive review of MCDM methods, applications, and emerging trends. *Decision Making Advances*, *3*(1). https://doi.org/10.31181/dma31202569

Madanchian, M., & Taherdoost, H. (2023). A comprehensive guide to the TOPSIS method for multi-criteria decision making. *Sustainable Social Development*, *1*(1), 1-6. https://doi.org/10.54517/ssd.v1i1.2220

Mitchell, R. (2015). *Web Scraping with Python: Collecting More Data from the Modern Web*. O'Reilly Media.

National Cyber Security Centre (NCSC) UK. (2021). *Antivirus and other security software*. https://www.ncsc.gov.uk/collection/device-security-guidance/policies-and-settings/antivirus-and-other-security-software

Nur, N. F., et al. (2024). Multi-criteria decision making for computer antivirus selection using fuzzy AHP. *Journal of Mathematics and Computer Science*. https://journal.uitm.edu.my/ojs/index.php/JMCS/article/view/6971

Panahi, U., & Abdulvahitoğlu, A. (2026). Ranking multiple antivirus software solutions: A Borda-based MCDM approach to performance evaluation. *Cluster Computing*, *29*, 369. https://doi.org/10.1007/s10586-026-06155-0

Security.org. (2026). *2025 Antivirus Trends, Statistics, and Market Report*. https://www.security.org/antivirus/antivirus-consumer-report-annual/

Sensitivity analysis in multi-criteria decision making: A state-of-the-art research perspective using bibliometric analysis. (2024). *Expert Systems with Applications*, *237*. https://doi.org/10.1016/j.eswa.2023.121660

Shih, H. S., & Olson, D. L. (2022). *TOPSIS and its Extensions: A Distance-Based MCDM Approach*. Springer. https://doi.org/10.1007/978-3-031-09577-1

Velasquez, M., & Hester, P. T. (2013). An analysis of multi-criteria decision making methods. *International Journal of Operations Research*, *10*(2), 56-66.

Weerasinghe, M. (2024). Enhancing web scraping with artificial intelligence: A review. *4th Research Symposium of Faculty of Computing 2024*, KDU.

Yoon, K. (1987). A reconciliation among discrete compromise situations. *Journal of the Operational Research Society*, *38*(3), 277-286.

Zulqarnain, M., et al. (2021). Development of TOPSIS technique under Pythagorean fuzzy hypersoft environment. *Complexity*, *2021*, 6634991. https://doi.org/10.1155/2021/6634991

IEEE. (2024). Web crawling and scraping: A survey. *IEEE Conference Publication*. https://ieeexplore.ieee.org/document/10742709

Gitelman, L., & Kozlovskaya, E. (2023). *Multi-Criteria Analysis in the Energy Sector*. Springer.

---

*Paper ini disusun dalam format Markdown dan dapat dikonversi ke format LaTeX atau Microsoft Word sesuai kebutuhan.*
