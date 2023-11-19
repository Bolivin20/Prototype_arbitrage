import argparse
import pandas as pd
import matplotlib.pyplot as plt

# Dodaj obsługę argumentów wiersza poleceń
parser = argparse.ArgumentParser(description='Generate and save arbitrage profit chart.')
parser.add_argument('symbol', type=str, help='Cryptocurrency symbol')
args = parser.parse_args()

# Wczytaj dane z pliku CSV
filename = f'results/{args.symbol}_chart_data.csv'
data = pd.read_csv(filename, header=None, names=['Timestamp', 'Exchange1', 'Exchange2', 'Value', 'Profit'])

# Przekształć kolumnę Timestamp na obiekt datetime
data['Timestamp'] = pd.to_datetime(data['Timestamp'], format='%Y-%m-%d %H:%M:%S')

# Utwórz wykres
plt.figure(figsize=(10, 6))
plt.plot(data['Timestamp'], data['Profit'], label=f'{args.symbol} Arbitrage Profit', marker='o')

# Dodaj etykiety i tytuły
plt.xlabel('Time')
plt.ylabel('Profit')
plt.title(f'Arbitrage Profit for {args.symbol}')
plt.legend()

# Zapisz wykres do pliku
output_filename = f'charts/{args.symbol}_chart.png'
plt.savefig(output_filename)

# Pokaż wykres
plt.show()
