import time
# for i in range(0,99999):
# 	time.sleep(.9)
# 	print(i)
	# print('Internet is an h aa a  ads d sfsfffd fd fd')

# if __name__ == '__main__':
# 	print('Here it goes')
# 	time.sleep(2)
# 	print("This is the beginnig")

from pathlib import Path
p = Path('.')
print('Printing subdirectories')
print([x for x in p.iterdir() if x.is_dir()])
print("Printing Files")
# print(list(p.glob('*.py')))