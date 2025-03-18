# Daftar destinasi dan biaya dalam ribuan rupiah
destinations = [
    {"name": "Gunung Rinjani", "total": 1500},  # 1.5 juta
    {"name": "Gili Trawangan", "total": 1000},   # 1.0 juta
    {"name": "Pantai Kuta Lombok", "total": 500}  # 0.5 juta
]

# Anggaran yang harus dicapai (dalam ribuan rupiah)
budget = 3000  # 3 juta rupiah dalam satuan ribu

# Fungsi backtracking untuk mencari kombinasi tepat 3 juta
def find_trip(destinations, budget, selected=None, index=0):
    if selected is None:
        selected = []

    total_cost = sum(d['total'] for d in selected)

    # Jika total biaya tepat 3 juta, kembalikan hasilnya
    if total_cost == budget:
        return selected  

    # Jika melebihi anggaran, hentikan pencarian
    if total_cost > budget:
        return None  

    for i in range(index, len(destinations)):
        # Salin daftar saat ini untuk rekursi (menghindari mutasi langsung)
        new_selected = selected + [destinations[i]]
        result = find_trip(destinations, budget, new_selected, i + 1)  # Rekursif
        if result:
            return result  # Langsung kembalikan solusi pertama yang valid

    return None  # Jika tidak ada kombinasi yang valid

def main():
    # Menjalankan algoritma
    result = find_trip(destinations, budget)

    # Menampilkan hasil
    if result:
        print("\n✅ Rencana Liburan (Total harus 3 juta rupiah):")
        for d in result:
            print(f"- {d['name']} (Biaya: {d['total']} ribu rupiah)")
        total_biaya = sum(d['total'] for d in result)
        print(f"\n💰 Total Biaya: {total_biaya} ribu rupiah")
        
        # Menampilkan penjelasan logika backtracking
        print("\n🔍 Penjelasan Logika Backtracking:")
        print("1. Program memeriksa berbagai kombinasi destinasi secara rekursif.")
        print("2. Jika kombinasi biaya mencapai 3 juta, program menyimpannya sebagai solusi.")
        print("3. Jika biaya melebihi anggaran, program menghentikan pencarian.")
        print("4. Program mencoba berbagai kemungkinan hingga menemukan kombinasi yang valid.")
        
        # Menampilkan kelebihan dan kekurangan backtracking
        print("\n📊 Analisis Backtracking:")
        print("✅ Kelebihan:")
        print("- Menjamin solusi optimal karena mencoba berbagai kemungkinan.")
        print("- Efektif untuk dataset kecil dengan kombinasi terbatas.")
        print("- Fleksibel, dapat digunakan dengan berbagai anggaran dan destinasi.")
        print("❌ Kekurangan:")
        print("- Tidak efisien jika jumlah destinasi sangat besar.")
        print("- Tidak selalu menemukan semua solusi, hanya yang pertama ditemukan.")
        print("- Rekursi bisa memakan banyak memori pada dataset besar.")
    else:
        print("❌ Tidak ada kombinasi yang tepat 3 juta rupiah.")

if __name__ == "__main__":
    main()
