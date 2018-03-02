import os,time
i=0
s='0'
while True:
	if i ==0:
		s1='s'
		d=' '
		y=' '
		x=' '
		b=' '
		a=' '
		n=' '
		a=' '
	if i==1:
		s1=' '
		d='s'
	if i==2:
		d=' '
		print('-_-')
	if i == 3:
		y='s'
		d=' '
	if i == 4:
		x='s'
		y=' '
	if i == 5:
		b='s'
		x=' '
	if i == 6:
		b=' '
		a='s'
	if i == 7:
		a=' '
		n='s'          
		i=-1
	print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
	print('$$$                           $$$')
	print('$           $$$$$$$$$$$         $')
	print('$         $$     12    $$       $')
	print('$       $$ '+d+"     "+s+"     "+y+' $$     $')
	print('$     $$     '+d+"   "+s+"   "+y+'     $$   $')
	print('$    $$        '+d+" "+s+" "+y+'        $$  $')
	print('$    $$9 '+s1+ ' '+s1+ " "+s1+' '+ s1+' O '+x+ ' '+x+ " "+x+' '+x+' 3$$  $')
	print('$    $$        '+n+" "+a+" "+b+'        $$  $')
	print('$     $$     '+n+"   "+a+"   "+b+'     $$   $')
	print('$       $$ '+n+"     "+a+"     "+b+' $$     $')
	print('$         $$     6     $$       $')
	print('$           $$$$$$$$$$$         $')
	print('$                               $')
	print('$$$                           $$$')
	print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
	time.sleep(0.5)
	os.system('cls')
	i+=1