# SonicLabs Testnet Bot

Bot ini dirancang untuk mengirimkan token S di jaringan Sonic Testnet secara otomatis. Bot akan mengirim token ke alamat yang dihasilkan secara acak, dengan kemampuan untuk memilih bahasa, jumlah token yang akan dikirim, dan menampilkan hasil transaksi.

## Fitur

- Mengirim token S ke alamat yang dihasilkan secara acak di jaringan Sonic Testnet.
- Pilihan bahasa untuk tampilan output: Bahasa Indonesia atau Inggris.
- Pilihan jumlah token yang akan dikirim (default: 0.000001 S, maksimum: 0.0001 S).
- Menampilkan informasi transaksi yang berhasil, termasuk saldo terkini, gas yang digunakan, dan nomor blok.
- Menampilkan hanya link explorer untuk transaksi yang berhasil.

## Prerequisites

- Python 3.x
- Web3.py
- Colorama

## Instalasi

1. Clone repositori ini:

    ```sh
    git clone https://github.com/vinskasenda/soniclabs-bot.git
    ```

2. Masuk ke direktori proyek:

    ```sh
    cd soniclabs-testnet-bot
    ```

3. Install dependensi yang diperlukan:

    ```sh
    pip install web3 colorama
    ```

## Konfigurasi

1. Buka file `sonic.py` dan pastikan untuk mengganti `private_key` dengan kunci pribadi Anda yang valid.
2. Pastikan URL RPC dan `chain_id` sesuai dengan jaringan Sonic Testnet yang Anda gunakan.

## Penggunaan

1. Jalankan skrip bot dengan perintah:

    ```sh
    python sonic.py
    ```

2. Ikuti instruksi untuk memilih bahasa, jumlah token yang akan dikirim, dan bot akan mulai mengirimkan transaksi.

