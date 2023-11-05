# Prototype_arbitrage

## Opis
Prototyp bota arbitrażowego symulującego przeprowadzanie transakcji na giełdach kryptowalut.
Po dokonaniu sprawdzenia giełd pod kątem braku prowizji od przeprowadzania transakcji znalazłem dwie giełdy:
* MEXC
* Lykke
* Binance ale tylko w przypadku wymiany za pośrednctwem stablecoina BUSD.

Bot bierze pod uwage tylko jedną parę walutową: np. BTC/BUSD.
Wykonuje arbitraż na dwóch giełdach bez tranferu środków pomiędzy nimi. Opiera się na mechanizmie "na jednej giełdzie kup, na drugiej sprzedaj tyle samo".

## Instalacja
1. Pobranie repozytorium
2. Uruchomienie pliku Main.py

Logi zapisywane są do pliku results/log.txt

W folderze results_analysis znajduje się skrypt, który analizuje logi i zapisuje do formatu - data:procent_zysku_ze_sprzedaży:procent_zysku_z_kupna i zapisuje wyniki do pliku results_analysis/price_difference.txt

## Przykładowy wynik
```
2023-11-01 22:17:02,359 - INFO: Kupiono 0.85124 BTC na giełdzie Binance po cenie 35320.04000 USDT 
Sprzedano 0.85124 BTC na giełdzie Mexc po cenie 35324.37000 USDT 
Zysk: 3.68585 USDT
Stan konta na giełdzie Binance: 0.00000 USDT oraz 0.92176 BTC 
Stan konta na giełdzie Mexc: 30069.35035 USDT oraz 0.07824 BTC


2023-11-01 22:17:30,783 - INFO: Kupiono 0.85029 BTC na giełdzie Mexc po cenie 35363.81000 USDT 
Sprzedano 0.85029 BTC na giełdzie Binance po cenie 35366.95000 USDT 
Zysk: 2.66990 USDT
Stan konta na giełdzie Mexc: 0.00000 USDT oraz 0.92853 BTC 
Stan konta na giełdzie Binance: 30072.02024 USDT oraz 0.07147 BTC


2023-11-01 22:18:36,639 - INFO: Kupiono 0.84823 BTC na giełdzie Binance po cenie 35452.72000 USDT 
Sprzedano 0.84823 BTC na giełdzie Mexc po cenie 35457.81000 USDT 
Zysk: 4.31748 USDT
Stan konta na giełdzie Binance: 0.00000 USDT oraz 0.91970 BTC 
Stan konta na giełdzie Mexc: 30076.33773 USDT oraz 0.08030 BTC


2023-11-01 22:19:29,823 - INFO: Kupiono 0.85049 BTC na giełdzie Mexc po cenie 35363.47000 USDT 
Sprzedano 0.85049 BTC na giełdzie Binance po cenie 35365.51000 USDT 
Zysk: 1.73500 USDT
Stan konta na giełdzie Mexc: 0.00000 USDT oraz 0.93079 BTC 
Stan konta na giełdzie Binance: 30078.07273 USDT oraz 0.06921 BTC
```

## Przykładowy wynik analizy logów
```
2023-11-01 22:17:02,359 : 0.0122578 % : 0.0122593 %
2023-11-01 22:17:30,783 : 0.0088783 % : 0.0088791 %
2023-11-01 22:18:36,639 : 0.0143551 % : 0.0143571 %
2023-11-01 22:19:29,823 : 0.0057683 % : 0.0057687 %
```

## Propozycje rozwoju
* Sparametryzowanie wyboru pary walutowej
* Rozszerzenie liczby giełd
* Dodanie sprawdzenia wolumenu dostępnej waluty na giełdzie 
* Dodanie warunku na minimalny procent zysku z transakcji
* Wczytywanie parametrów portfela z pliku konfiguracyjnego
* Rozwiązanie limitu requestów na giełdach (API z uwierzytelnieniem)