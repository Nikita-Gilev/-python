goods = []
features = {'наименование': '', 'стоимость': '', 'количество': '', 'единицы': ''}
analytics = {'наименование': [], 'стоимость': [], 'количество': [], 'единицы': []}
num = 0
feature_ = None
control = None
while True:
    control = input("для выхода нажмите 'Q', для продолжения нажмите 'Enter', вывод аналитики нажмите 'A'").upper()
    if control == 'Q':
        break
    num += 1
    if control == 'A':
        print(f'\n аналитика \n {"-" * 30}')
        for key, value in analytics.items():
            print(f'{key[:25]:>30}: {value}')
            print("-" * 30)
    for f in features.keys():
        feature_ = input(f'Input feature "{f}"')
        features[f] = int(feature_) if (f == 'стоимость' or f == 'количество') else feature_
        analytics[f].append(features[f])
    goods.append((num, features))
