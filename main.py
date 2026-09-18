# main.py - Tahap Awal

def hitung_total_panen(berat_kg, harga_per_kg):
    """Menghitung total harga hasil panen sebelum diskon."""
    return berat_kg * harga_per_kg

if __name__ == "__main__":
    print("=== SISTEM PENCATATAN HASIL PANEN DIGITAL (TIN) ===")
    berat = float(input("Masukkan berat hasil panen (kg): "))
    harga = float(input("Masukkan harga per kg (Rp): "))
    
    total = hitung_total_panen(berat, harga)
    print(f"Total Harga Panen: Rp {total:,.2f}")
