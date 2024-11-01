import os

def rename_folders():
    # Dapatkan direktori saat ini
    current_dir = os.getcwd()
    
    # Loop melalui semua item di direktori
    for item in os.listdir(current_dir):
        if os.path.isdir(item) and "Taco Tribe " in item:
            # Nama baru adalah nama folder tanpa "Taco Tribe "
            new_name = item.replace("Taco Tribe ", "")
            
            # Rename folder
            try:
                os.rename(item, new_name)
                print(f"Berhasil mengubah nama: {item} -> {new_name}")
            except Exception as e:
                print(f"Gagal mengubah nama {item}: {str(e)}")

if __name__ == "__main__":
    rename_folders()
