#Подключаем библиотеки
import os,time
from colorama import Fore, Back, Style, init

i=0

#Используем цвета и запускаем бесконечный цикл
az=Fore.WHITE + Style.BRIGHT+'.'
s=Fore.BLACK + Style.BRIGHT + '0'
while True:
	#Условия "движения"
	if i ==0:
		s1=Fore.WHITE + Style.BRIGHT +'.'
		d=Fore.WHITE + Style.BRIGHT +'.'
		y=Fore.WHITE + Style.BRIGHT +'.'
		x=Fore.WHITE + Style.BRIGHT +'.'
		b=Fore.WHITE + Style.BRIGHT +'.'
		a=Fore.WHITE + Style.BRIGHT +'.'
		n=Fore.WHITE + Style.BRIGHT +'.'
		a=Fore.WHITE + Style.BRIGHT +'.'
	if i==1:
		y=Fore.BLACK + Style.BRIGHT + 's'
	if i==2:
		y=Fore.WHITE + Style.BRIGHT +'.'
		x=Fore.BLACK + Style.BRIGHT +'s'
	if i == 3:
		b=Fore.BLACK + Style.BRIGHT +'s'
		x=Fore.WHITE + Style.BRIGHT +'.'
	if i == 4:
		a=Fore.BLACK + Style.BRIGHT +'s'
		b=Fore.WHITE + Style.BRIGHT +'.'
	if i == 5:
		n=Fore.BLACK + Style.BRIGHT +'s'
		a=Fore.WHITE + Style.BRIGHT +'.'
	if i == 6:
		n=Fore.WHITE + Style.BRIGHT +'.'
		s1=Fore.BLACK + Style.BRIGHT +'s'
	if i == 7:
		s1=Fore.WHITE + Style.BRIGHT +'.'
		d=Fore.BLACK + Style.BRIGHT +'s'
		i=-1
	#Выводим на экран (Пришло время "анимации")
	print(Fore.BLACK + Style.BRIGHT + '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
	print(Fore.BLACK + Style.BRIGHT + '$$$                           $$$')
	print(Fore.BLACK + Style.BRIGHT + '$         '+Fore.YELLOW + Style.BRIGHT + ' $$$$$$$$$$$  '+Fore.BLACK + Style.BRIGHT + '        $')
	print(Fore.BLACK + Style.BRIGHT + '$      '+Fore.YELLOW + Style.BRIGHT + '  $$'+az+az+az+az+az+'12'+az+az+az+az+''+Fore.YELLOW + Style.BRIGHT + '$$    '+Fore.BLACK + Style.BRIGHT + '    $')
	print(Fore.BLACK + Style.BRIGHT + '$    '+Fore.YELLOW + Style.BRIGHT + '  $$ '+d+az+az+az+az+az+s+az+az+az+az+az+y+''+Fore.YELLOW + Style.BRIGHT + ' $$   '+Fore.BLACK + Style.BRIGHT + '   $')
	print(Fore.BLACK + Style.BRIGHT + '$    '+Fore.YELLOW + Style.BRIGHT + '$$'+az+az+az+az+az+d+az+az+az+s+az+az+az+y+az+az+az+az+az+''+Fore.YELLOW + Style.BRIGHT + '$$  '+Fore.BLACK + Style.BRIGHT + '  $')
	print(Fore.BLACK + Style.BRIGHT + '$  '+Fore.YELLOW + Style.BRIGHT + ' $$'+az+az+az+az+az+az+az+az+d+az+s+az+y+az+az+az+az+az+az+az+az+''+Fore.YELLOW + Style.BRIGHT + '$$'+Fore.BLACK + Style.BRIGHT + '   $')
	print(Fore.BLACK + Style.BRIGHT + '$ '+Fore.YELLOW + Style.BRIGHT + '  $$'+Fore.WHITE + Style.BRIGHT+'9 '+s1+ ' '+s1+ " "+s1+' '+ s1+''+Fore.WHITE + Style.BRIGHT+' O '+x+ ' '+x+ " "+x+' '+x+''+Fore.WHITE + Style.BRIGHT+' 3'+Fore.YELLOW + Style.BRIGHT + '$$'+Fore.BLACK + Style.BRIGHT + '   $')
	print(Fore.BLACK + Style.BRIGHT + '$ '+Fore.YELLOW + Style.BRIGHT + '  $$'+az+az+az+az+az+az+az+az+n+az+a+az+b+az+az+az+az+az+az+az+az+''+Fore.YELLOW + Style.BRIGHT + '$$ '+Fore.BLACK + Style.BRIGHT + '  $')
	print(Fore.BLACK + Style.BRIGHT + '$ '+Fore.YELLOW + Style.BRIGHT + '   $$'+az+az+az+az+az+n+az+az+az+a+az+az+az+b+az+az+az+az+az+''+Fore.YELLOW + Style.BRIGHT + '$$  '+Fore.BLACK + Style.BRIGHT + '  $')
	print(Fore.BLACK + Style.BRIGHT + '$   '+Fore.YELLOW + Style.BRIGHT + '   $$.'+n+az+az+az+az+az+a+az+az+az+az+az+b+az+''+Fore.YELLOW + Style.BRIGHT + '$$   '+Fore.BLACK + Style.BRIGHT + '   $')
	print(Fore.BLACK + Style.BRIGHT + '$   '+Fore.YELLOW + Style.BRIGHT + '     $$'+az+az+az+az+az+'6'+az+az+az+az+az+''+Fore.YELLOW + Style.BRIGHT + '$$      '+Fore.BLACK + Style.BRIGHT + '  $')
	print(Fore.BLACK + Style.BRIGHT + '$    '+Fore.YELLOW + Style.BRIGHT + '      $$$$$$$$$$$      '+Fore.BLACK + Style.BRIGHT + '    $')
	print(Fore.BLACK + Style.BRIGHT + '$                               $')
	print(Fore.BLACK + Style.BRIGHT + '$$$                           $$$')
	print(Fore.BLACK + Style.BRIGHT + '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
	time.sleep(0.5)
	os.system('cls')
	i+=1
