# Wczytaj plik z logami
with open('../results/log.txt', 'r') as log_file:
    log_lines = log_file.readlines()

# Inicjalizacja słownika do przechowywania różnic cen kupna i ilości kupionego BTC
price_differences = {}

# Iteruj przez każdą linię logów
for line in log_lines:
    # Sprawdź, czy linia zawiera informacje o kupnie i sprzedaży
    if "Kupiono" in line:
        parts = line.split()
        date = parts[0]
        time = parts[1]
        buy_price = float(parts[12])
        #sell_price = float(parts[11])
        quantity = float(parts[5])

        # Oblicz różnicę cen kupna i ilość kupionego BTC
    if "Sprzedano" in line:
        parts = line.split()
        sell_price = float(parts[8])

        price_difference_sell = abs(sell_price - buy_price) / sell_price * 100
        price_difference_buy = abs(sell_price - buy_price) / buy_price * 100

        # Dodaj dane do słownika
        key = f"{date} {time}"
        price_differences[key] = (price_difference_sell, price_difference_buy)

# Zapisz różnice cen kupna do innego pliku
with open('price_differences.txt', 'w') as output_file:
    for key, value in price_differences.items():
        output_file.write(f"{key} : {value[0]:.7f} % : {value[1]:.7f} %\n")
