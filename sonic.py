import random
import time
from web3 import Web3
from eth_account import Account
from colorama import Fore, Style, init
import shutil

# Inisialisasi colorama
init(autoreset=True)

# Konfigurasi jaringan
network_url = "https://rpc.testnet.soniclabs.com"
chain_id = 64165
private_key = "YOUR PRIVATE KEY EVM" # Masukan Private Key
explorer_url = "https://testnet.soniclabs.com/tx/0x"  # Base URL untuk explorer

# Menghubungkan ke jaringan Sonic Testnet
web3 = Web3(Web3.HTTPProvider(network_url))

# Memastikan koneksi berhasil
if not web3.is_connected():
    raise Exception("Gagal terhubung ke jaringan")

# Mendapatkan alamat dari private key
account = Account.from_key(private_key)
sender_address = account.address

# Header ASCII art
def print_header():
    ascii_art =  """
 __     ___ _    _ _            _     _ 
 \ \   / (_) | _(_) |_ ___  ___| |__ (_)
  \ \ / /| | |/ / | __/ _ \/ __| '_ \| |
   \ V / | |   <| | || (_) \__ \ | | | |
    \_/  |_|_|\_\_|\__\___/|___/_| |_|_|
"""
    # Center the ASCII art based on terminal width
    terminal_width = shutil.get_terminal_size().columns
    lines = ascii_art.strip().split('\n')
    centered_lines = [line.center(terminal_width) for line in lines]
    header = '\n'.join(centered_lines)

    # Print ASCII art with red color
    print(Fore.RED + header + Style.RESET_ALL)

    # Print description below ASCII art with 1 line gap
    description = "SonicLabs Testnet Bot"
    print()
    print(description.center(terminal_width))
    description = "Join our Telegram channel for updates: https://t.me/AirdropInsiderID"
    print()
    print(description.center(terminal_width))
    print()
    print()

# Pilihan bahasa
def select_language():
    while True:
        print()
        print("Pilih bahasa:")
        print("1. Bahasa Indonesia")
        print("2. English")
        choice = input("Masukkan pilihan (1/2): ")

        if choice == '1':
            return 'id'
        elif choice == '2':
            return 'en'
        else:
            print("Pilihan tidak valid. Silakan pilih 1 atau 2.")
            print()

# Pesan berdasarkan bahasa
def get_messages(language):
    if language == 'id':
        return {
            'success': "✅ Transaksi sukses! Link: {}",
            'failure': "❌ Transaksi gagal. Link: {}",
            'sender': "📤 Alamat pengirim: {}",
            'receiver': "📥 Alamat penerima: {}",
            'amount': "💸 Jumlah S yang dikirim: {} S",
            'gas': "⛽ Gas digunakan: {}",
            'block': "🗳️  Nomor blok: {}",
            'balance': "💰 Saldo terkini: {} S",
            'total': "🏆 Total sukses: {}",
            'total_tx': "🔢 Total transaksi: {}",
            'amount_prompt': "Masukkan jumlah S yang ingin dikirim (default 0.000001, maksimum 0.0001): "
        }
    else:  # English
        return {
            'success': "✅ Transaction successful! Link: {}",
            'failure': "❌ Transaction failed. Link: {}",
            'sender': "📤 Sender address: {}",
            'receiver': "📥 Receiver address: {}",
            'amount': "💸 Amount S sent: {} S",
            'gas': "⛽ Gas used: {}",
            'block': "🗳️  Block number: {}",
            'balance': "💰 Current balance: {} S",
            'total': "🏆 Total successful: {}",
            'total_tx': "🔢 Total transactions: {}",
            'amount_prompt': "Enter the amount of S to send (default 0.000001, maximum 0.0001): "
        }

# Pilihan jumlah token
def select_amount(language):
    messages = get_messages(language)
    while True:
        try:
            amount = float(input(messages['amount_prompt']) or 0.000001)
            if 0 < amount <= 0.0001:
                return amount
            else:
                print("Jumlah tidak valid. Jumlah harus lebih dari 0 dan tidak lebih dari 0.0001.")
        except ValueError:
            print("Input tidak valid. Masukkan angka.")

# Fungsi untuk mengirim transaksi
def send_transaction(to_address, amount):
    # Membuat transaksi
    nonce = web3.eth.get_transaction_count(sender_address)  # Menggunakan `get_transaction_count`
    tx = {
        'nonce': nonce,
        'to': Web3.to_checksum_address(to_address),  # Pastikan alamat dalam bentuk checksum
        'value': web3.to_wei(amount, 'ether'),  # Jumlah S yang akan dikirim
        'gas': 21000,  # Gas limit untuk transaksi sederhana
        'gasPrice': web3.eth.gas_price,
        'chainId': chain_id
    }

    # Menandatangani transaksi
    signed_tx = web3.eth.account.sign_transaction(tx, private_key)

    # Mengirim transaksi
    tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)

    # Menunggu transaksi untuk dimasukkan ke dalam blok
    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

    return tx_hash.hex(), tx_receipt, amount

# Alamat tujuan secara acak dengan checksum
def get_random_address():
    random_address = '0x' + ''.join(random.choices('0123456789abcdef', k=40))
    return Web3.to_checksum_address(random_address)

# Fungsi utama
def main():
    total_tx = 0
    successful_tx = 0
    header_displayed = False

    language = select_language()
    messages = get_messages(language)

    amount = select_amount(language)

    try:
        while True:
            if not header_displayed:
                print_header()  # Cetak header hanya sekali
                header_displayed = True

            to_address = get_random_address()
            tx_hash, tx_receipt, sent_amount = send_transaction(to_address, amount)

            # Menghapus awalan "0x" dari hash transaksi
            tx_hash_no_prefix = tx_hash[2:]
            tx_link = explorer_url + tx_hash_no_prefix  # Membuat tautan txHash tanpa "0x"

            # Format jumlah S yang dikirim
            formatted_amount = f"{sent_amount:.6f}"

            # Menampilkan informasi tambahan
            if tx_receipt['status'] == 1:
                successful_tx += 1
                # Mendapatkan saldo terkini
                current_balance = web3.eth.get_balance(sender_address)
                # Format saldo terkini
                formatted_balance = f"{web3.from_wei(current_balance, 'ether'):.6f}"
                # Menampilkan informasi tambahan dengan emotikon/simbol dan warna
                print(messages['success'].format(Fore.GREEN + tx_link + Style.RESET_ALL))
                print(messages['sender'].format(sender_address))
                print(messages['receiver'].format(Web3.to_checksum_address(to_address)))
                print(messages['amount'].format(formatted_amount))
                print(messages['gas'].format(tx_receipt['gasUsed']))
                print(messages['block'].format(tx_receipt['blockNumber']))
                print(messages['balance'].format(formatted_balance))
                print(messages['total'].format(successful_tx))
            else:
                print(messages['failure'].format(Fore.GREEN + tx_link + Style.RESET_ALL))
                print(messages['sender'].format(sender_address))
                print(messages['receiver'].format(Web3.to_checksum_address(to_address)))
                print(messages['amount'].format(formatted_amount))

            # Menambahkan baris kosong antar transaksi
            print()

            # Jeda 3 detik antar transaksi
            time.sleep(2)

    except KeyboardInterrupt:
        print("Bot Stopped.")

if __name__ == "__main__":
    main()
