class ContactManager:
    def __init__(self):
        self.contacts = []

    def create_contact(self, name, phone_number, email):
        contact = {
            'name': name,
            'phone_number': phone_number,
            'email': email
        }
        self.contacts.append(contact)
        print("Kontak berhasil ditambahkan.")

    def read_contacts(self):
        if self.contacts:
            print("Daftar Kontak:")
            for index, contact in enumerate(self.contacts):
                print(f"{index + 1}. Nama: {contact['name']}, No. Telepon: {contact['phone_number']}, Email: {contact['email']}")
        else:
            print("Daftar kontak kosong.")

    def update_contact(self, index, name, phone_number, email):
        if 0 <= index < len(self.contacts):
            self.contacts[index] = {
                'name': name,
                'phone_number': phone_number,
                'email': email
            }
            print("Kontak berhasil diperbarui.")
        else:
            print("Indeks kontak tidak valid.")

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            del self.contacts[index]
            print("Kontak berhasil dihapus.")
        else:
            print("Indeks kontak tidak valid.")


def main():
    contact_manager = ContactManager()
    
    while True:
        print("\nPilihan Menu:")
        print("1. Tambah Kontak")
        print("2. Lihat Daftar Kontak")
        print("3. Perbarui Kontak")
        print("4. Hapus Kontak")
        print("5. Keluar")

        choice = input("Masukkan pilihan (1/2/3/4/5): ")

        if choice == '1':
            name = input("Masukkan nama kontak: ")
            phone_number = input("Masukkan nomor telepon kontak: ")
            email = input("Masukkan email kontak: ")
            contact_manager.create_contact(name, phone_number, email)
        elif choice == '2':
            contact_manager.read_contacts()
        elif choice == '3':
            index = int(input("Masukkan indeks kontak yang akan diperbarui: "))
            name = input("Masukkan nama baru: ")
            phone_number = input("Masukkan nomor telepon baru: ")
            email = input("Masukkan email baru: ")
            contact_manager.update_contact(index - 1, name, phone_number, email)
        elif choice == '4':
            index = int(input("Masukkan indeks kontak yang akan dihapus: "))
            contact_manager.delete_contact(index - 1)
        elif choice == '5':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()
