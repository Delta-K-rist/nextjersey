## Tugas Individu - PBP C
### Deltakristiano Kurniaputra - NPM: 2406425810
#### Link Deployment: 

<details><summary>Tugas 3: Implementasi Form dan Data Delivery pada Django</summary>

---
## **Q1:** Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Karena dalam pengimplementasian sebuah platform, kita perlu mengirimkan data dari satu komponen ke komponen lainnya. Dalam proses ini, data dapat dikirimkan dalam berbagai format seperti HTML, XML, dan JSON sesuai dengan kebutuhan dan kecocokan sistem. Format-format ini dirancang agar mudah dimengerti dan dapat diproses dengan cepat oleh program. Dengan menggunakan data delivery yang tepat, berbagai komponen sistem dapat saling berkomunikasi dengan efektif. 

---

## **Q2:** Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Menurut saya pribadi, JSON jauh lebih intuitif dan mudah dipahami dibandingkan XML, bahkan tanpa background ataupun prior knowledge. Saya pertama kali tahu adanya JSON kurang dari setahun lalu saat seleksi RISTEK Data Science, dan langsung memahaminya saat pertama kali membacanya. Hal ini mungkin karena format key-value pairs JSON lebih sederhana, sedangkan XML memiliki struktur yang lebih kompleks dengan banyak tag pembuka dan penutup.



Dari segi penggunaan praktis, saya jarang menemukan project yang masih menggunakan XML. Dalam project, konvensi merupakan hal yang penting, dan mungkin, dugaan saya, XML menjadi jarang digunakan karena sedikit orang yang memakainya, sehingga tercipta siklus di mana semakin sedikit adoption, semakin jarang orang memilihnya (bukan konvensi). Selain itu, JSON juga memiliki dukungan yang lebih luas dari hampir semua bahasa pemrograman modern, membuat JSON menjadi pilihan yang lebih praktis dan relevan untuk pengembangan aplikasi saat ini.

---
## **Q3:** Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?
Method `is_valid()` pada form Django digunakan untuk memvalidasi data yang dikirimkan oleh pengguna melalui form. Method ini memeriksa apakah semua data telah memenuhi kriteria yang didefinisikan dan mengembalikan nilai `True` jika valid atau `False` jika tidak.

Kita membutuhkan `is_valid()` karena method ini memastikan keamanan dan integritas data sebelum disimpan ke database. Dengan memvalidasi data terlebih dahulu, kita dapat mencegah data yang tidak aman atau tidak sesuai format dari masuk ke sistem, menghindari error aplikasi, dan memberikan feedback yang jelas kepada pengguna jika ada kesalahan input. Seperti yang terlihat dalam tutorial, pada fungsi `create_news`, form hanya akan disimpan ke database ketika `is_valid()` mengembalikan `True` dan request method adalah POST.

---

## **Q4:** Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

`csrf_token` adalah token keamanan yang di-generate otomatis oleh Django untuk melindungi aplikasi dari serangan CSRF (Cross-Site Request Forgery). Token ini memastikan bahwa form yang di-submit benar-benar berasal dari aplikasi kita, bukan dari situs lain yang sekiranya berbahaya.

`csrf_token` bekerja dengan cara menyisipkan token unik yang acak ke dalam setiap permintaan POST. Karena penyerang tidak memiliki akses ke token yang sah milik pengguna, mereka tidak dapat membuat permintaan palsu yang akan diterima oleh server. Dengan mekanisme ini, Django memastikan bahwa hanya permintaan yang memiliki token yang tepat yang akan diproses.

Tanpa `csrf_token`, aplikasi menjadi rentan terhadap serangan. Penyerang dapat membuat situs palsu dengan form tersembunyi yang secara otomatis terkirim ketika pengguna mengunjungi situs mereka. Jika pengguna masih login di aplikasi kita, request akan dikirimkan dengan kredensial login pengguna yang valid, memungkinkan penyerang untuk melakukan aksi tanpa persetujuan pengguna seperti mengubah data pribadi, menghapus konten, atau melakukan transaksi. Dengan `csrf_token`, Django memvalidasi bahwa request benar-benar dari aplikasi kita sendiri, sehingga mencegah serangan semacam ini terjadi.

---

## **Q5:** Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Mirip seperti pengerjaan Tugas 2 sebelumnya, saya mulai dengan tutorial dan bertanya kepada LLM (read: chatgpt/claude) untuk meningkatkan pemahaman dan bertanya hal yang membingungkan selama pengerjaan tugas ini. Step saya dalam pemenuhan checklist adalah seperti ini:

1. Membuat fungsi view dan URL routing untuk menampilkan data `Product` dalam berbagai format (`XML`, `JSON`, `XML by ID`, dan `JSON by ID`) sesuai contoh tutorial.
2. Menambahkan halaman `/add-product` dengan form untuk membuat `Product` baru dan halaman `/product/<str:id>` untuk detail `Product`.
3. Mendokumentasikan jawaban pertanyaan dalam `README.md`.
4. Melakukan pengujian API `GET` via POSTMAN.
5. Commit ke GitHub dan deployment ke PWS.

---

## **Q6:** Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?

Sudah sangat baik, hampir semua komponen dalam tugas dapat dipelajari dari tutorial 👍👍👍

Cuma mungkin another feedback sedikit, it'd be nice kalau di tiap sesi tutorial dijelaskan juga sisi "why"-nya. I assume ini tidak dijelaskan karena harapannya mahasiswa mencari sendiri untuk menjawab tugas secara mandiri. Namun menurut saya pribadi, dalam sesi pembelajaran, agar pelajaran lebih "nyantol" ke mahasiswa, perlu diterangkan "why" dari each major steps. I think that'd really help enhance the learning experience by a significant margin.

---
## Postman:
<img width="1280" height="683" alt="gambar-t3-xml-id" src="gambar-t3-xml-id.jpg" />
<img width="1280" height="683" alt="gambar-t3-xml" src="gambar-t3-xml.jpg" />
<img width="1280" height="683" alt="gambar-t3-json-id" src="gambar-t3-json-id.jpg" />
<img width="1280" height="683" alt="gambar-t3-json" src="gambar-t3-json.jpg" />

(Kalo gabisa diakses, buka aja file `gambar-t3-<format>` yang ada di repo ini)

---
### Checklist Tugas

- [X] Tambahkan 4 fungsi `views` baru untuk melihat objek yang sudah ditambahkan dalam format:
    - [X] XML
    - [X] JSON
    - [X] XML by ID
    - [X] JSON by ID
- [X] Buat **routing URL** untuk masing-masing `views` yang telah ditambahkan.
- [X] Buat halaman yang menampilkan data objek model. Halaman ini harus memiliki:
    - [X] Tombol "Add" yang akan mengarah ke halaman formulir.
    - [X] Tombol "Detail" pada setiap data objek model untuk menampilkan halaman detail objek.
- [X] Buat halaman **formulir** untuk menambahkan objek model pada aplikasi sebelumnya.
- [X] Buat halaman yang menampilkan detail dari setiap data objek model.
- [X] Jawab pertanyaan-pertanyaan berikut pada berkas `README.md` di _root folder_:
    - [X] Mengapa kita memerlukan **data delivery** dalam pengimplementasian sebuah _platform_?
    - [X] Mana yang lebih baik antara **XML** dan **JSON**? Mengapa **JSON** lebih populer dibandingkan **XML**?
    - [X] Jelaskan fungsi dari method `is_valid()` pada formulir Django dan mengapa kita membutuhkannya.
    - [X] Mengapa kita membutuhkan `csrf_token` saat membuat formulir di Django? Apa yang dapat terjadi jika tidak ada `csrf_token`? Bagaimana hal ini dapat dimanfaatkan oleh penyerang?
    - [X] Jelaskan implementasi **_step-by-step_** dari daftar periksa di atas.
    - [X] Berikan _feedback_ untuk asdos pada tutorial 2.
- [X] Akses keempat URL di poin 2 menggunakan **Postman**.
- [X] Buat **_screenshot_** dari hasil akses URL pada Postman dan tambahkan ke `README.md`.
- [X] Lakukan `add-commit-push` ke GitHub.
</details>

<details><summary>Tugas 2: Implementasi Model-View-Template (MVT) pada Django</summary>


---
## **Q1:** Jelaskan bagaimana cara kamu mengimplementasikan checklist secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- Pertama buka tutorial, `print as pdf`, lalu saya upload tutorial ke chatgpt/claude buat memberikan chatgpt/claude context akan pekerjaan saya. Tujuannya adalah ketika ada error atau istilah yang belum pernah dengar atau penjelasan yang saya rasa membingungkan, saya bisa tanya chatgpt/claude. Better, saya bisa konfigurasikan cara penjelasannya sesuai preferensi saya agar saya lebih mudah memahaminya (saya lebih mudah paham jika dijelaskan dengan pendekatan seperti ini: Misal ada sebongkah lines of codes, saya ingin tahu alasan kenapa diperlukan those line of codes dan apa impactnya terhadap goal overall, dan contoh langsung supaya lebih terbayang. Dengan pendekatan penjelasan ini, saya jadi jauh lebih memahami materi, dan chatgpt/claude easily help me done that.)
- Saya lalu baca sekilas checklist tugas, apa aja yang diharapkan untuk dilakukan, tanya chatgpt/claude juga kalau tidak paham maksudnya apa.
- Mengimplementasikan setiap step dari tutorial, lalu setiap ada perubahan (perbedaan dengan tugas), saya langsung edit implementasi tutorial sesuai dengan tugas.
- Selama local server udah bisa di run, especially saat mengedit file `html`, saya selalu check di lokal bagaimana perubahan yang lakukan berdampak ke presentasi dari webnya. Supaya lebih kebayang each line of htmlnya gunanya untuk apa.

Berikut langkah-langkahnya untuk menyelesaikan checklist:

1. Pertama mengikuti seperti tutorial dulu, menyiapkan folder project baru dengan Python virtual environment, file `requirements.txt`, dan menginstall semua dependency yang dibutuhkan.
2. Membuat project Django `nextjersey` menggunakan `django-admin startproject`, kemudian mengkonfigurasi `settings.py` untuk menghubungkan dengan database dan menyiapkan `git` serta `github` untuk version control.
3. Menjalankan arsitektur *MVT dengan membuat aplikasi `main`, mendefinisikan model `Product` pada `models.py`, dan melakukan migrasi untuk menerapkannya ke database.
4. Membuat template HTML dalam direktori `template` dan mengatur sistem routing URL melalui `views.py` di aplikasi `main` serta `urls.py` di level project dan aplikasi.
5. Melakukan deployment ke PWS.

---



## **Q2:** Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

\
<img width="1019" height="660" alt="gambar-t2" src="gambar-t2.png" />
(Made in Miro)
(Kalo gabisa diakses, buka aja file `gambar-t2.png` yang ada di repo ini)

Alur: 
1. User kirim request URL
2. urls.py cocokkan URL lalu menentukan view mana yang dijalankan
3. views.py jalanin -> minta data ke models.py
4. models.py ambil data dari database → kembalikan ke views.py
4. views.py kirim data ke filename.html → template render jadi HTML
5. views.py ambil HTML dari template → di wrap jadi HTTP Response
6. Kirim response ke browser user
7. user sekarang bisa lihat web pagenya

---

## **Q3:** Jelaskan peran `settings.py` dalam proyek Django!

`settings.py` adalah file konfigurasi utama di Django yang fungsinya adalah untuk mengatur (as the name suggests, settings) semua aspek jalannya aplikasi sesuai dengan kebutuhan proyek. Konfigurasi tersebut contoh-contohnya:

1. Database: mengatur koneksi database (engine, nama DB, user, password, host, port)
2. Installed Apps: mendaftar aplikasi bawaan Django dan aplikasi custom yang digunakan
3. Middleware: mengatur layer pemrosesan untuk setiap request dan response
4. Static & Media Files: menentukan lokasi static file (CSS, JS, gambar) dan file upload user
5. Security: konfigurasi keamanan seperti `SECRET_KEY`, `ALLOWED_HOSTS`, CSRF protection, dan autentikasi
6. Debugging: mengaktifkan atau menonaktifkan mode debug untuk development
7. Internationalization: mengatur bahasa aplikasi (`LANGUAGE_CODE`) dan zona waktu (`TIME_ZONE`), yang mana berguna juga kalau mau menggunakan format mata uang negara tertentu.

---
## **Q4:** Bagaimana cara kerja migrasi database di Django?

1. Pertama, command `python manage.py makemigrations` akan membuat Django membaca perubahan model pada models.py lalu membuat file migrasi. File migrasi adalah file berisi instruksi SQL tetapi dalam bentuk Python.
2. Command `python manage.py migrate` akan menerjemahkan file migrasi tadi menjadi perintah SQL yang dijalankan ke database.
3. Lalu catatan migrasi tersebut disimpan di `migrations`, sehingga tidak perlu dieksekusi dua kali.

---
## **Q5:**  Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Karena relatif mudah untuk pemula. Apalagi dalam konteks FASILKOM UI, kita semua start dengan belajar python di Dasar Dasar Pemrograman 1 sehingga menggunakan django akan sangat mudah karena django adalah python-based. Lalu sepertinya django sudah banyak mengatur hal di belakang layar (semacam abstraction gitu) jadinya gabanyak hal yang perlu di atur from scratch oleh developer. Cocok untuk pemula

---
## **Q6:**  Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?

Jujur tutorialnya sudah bagus sekali dan penjelasannya cukup mudah dipahami. Cuma mungkin diberi tambahan seperti tips & trick yang sekiranya bermanfaat. Misalnya untuk setiap perubahan cek di local. Itu orang awam belum tentu mengerti (saya awalnya tidak kepikiran sampai diberi tahu teman saya). I guess it’s nice kalau disampaikan explicitly.

---

# Checklist Tugas

- [X] Membuat sebuah proyek Django baru.
- [X] Membuat aplikasi dengan nama main pada proyek tersebut.
- [X] Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
- [X] Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut.
  - [X] name sebagai nama item dengan tipe CharField.
  - [X] price sebagai harga item dengan tipe IntegerField.
  - [X] description sebagai deskripsi item dengan tipe TextField.
  - [X] thumbnail sebagai gambar item dengan tipe URLField.
  - [X] category sebagai kategori item dengan tipe CharField.
  - [X] is_featured sebagai status unggulan item dengan tipe BooleanField.
- [X] Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
- [X] Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
- [X] Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
- [X] Membuat sebuah README.md yang berisi tautan menuju aplikasi PWS yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.
  - [X] Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
  - [X] Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
  - [X] Jelaskan peran settings.py dalam proyek Django!
  - [X] Bagaimana cara kerja migrasi database di Django?
  - [X] Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
  - [X] Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?

</details>