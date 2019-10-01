def bottle_song(num):
	count = num
	while count >= 0:
		if count >= 2:
			print (f"{count} bottles of beer on the wall, {count} bottles of beer. Take one down and pass it around, {count - 1} bottles of beer on the wall.")
		elif count == 1:
			print ('1 bottle of beer on the wall, 1 bottle of beer. Take one down and pass it around, no more bottles of beer on the wall.')
		else:
			print (f"No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, {num} bottles of beer on the wall.")
		count = count - 1


bottle_song(100)
