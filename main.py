def hitung_total_panen(berat_kg, harga_per_kg):
    """Menghitung total harga hasil panen sebelum diskon."""
    return berat_kg * harga_per_kg

def hitung_diskon(total_harga, persentase_diskon):
    """Menghitung jumlah potongan harga berdasarkan persentase."""
    return total_harga * (persentase_diskon / 100)

if __name__ == "__main__":
    print("=== SISTEM PENCATATAN HASIL PANEN DIGITAL (TIN) ===")
    berat = float(input("Masukkan berat hasil panen (kg): "))
    harga = float(input("Masukkan harga per kg (Rp): "))
    
    total = hitung_total_panen(berat, harga)
    print(f"Total Harga Panen (Kotor): Rp {total:,.2f}")
    
    # Fitur Diskon
    persen_diskon = float(input("Masukkan persentase diskon (%): "))
    potongan = hitung_diskon(total, persen_diskon)
    total_akhir = total - potongan
    
    print(f"Potongan Diskon: Rp {potongan:,.2f}")
    print(f"Total Bayar (Bersih): Rp {total_akhir:,.2f}")
