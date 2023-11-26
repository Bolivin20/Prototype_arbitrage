#!/bin/bash

echo "Uruchamianie wyszukiwania arbitrażu..."
python3 Main.py &

main_pid=$!

echo "Naciśnij 'k' aby zakończyć..."
read -n 1 key

if [ "$key" == "k" ]; then
    echo "Zatrzymywanie wyszukiwania arbitrażu..."
    kill $main_pid
fi

echo "Rysowanie wykresów..."
python3 results_analysis/drawChart.py BTC
python3 results_analysis/drawChart.py ETH
python3 results_analysis/drawChart.py DOGE

python3 results_analysis/drawChartPercentage.py BTC
python3 results_analysis/drawChartPercentage.py ETH
python3 results_analysis/drawChartPercentage.py DOGE
