per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = input("Введите сумму вклада:")
bankTKB = int(money) * (per_cent['ТКБ']) / 100
banкCKB = int(money) * (per_cent['СКБ']) / 100
bankVTB = int(money) * (per_cent['ВТБ']) / 100
bankSBER = int(money) * (per_cent['СБЕР']) / 100
print('ТКБ-', round((bankTKB), 2))
print('СКБ-', round((banкCKB), 2))
print('ВТБ-', round((bankVTB), 2))
print('СБЕР-', round((bankSBER), 2))
deposit = [(bankTKB), (banкCKB), (bankVTB), (bankSBER)]
depositi = max(deposit)
max_val_key = max(per_cent, key=per_cent.get)
print("Максимальная сумма дохода:", round((depositi), 2), "в", (max_val_key), "банке")