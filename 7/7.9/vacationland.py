# 梦想的度假胜地

vacationlands = []

active = True
while active:
    vacationland = input('你梦想的度假胜地是哪里？\n')
    if vacationland == 'q':
        break
    vacationlands.append(vacationland)

print('人们梦想的度假胜地有:\n')
print(vacationlands)
