from .Shop import Shop
from .InvoiceRepository import InvoiceRepository
from .Warehouse import Warehouse
from .exceptions import OutOfStore


def main():
    # Inicjalizacja systemu
    warehouse = Warehouse()
    invoice_repo = InvoiceRepository()
    shop = Shop(invoice_repo, warehouse)

    # Przykładowe produkty w magazynie
    warehouse.add_product("cukierki", 50, 2.99)
    warehouse.add_product("chleb", 30, 3.50)
    warehouse.add_product("mleko", 20, 2.10)

    while True:
        print("\n=== MENU GŁÓWNE ===")
        print("1. Dodaj produkt do magazynu")
        print("2. Sprzedaj produkty (generuj fakturę)")
        print("3. Zwróć produkty (całość/część)")
        print("4. Pokaż stan magazynu")
        print("5. Pokaż wszystkie faktury")
        print("0. Wyjdź")

        choice = input("Wybierz opcję: ")

        if choice == "1":
            # Dodawanie produktu do magazynu
            name = input("Nazwa produktu: ")
            quantity = int(input("Ilość: "))
            price = float(input("Cena: "))
            warehouse.add_product(name, quantity, price)
            print(f"Dodano {quantity} szt. produktu '{name}' do magazynu.")

        elif choice == "2":
            # Sprzedaż (generowanie faktury)
            customer = input("Imię klienta: ")
            items = []
            while True:
                print("\nDostępne produkty:")
                for product, info in warehouse.products.items():
                    print(f"- {product}: {info['quantity']} szt. (cena: {info['price']} zł)")

                product = input("Podaj nazwę produktu (lub 'koniec'): ")
                if product.lower() == "koniec":
                    break
                if product not in warehouse.products:
                    print("Nie ma takiego produktu!")
                    continue
                quantity = int(input(f"Ilość '{product}': "))
                items.append((product, quantity))

            try:
                invoice = shop.buy(customer, items)
                print(f"Wygenerowano fakturę nr {invoice.number} dla {customer}.")
            except OutOfStore as e:
                print(f"Błąd: {e}")

        elif choice == "3":
            # Zwrot towaru
            invoice_number = int(input("Numer faktury do zwrotu: "))
            invoice = invoice_repo.find_by_number(invoice_number)
            if not invoice:
                print("Nie znaleziono faktury!")
                continue

            print(f"\nFaktura nr {invoice.number}, klient: {invoice.customer}")
            print("Produkty na fakturze:")
            for idx, (product, quantity) in enumerate(invoice.items, 1):
                print(f"{idx}. {product}: {quantity} szt.")

            return_option = input("Zwrócić wszystko? (T/N): ").strip().upper()
            if return_option == "T":
                shop.returning_goods(invoice)
                print("Zwrócono wszystkie produkty.")
            else:
                items_to_return = []
                product_name = input("Nazwa produktu do zwrotu: ")
                quantity = int(input("Ilość do zwrotu: "))
                items_to_return.append((product_name, quantity))
                shop.returning_goods(invoice, items_to_return)
                print(f"Zwrócono {quantity} szt. produktu '{product_name}'.")

        elif choice == "4":
            # Wyświetl stan magazynu
            print("\nStan magazynu:")
            for product, info in warehouse.products.items():
                print(f"- {product}: {info['quantity']} szt. | Cena: {info['price']} zł")

        elif choice == "5":
            # Wyświetl faktury
            print("\nWystawione faktury:")
            for invoice in invoice_repo.data_source:
                print(f"Nr {invoice.number}: {invoice.customer}, produkty: {invoice.items}")

        elif choice == "0":
            break

        else:
            print("Nieprawidłowa opcja!")


if __name__ == "__main__":
    main()