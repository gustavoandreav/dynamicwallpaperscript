import os
import yaml
import time
import sys

def main():
	with open('config.yml', 'r') as file:
		config_file = yaml.safe_load(file)
		
	wallpaper_dir = config_file['wallpaper']
	period = int(config_file['period'])
	
	entries = os.listdir(wallpaper_dir)
	count = len(entries)
	index = 0
	while True:
		filename = "'{}/{}'".format(wallpaper_dir, entries[index])
		os.system('dconf write /org/mate/desktop/background/picture-filename "{}"'.format(filename))
		print('executed dconf write /org/mate/desktop/background/picture-filename "{}"'.format(filename))
		if(index == count-1):
			index = 0
		else:
			index+=1
		sys.stdout.flush()
		time.sleep(period)

if __name__ == "__main__":
	main()
