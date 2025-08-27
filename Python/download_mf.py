import os
import shutil
from datetime import datetime, timedelta

basedir1 = '/mnt/essl/data/radars/meteo-france'
basedir2 = '/mnt/srv3_data/radars/meteo-france'
save_basedir = '/mnt/e/radar_data_NLradar/Meteo France'

jobs = [(r, '202501270900', '202501271100') for r in ('Noyal', 'Bourges', 'Arcis-sur-Aube', 'Avesnes', 'Treillieres', 'Bordeaux', 'Cherves')]
jobs = [(r, '202504191200', '202504191500') for r in ('Opoul',)]

for job in jobs:
	print(job)
	radar, dt_start, dt_end = job
	dt_start, dt_end = datetime.strptime(dt_start, '%Y%m%d%H%M'), datetime.strptime(dt_end, '%Y%m%d%H%M')
	dt = dt_start
	date_before = None
	while dt <= dt_end:
		date = dt.strftime('%Y%m%d')
		dt += timedelta(minutes=5)
		if date == date_before:
			continue
		date_before = date
		
		directory = basedir1+f'/{date[:6]}/{date}/{radar.lower()}'
		if not os.path.exists(directory):
			directory = basedir2+f'/{date[:6]}/{date}/{radar.lower()}'
		
		save_directory = save_basedir+f'/{date}/{radar}'
		os.makedirs(save_directory, exist_ok=True)
		
		files = os.listdir(directory)
		for file in files:
			file_dt = datetime.strptime(file.split('_')[-1][:12], '%Y%m%d%H%M')			
			if dt_start <= file_dt <= dt_end:
				if not os.path.exists(save_directory+'/'+file):
					print(file)
					shutil.copyfile(directory+'/'+file, save_directory+'/'+file)
