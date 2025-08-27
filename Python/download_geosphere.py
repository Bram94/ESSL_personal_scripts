import os
import shutil
from datetime import datetime, timedelta

basedir = '/mnt/essl/data/radars/geosphere'
# basedir = '/mnt/essl/data_perm/radars/special_cases/dwd'
save_basedir = '/mnt/e/radar_data_NLradar/ZAMG'

jobs = [('Hochficht', '202503270100', '202503270400')]

for job in jobs:
	print(job)
	radar, dt_start, dt_end = job
	dt_start, dt_end = datetime.strptime(dt_start, '%Y%m%d%H%M'), datetime.strptime(dt_end, '%Y%m%d%H%M')
	dt = dt_start
	while dt < dt_end:
		date = dt.strftime('%Y%m%d')
		
		directory = basedir+f'/{date[:6]}/{date}/{radar.lower()}'
		
		files = os.listdir(directory)
		for file in files:
			_datetime = file[file.index(date):][:12]
			file_dt = datetime.strptime(_datetime, '%Y%m%d%H%M')
			if dt_start <= file_dt <= dt_end:	
				save_directory = save_basedir+f'/{date}/{radar}'
				os.makedirs(save_directory, exist_ok=True)
				
				if not os.path.exists(save_directory+'/'+file):
					print(file)
					shutil.copyfile(directory+'/'+file, save_directory+'/'+file)

		dt += timedelta(days=1)
