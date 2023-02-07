per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = input("Введите сумму вклада:")
bankТКБ = int(money) * (per_cent['ТКБ']) / 100
banкСКБ = int(money) * (per_cent['СКБ']) / 100
bankВТБ = int(money) * (per_cent['ВТБ']) / 100
bankСБЕР = int(money) * (per_cent['СБЕР']) / 100
print('ТКБ-', (bankТКБ))
print('СКБ-', (banкСКБ))
print('ВТБ-', (bankВТБ))
print('СБЕР-', (bankСБЕР))
deposit = [int(bankТКБ), int(banкСКБ), int(bankВТБ), int(bankСБЕР)]
depositi = max(deposit)

max_val_key = max(per_cent, key=per_cent.get)
print("Максимальная сумма дохода:", int(depositi), "в", (max_val_key), "банке")



