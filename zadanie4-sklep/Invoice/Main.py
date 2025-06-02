# from Invoice.Shop import Shop
# from Invoice.InvoiceRepository import InvoiceRepository

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Invoice.InvoiceObject import InvoiceObject
from Invoice.Warehouse import Warehouse
from Invoice.exceptions import OutOfStore
from Invoice.Shop import Shop
from Invoice.InvoiceRepository import InvoiceRepository

# Inicjalizacja systemu
warehouse = Warehouse()
invoice_repo = InvoiceRepository()
shop = Shop(invoice_repo, warehouse)

def main():
    global warehouse, invoice_repo, shop

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
        print("6. Zapisz faktury do pliku")
        print("7. Usuń faktury")
        print("0. Wyjdź")

        choice = input("Wybierz opcję: ")

        if choice == "1":
            # Dodawanie produktu do magazynu
            name = input("Nazwa produktu: ")
            quantity = int(input("Ilość: "))
            price = float(input("Cena: ").replace(',', '.'))
            warehouse.add_product(name, quantity, price)
            print(f"Dodano {quantity} szt. produktu '{name}' do magazynu.")

        elif choice == "2":
            # Sprzedaż (generowanie faktury)
            customer = input("Imię klienta: ")
            items = []      # nazwa produktu, ilość
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
                print(f"\nWygenerowano fakturę nr {invoice.number} dla {customer}:")
                print("Zamówione produkty:")
                total = 0.0
                for product, quantity in invoice.items:
                    price = warehouse.get_product_info(product)["price"]
                    item_total = price * quantity
                    total += item_total
                    print(f"- {product}: {quantity} szt. x {price:.2f} zł = {item_total:.2f} zł")
                print(f"Suma: {total:.2f} zł")
                print(f"Faktura została zapisana w systemie i pliku invoices.txt")
            except OutOfStore as e:
                print(f"Błąd: {e}")

        elif choice == "3":
            # Zwrot towaru
            print("\nDostępne faktury:")
            for invoice in invoice_repo.data_source:
                print(f"Nr {invoice.number}: {invoice.customer}, produkty: {invoice.items}")

            try:
                invoice_number = int(input("\nNumer faktury do zwrotu: "))
            except ValueError:
                print("Nieprawidłowy numer faktury!")
                continue

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
                if not any(product_name == product for product, _ in invoice.items):
                    print("Ten produkt nie występuje na fakturze!")
                    continue
                try:
                    quantity = int(input("Ilość do zwrotu: "))
                    if quantity <= 0:
                        print("Ilość musi być większa od 0!")
                        continue
                    # Sprawdzamy czy nie zwracamy więcej niż kupiono
                    current_qty = next(qty for product, qty in invoice.items if product == product_name)
                    if quantity > current_qty:
                        print(f"Nie można zwrócić więcej niż {current_qty} szt.!")
                        continue
                    items_to_return.append((product_name, quantity))
                    shop.returning_goods(invoice, items_to_return)
                    print(f"Zwrócono {quantity} szt. produktu '{product_name}'.")
                except ValueError:
                    print("Nieprawidłowa ilość!")

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


        elif choice == "6":
            if invoice_repo.save_to_file():
                print("Faktury zostały zapisane do pliku invoices.txt")


        elif choice == "7":
            if not invoice_repo.data_source:
                print("Brak faktur do usunięcia.")
                continue

            print("\nDostępne faktury:")
            for invoice in invoice_repo.data_source:
                print(f"Nr {invoice.number}: {invoice.customer}, produkty: {invoice.items}")

            delete_option = input("Usunąć wszystkie faktury? (T/N): ").strip().upper()

            if delete_option == "T":
                invoice_repo.delete_all()
                print("Usunięto wszystkie faktury.")
            else:
                try:
                    invoice_number = int(input("Podaj numer faktury do usunięcia: "))
                    invoice = invoice_repo.find_by_number(invoice_number)
                    if invoice:
                        invoice_repo.delete(invoice)
                        print(f"Usunięto fakturę nr {invoice_number}.")
                    else:
                        print("Nie znaleziono faktury o podanym numerze.")
                except ValueError:
                    print("Nieprawidłowy numer faktury!")

        elif choice == "0":
            break

        else:
            print("Nieprawidłowa opcja!")


if __name__ == "__main__":
    main()