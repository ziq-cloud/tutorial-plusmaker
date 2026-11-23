# PlusMaker Performance Card

Template 16:9 untuk share performance di channel Telegram: GIF/video di atas, caption anda di bawah.

**Untuk Telegram:** biarkan *Teks dalam video* = Tiada, tulis caption (had 1024 aksara), tekan **Salin caption**, kemudian **Simpan video**. Hantar MP4 itu dalam channel dan tampal caption. MP4 tanpa bunyi dimainkan Telegram sebagai GIF (auto main & ulang).

- Buka `standalone.html` dalam Chrome / Edge / Safari (tak perlu install apa-apa).
- Pilih GIF, video (MP4/MOV/WebM) atau gambar.
- Tulis label, ayat utama dan baris bawah (contoh `@username · tarikh`).
- Pilih tema (Malam / Siang / Emas), jajaran dan saiz.
- Simpan sebagai **video** (MP4, atau WebM jika browser tak sokong MP4), **GIF** (960 px, 12 fps) atau **PNG**.

Teks dalam video (pilihan):
- *Tiada*: video 16:9 bersih, ayat diletak sebagai caption Telegram.
- *Semua dalam 16:9*: media + teks dalam satu frame 1920×1080.
- *Media 16:9 + teks bawah*: media kekal 1920×1080, jalur teks ditambah di bawah.

`index.html` ialah versi yang diterbitkan sebagai Artifact; `standalone.html` ialah salinan yang sama untuk dibuka terus.
Termasuk [gifenc](https://github.com/mattdesl/gifenc) 1.0.3 (MIT).
