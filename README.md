# Лаборторная работа 1
## Задание 1 — Привет и возраст
```
name = input("Имя: ")
age = int(input("Возраст: "))
print(f"Привет, {name}! Через год тебе будет {age+1}.")
```
<img width="2818" height="1366" alt="src01 greeting" src="https://github.com/user-attachments/assets/4b4812e3-07b7-402d-9068-d270a7d5c2ee" />

## 
Задание 2 — Сумма и среднее
```
a=input('a: ')
b=input('b: ')
a=a.replace(',','.',1)
b=b.replace(',','.',1)
a=float(a)
b=float(b)
c=a+b
print(f'sum={c:.2f}; avg={(c/2):.2f}')
```
<img width="2739" height="1346" alt="src02_sum_avg" src="https://github.com/user-attachments/assets/504062a3-eb3d-41d0-a303-bb7db312239f" />

## Задание 3 — Чек: скидка и НДС
```
price = int(input('price = '))
discount= int(input('discount = '))
vat= int(input('vat = '))
base = price * (1-discount/100)
vat_amount = base * (vat/100)
total = base+ vat_amount
print(f'База после скидки: {base:.2f} ₽')
print(f'НДС: {vat_amount:.2f} ₽')
print(f'Итого к оплате: {total:.2f} ₽')
```
<img width="2838" height="1080" alt="src03_discount_vat" src="https://github.com/user-attachments/assets/4987a917-7a4b-47b5-9976-81861067af31" />

## Задание 4 — Минуты → ЧЧ:ММ
```
m = int(input('Минуты: '))
print(f'{m//60}:{m%60}')
```
<img width="2317" height="850" alt="src04_minutes_to_hhmm" src="https://github.com/user-attachments/assets/4c1f18a1-975e-44d2-9049-ed18fa858ead" />

## Задание 5 — Инициалы и длина строки
```
f=input('ФИО: ')
n=f.split()
f=f.replace(' ','')
print(f'Инициалы:  {n[0][:1]}{n[1][:1]}{n[2][:1]}.')
print(f'Длина (символы): {len(f)+2}')
```
<img width="1232" height="825" alt="scr05_initials_and_lenn (2)" src="https://github.com/user-attachments/assets/89e915f6-1bf1-46b6-be32-b741583bc337" />


## Задание 6*
```
n=int(input())
o=[]
z=[]
while n>0:
    f=input()
    n=n-1
    if 'True' in f:
        o.append(f)
    if 'False' in f:
        z.append(f)
print('out',len(o),len(z))
```
<img width="2536" height="1315" alt="6" src="https://github.com/user-attachments/assets/d6381491-7563-4061-919f-19f6936733bd" />



