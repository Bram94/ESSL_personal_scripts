import os
import shutil
from datetime import datetime, timedelta
import tarfile

basedir1 = '/mnt/essl/data/radars/dwd'
basedir2 = '/mnt/srv3_data/radars/dwd'
save_basedir = '/mnt/h/radar_data_NLradar/DWD'

jobs = [('Offenthal', '202505031200', '202505031800'),]

for job in jobs:
	print(job)
	radar, dt_start, dt_end = job
	dt_start, dt_end = datetime.strptime(dt_start, '%Y%m%d%H%M'), datetime.strptime(dt_end, '%Y%m%d%H%M')
	dt = dt_start
	
	tar_name = f'{radar}_{dt_start}_{dt_end}.tmp'
	with tarfile.open(tar_name, "w:gz") as tar:
		while dt < dt_end:
			date = dt.strftime('%Y%m%d')
			
			directory = basedir1+f'/{date[:6]}/{date}/{radar.lower()}'
			if not os.path.exists(directory):
				directory = basedir2+f'/{date[:6]}/{date}/{radar.lower()}'
			
			for dataset in ('Z', 'V'):
				_dataset = '/precip' if dataset == 'Z' else ''
				files = os.listdir(directory+_dataset)
				for file in files:
					_datetime = file[file.index(date):][:12]
					file_dt = datetime.strptime(_datetime, '%Y%m%d%H%M')
					if dt_start <= file_dt <= dt_end:
						hour = int(_datetime[-4:-2])
						hour = format(hour*100, '04d')+'-'+format((hour+1)%24 * 100, '04d')
						
						save_folder = f'{date}/{radar}_{dataset}/{hour}'
						save_directory = save_basedir+'/'+save_folder
						if not os.path.exists(save_directory+'/'+file):
							print(file)
						
							tar.add(directory+_dataset+'/'+file, arcname = save_folder+'/'+file)
	#						shutil.copyfile(directory+'/'+file, save_directory+'/'+file)

			dt += timedelta(days=1)
			
	shutil.copyfile(tar_name, save_directory)
