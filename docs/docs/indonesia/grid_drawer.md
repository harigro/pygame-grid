# Kelas GridDrawer

Kelas `GridDrawer` memungkinkan Anda untuk menggambar grid yang dapat disesuaikan di layar Pygame. Kelas ini menyediakan berbagai opsi untuk mengatur penampilan dan jarak grid, serta label untuk garis grid utama.

## Konstruktor: `__init__`

Menginisialisasi `GridDrawer` dengan properti grid yang dapat disesuaikan.

### Parameter:

- `x_dist` (int, default=100): Jarak antara garis vertikal grid utama dalam piksel.
- `y_dist` (int, default=100): Jarak antara garis horizontal grid utama dalam piksel.
- `color` (str, default="black"): Warna garis grid utama.
- `opacity` (float, default=0.5): Opasitas garis grid utama, antara 0.0 dan 1.0.
- `thickness` (int, default=3): Ketebalan garis grid utama dalam piksel.
- `x_minor_dist` (int, default=20): Jarak antara garis vertikal grid minor dalam piksel.
- `y_minor_dist` (int, default=20): Jarak antara garis horizontal grid minor dalam piksel.
- `minor_color` (str, default="black"): Warna garis grid minor.
- `minor_opacity` (float, default=0.25): Opasitas garis grid minor, antara 0.0 dan 1.0.
- `minor_thickness` (int, default=1): Ketebalan garis grid minor.

## Metode: `draw_minor_vertical_lines`

Menggambar garis vertikal grid minor pada layar.

### Parameter:

- `screen` (pygame.Surface): Surface Pygame tempat menggambar.
- `width` (int): Lebar layar.
- `height` (int): Tinggi layar.

## Metode: `draw_minor_horizontal_lines`

Menggambar garis horizontal grid minor pada layar.

### Parameter:

- `screen` (pygame.Surface): Surface Pygame tempat menggambar.
- `width` (int): Lebar layar.
- `height` (int): Tinggi layar.

## Metode: `draw_major_vertical_lines`

Menggambar garis vertikal grid utama dengan label pada layar.

### Parameter:

- `screen` (pygame.Surface): Surface Pygame tempat menggambar.
- `width` (int): Lebar layar.
- `height` (int): Tinggi layar.
- `font` (bool): Font yang digunakan untuk memberi label pada garis grid.

## Metode: `draw_major_horizontal_lines`

Menggambar garis horizontal grid utama dengan label pada layar.

### Parameter:

- `screen` (pygame.Surface): Surface Pygame tempat menggambar.
- `width` (int): Lebar layar.
- `height` (int): Tinggi layar.
- `font` (bool): Font yang digunakan untuk memberi label pada garis grid.

## Metode: `draw_grid`

Menggambar seluruh grid (garis minor dan utama dengan label) pada surface Pygame yang sedang aktif.

### Meninggalkan:

- `RuntimeError`: Jika tidak ada layar Pygame yang terbuka.
