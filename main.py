per_cent = {
    'ТКБ': 5.6,
    'СКБ': 5.9,
    'ВТБ': 4.28,
    'СБЕР': 4.0
}

money = int(input('Введите сумму вклада: '))

deposit = []
deposit.append(int(per_cent.get('ТКБ') * money/100))
deposit.append(int(per_cent.get('СКБ') * money/100))
deposit.append(int(per_cent.get('ВТБ') * money/100))
deposit.append(int(per_cent.get('СБЕР') * money/100))

print(deposit)

print(f'Максимальная сумма, которую вы можете заработать -  {max(deposit)}')