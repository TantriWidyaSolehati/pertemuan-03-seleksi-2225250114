# Pertemuan 03 Seleksi Python
- Nama: Tantri Widya Solehati
- NIM: 2225250114
- Kelas: 3F

## Tujuan
Menulis program seleksi if, if-else, kondisi majemuk, dan nested if.

## Cara Menjalankan
 1. Buka terminal di folder project:
   ```bash  
    python3 tugas/analisis_persamaan_kuadrat.py

## Algoritma Tugas
1. **Mulai** program.
2. **Input data** yang diperlukan (koefisien variabel a, b, c).
3. **Periksa kondisi awal**:
   - Jika a=0 → tampilkan "Bukan persamaan kuadrat".
   - Jika valid → lanjut ke proses berikutnya yaitu menghitung diskriminan.
4. **Lakukan perhitungan utama** sesuai rumus diskriminan (D = b**2 - 4*a*c)
5. **Bandingkan hasil** dengan syarat tertentu.
    - D=0 → akar-akar kembar
      - melakukan perhitungan untuk menentukan akarnya (x = -b / (2*a))
    - D>0 → akar-akar real
      - melakukan perhitungan untuk menentukan akarnya:
      x1 = (-b + D**0.5) / (2*a)
      x2 = (-b - D**0.5) / (2*a)  
    - D<0 → akar-akar imajiner
6. **Tampilkan output** hasil perhitungan.
7. **Selesai**.

## Hasil Pengujian
| Test Case | Input            |       Output Diharapkan      |        Output Aktual        |   Status  |
|-----------|------------------|------------------------------|-----------------------------|-----------|
| 1         | a=1, b=-5, c=6   | D=1, Dua akar real: 3 dan 2  | D=1, Dua akar real: 3 dan 2 |   Sesuai  |
| 2         | a=1, b=2, c=1    | D=0, akar kembar: -1         | D=0, akar kembar: -1        |   Sesuai  |
| 3         | a=1, b=0, c=1    | D=-4, Tidak ada akar real    | D=-4, Tidak ada akar real   |   Sesuai  |
| 4         | a=0, b=2, c=3    | Bukan persamaan kuadrat      | Bukan persamaan kuadrat     |   Sesuai  |

## Refleksi
- **Kesalahan logika:** Kondisi `D == 0` ditempatkan di dalam `if D > 0`, sehingga tidak bisa dijalankan. serta Pesan "tidak memiliki akar real" juga salah posisi masih di dalam kondisi `D == 0`.  
- **Perbaikan:** Gunakan struktur bercabang sejajar (`if`, `else`) untuk memisahkan kasus D > 0, D == 0, dan D < 0.  
- **Hasil:** Program mampu menentukan jenis akar-akar persamaan kuadrat dengan benar (akar real berbeda, akar kembar, atau akar kompleks).