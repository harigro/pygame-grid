# Tentang GridDrawer

Kelas `GridDrawer` adalah utilitas Python yang dirancang untuk membantu pengembang membuat pola grid yang dapat disesuaikan dalam aplikasi Pygame. Kelas ini menyediakan opsi untuk mengontrol tampilan, jarak, dan pelabelan garis grid utama maupun minor, sehingga sangat ideal untuk pengembangan game, simulasi, atau alat desain visual.

---

## Fitur

### Garis Grid yang Dapat Disesuaikan

Kelas `GridDrawer` memungkinkan pengguna untuk menentukan:

- Jarak antara garis grid utama (`x_dist`, `y_dist`)
- Ketebalan, warna, dan opasitas garis utama (`thickness`, `color`, `opacity`)
- Jarak antara garis grid minor (`x_minor_dist`, `y_minor_dist`)
- Ketebalan, warna, dan opasitas garis minor (`minor_thickness`, `minor_color`, `minor_opacity`)

### Label untuk Garis Utama

Garis grid utama dapat diberi label untuk meningkatkan kemudahan penggunaan, sehingga memudahkan referensi posisi dalam grid.

### Terintegrasi Sepenuhnya dengan Pygame

Kelas ini dibangun untuk Pygame, sehingga bekerja secara mulus dengan permukaan Pygame untuk rendering.

---

## Kasus Penggunaan

1. **Pengembangan Game**:
   
   - Menerapkan game berbasis ubin seperti game strategi atau puzzle.
   - Membuat editor peta.

2. **Visualisasi**:
   
   - Menggambar grid untuk visualisasi data atau simulasi.

3. **Desain UI/UX**:
   
   - Mendesain antarmuka dengan penjajaran yang presisi.

---

## Memulai

### Instalasi

Pastikan Anda telah menginstal Pygame. Jika belum, instal menggunakan:

```bash
pip install pygame
```

### Contoh Penggunaan

```python
import pygame
from pygame_grid import GridDrawer

# Inisialisasi Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Contoh GridDrawer")

# Buat instance GridDrawer
grid = GridDrawer()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # Isi layar dengan warna putih

    # Gambar grid
    grid.draw_grid(screen, width=800, height=600)

    pygame.display.flip()

pygame.quit()
```

---

## Kontribusi

Kontribusi untuk proyek `GridDrawer` sangat diterima! Jangan ragu untuk mengirimkan permintaan penarikan (pull request) atau melaporkan masalah pada repositori.

---

## Lisensi

Kelas `GridDrawer` dilisensikan di bawah Lisensi MIT. Lihat file `LICENSE` untuk detail lebih lanjut.
