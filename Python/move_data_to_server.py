import os
import shutil
import tarfile
import numpy as np



save_basedir = '/mnt/srv3_data/radars'

if 1:
	dates = ['20240408', '20240501', '20240505', '20240617', '20240730', '20240731', '20240824']
	dates = ['20240327', '20240620', '20240712', '20240801', '20240802', '20240815']
	dates = ['20220522', '20220604', '20220619', '20220621', '20230723']
	dates = ['20180429', '20190605', '20210619', '20220603']
	dates = ['20220604', '20220619', '20220621']
	dates = ['20220626', '20220630']
	dates = ['20180704', '20191015', '20200923', '20210619', '20211020', '20211031', '20220623', '20230309', '20240305', '20240711']
	dates = ['20220817', '20220818', '20220830', '20230711', '20230712', '20230724', '20230917']
	dates = ['20180429', '20190809', '20191014', '20191015', '20191222', '20200216', '20200923', '20220603', '20220720', '20220816', '20230309', '20230824', '20240305']
	dates += ['20131020', '20140125', '20140609', '20140610', '20140810', '20150513', '20150916']
	dates = ['20220907', '20220908', '20230330', '20230331', '20230618', '20230619']
	dates = ['20211021', '20130619', '20140609', '20140610', '20160623', '20180704', '20190604', '20210628', '20220520', '20221117', '20240404', '20230331', '20220907', '20220908', '20230618', '20230619']
	directory = '/mnt/e/radar_data_NLradar/Meteo France'
	for date in dates:
		print('MF', date)
		date_dir = directory+'/'+date
		radars = os.listdir(date_dir)
		for radar in radars:
			source_dir = date_dir+'/'+radar
			radar = radar.lower()
			save_dir = f'{save_basedir}/meteo-france/{date[:6]}/{date}/{radar}'
			tar_name = f'{date}_{radar}.tar'
			n_files = 0
			with tarfile.TarFile(tar_name, 'w') as f:
				for file in os.listdir(source_dir):
					if not os.path.exists(save_dir+'/'+file) or os.path.getsize(source_dir+'/'+file) != os.path.getsize(save_dir+'/'+file):
						print(file)
						f.add(source_dir+'/'+file, file)
						n_files += 1
			
			if n_files:
				os.makedirs(save_dir, exist_ok=True)
				print(save_dir+'/'+tar_name)
				shutil.copyfile(tar_name, save_dir+'/'+tar_name)
			os.remove(tar_name)
			
 
if 1:
	dates = ['20160623', '20190604', '20240824']
	dates = ['20100712', '20100714', '20140609', '20190809']
	dates = ['20180429', '20200216', '20211020', '20211021']
	dates = ['20080803', '20131020', '20140810', '20150824']
	dates = ['20220520']
	dates = ['20190313']
	directory = '/mnt/e/radar_data_NLradar/KNMI'
	for date in dates:
		print('KNMI', date)
		date_dir = directory+'/'+date
		radars = os.listdir(date_dir)
		for radar in radars:
			source_dir = date_dir+'/'+radar
			radar = radar.lower()
			save_dir = f'{save_basedir}/knmi/{date[:6]}/{date}/{radar}'
			tar_name = f'{date}_{radar}.tar'
			n_files = 0
			with tarfile.TarFile(tar_name, 'w') as f:
				for file in os.listdir(source_dir):
					if not os.path.exists(save_dir+'/'+file) or os.path.getsize(source_dir+'/'+file) != os.path.getsize(save_dir+'/'+file):
						print(file)
						f.add(source_dir+'/'+file, file)
						n_files += 1
					
			if n_files:
				os.makedirs(save_dir, exist_ok=True)
				print(save_dir+'/'+tar_name)
				shutil.copyfile(tar_name, save_dir+'/'+tar_name)
			os.remove(tar_name)
			
			
if 1:
	dates = ['20100712', '20100714', '20140125', '20140609', '20160623', '20180817', '20190604', '20190605', '20190809', '20210619', '20211020', '20221023', '20240709']
	dates = ['20080803', '20180429', '20200216']
	dates = ['20131020', '20140810']
	dates = ['20220520']
	dates = ['20140103', '20190313', '20211021']
	directory = '/mnt/e/radar_data_NLradar/KMI'
	source_map = {'wideumont':'kmi', 'jabbeke':'kmi', 'zaventem':'skeyes', 'helchteren':'vmm'}
	for date in dates:
		print('KMI', date)
		date_dir = directory+'/'+date
		folders = os.listdir(date_dir)
		for folder in folders:
			if folder[:2] == 'be':
				radar = 'wideumont'
				if folder[-1] == '2':
					continue
				dataset = 'precip' if folder[-1] == '1' else ''
			elif any(r in folder for r in ('Jabbeke', 'Zaventem', 'Wideumont', 'Helchteren')):
				radar = folder.split('_')[0].lower()
				dataset = 'precip' if folder[-1] == 'Z' else ''
			else:
				continue
				
			source_dir = date_dir+'/'+folder
			source = source_map[radar]
			save_dir = f'{save_basedir}/{source}/{date[:6]}/{date}/{radar}'+'/precip'*(dataset == 'precip')
			tar_name = f'{date}_{radar}.tar'
			n_files = 0
			with tarfile.TarFile(tar_name, 'w') as f:
				for file in os.listdir(source_dir):
					if not os.path.exists(save_dir+'/'+file) or os.path.getsize(source_dir+'/'+file) != os.path.getsize(save_dir+'/'+file):
						print(file)
						f.add(source_dir+'/'+file, file)
						n_files += 1
					
			if n_files:
				os.makedirs(save_dir, exist_ok=True)
				print(save_dir+'/'+tar_name)
				shutil.copyfile(tar_name, save_dir+'/'+tar_name)
			os.remove(tar_name)
		

if 1:
	dates = ['20100524', '20100712', '20100714', '20140609', '20160623', '20190604', '20230718', '20240609', '20240621', '20240630', '20240824']
	dates += ['20150505', '20150513', '20190809']
	dates += ['20180923']
#	dates += ['20190818']
#	dates = ['20180429', '20200216', '20211020', '20211021', '20220623', '20220626', '20220720', '20230824']
	dates = ['20190605', '20220627', '20220817', '20240621', '20240709', '20240926']
	dates = ['20190313', '20190611', '20190818', '20210624', '20210816', '20221023', '20230921', '20231221', '20240404']
	directory = '/mnt/e/radar_data_NLradar/DWD'
	for date in dates:
		print('DWD', date)
		date_dir = directory+'/'+date
		radar_datasets = sorted(os.listdir(date_dir))
		for i, rd in enumerate(radar_datasets):
			if not '_' in rd: continue
			radar, dataset = rd.split('_')
			radar = radar.lower()
			dataset = 'precip' if dataset == 'Z' else ''
			rd_dir = date_dir+'/'+rd
			save_dir = f'{save_basedir}/dwd/{date[:6]}/{date}/{radar}'+'/precip'*(dataset == 'precip')
			tar_name = f'{date}_{radar}.tar'
			n_files = 0
			with tarfile.TarFile(tar_name, 'w') as f:
				for hour in os.listdir(rd_dir):
					source_dir = rd_dir+'/'+hour
					files = os.listdir(source_dir)
					file_types = ['hd5' if 'hd5' in f else 'buf' for f in files]
					types, counts = np.unique(file_types, return_counts=True)
					most_common_type = types[np.argmax(counts)]
					print(types, counts)
					for file in files:
						if not most_common_type in file: continue
						if not os.path.exists(save_dir+'/'+file) or os.path.getsize(source_dir+'/'+file) != os.path.getsize(save_dir+'/'+file):
							print(file)
							f.add(source_dir+'/'+file, file)
							n_files += 1
					
			if n_files:
				os.makedirs(save_dir, exist_ok=True)
				print(save_dir+'/'+tar_name)
				shutil.copyfile(tar_name, save_dir+'/'+tar_name)
			os.remove(tar_name)
		

if 0:		
	dates = ['20240824']
	dates = ['20211020', '20211021']
	directory = '/mnt/e/radar_data_NLradar/DMI'
	for date in dates:
		print('DMI', date)
		date_dir = directory+'/'+date
		radar_datasets = sorted(os.listdir(date_dir))
		for i, rd in enumerate(radar_datasets):
			radar, dataset = rd.split('_')
			dataset = 'precip' if dataset == 'Z' else ''
			source_dir = date_dir+'/'+rd
			radar = radar.lower()
			save_dir = f'{save_basedir}/dmi/{date[:6]}/{date}/{radar}'+'/precip'*(dataset == 'precip')
			tar_name = f'{date}_{radar}.tar'
			n_files = 0
			with tarfile.TarFile(tar_name, 'w') as f:
				for file in os.listdir(source_dir):
					if not os.path.exists(save_dir+'/'+file) or os.path.getsize(source_dir+'/'+file) != os.path.getsize(save_dir+'/'+file):
						print(file)
						f.add(source_dir+'/'+file, file)
						n_files += 1
					
			if n_files:
				os.makedirs(save_dir, exist_ok=True)
				print(save_dir+'/'+tar_name)
				shutil.copyfile(tar_name, save_dir+'/'+tar_name)
			os.remove(tar_name)
		

if 0:		
	dates = ['20190611', '20230713', '20230718', '20230719', '20230724', '20240713']
	dates = ['20230801', '20230803', '20240701', '20240719']
	directory = '/mnt/e/radar_data_NLradar/ARSO'
	for date in dates:
		print('ARSO', date)
		date_dir = directory+'/'+date
		radars = os.listdir(date_dir)
		for radar in radars:
			source_dir = date_dir+'/'+radar
			radar = radar.lower()
			save_dir = f'{save_basedir}/arso/{date[:6]}/{date}/{radar}'
			tar_name = f'{date}_{radar}.tar'
			n_files = 0
			with tarfile.TarFile(tar_name, 'w') as f:
				for file in os.listdir(source_dir):
					if not os.path.exists(save_dir+'/'+file) or os.path.getsize(source_dir+'/'+file) != os.path.getsize(save_dir+'/'+file):
						print(file)
						f.add(source_dir+'/'+file, file)
						n_files += 1
					
			if n_files:
				os.makedirs(save_dir, exist_ok=True)
				print(save_dir+'/'+tar_name)
				shutil.copyfile(tar_name, save_dir+'/'+tar_name)
			os.remove(tar_name)
		

if 0:		
	dates = ['20230719']
	directory = '/mnt/e/radar_data_NLradar/ARPAV'
	for date in dates:
		print('ARPAV', date)
		date_dir = directory+'/'+date
		radars = os.listdir(date_dir)
		for radar in radars:
			source_dir = date_dir+'/'+radar
			radar = radar.lower()
			save_dir = f'{save_basedir}/arpav/{date[:6]}/{date}/{radar}'
			tar_name = f'{date}_{radar}.tar'
			n_files = 0
			with tarfile.TarFile(tar_name, 'w') as f:
				for file in os.listdir(source_dir):
					if not os.path.exists(save_dir+'/'+file) or os.path.getsize(source_dir+'/'+file) != os.path.getsize(save_dir+'/'+file):
						print(file)
						f.add(source_dir+'/'+file, file)
						n_files += 1
					
			if n_files:
				os.makedirs(save_dir, exist_ok=True)
				print(save_dir+'/'+tar_name)
				shutil.copyfile(tar_name, save_dir+'/'+tar_name)
			os.remove(tar_name)
			
			
if 0:
	dates = ['20240621', '20240630', '20240711']
	dates = ['20240619']
	directory = '/mnt/e/radar_data_NLradar/CHMI'
	for date in dates:
		print('CHMI', date)
		date_dir = directory+'/'+date
		radars = os.listdir(date_dir)
		for radar in radars:
			source_dir = date_dir+'/'+radar
			radar = radar.lower()
			save_dir = f'{save_basedir}/chmi/{date[:6]}/{date}/{radar}'
			tar_name = f'{date}_{radar}.tar'
			n_files = 0
			with tarfile.TarFile(tar_name, 'w') as f:
				for file in os.listdir(source_dir):
					if not os.path.exists(save_dir+'/'+file) or os.path.getsize(source_dir+'/'+file) != os.path.getsize(save_dir+'/'+file):
						print(file)
						f.add(source_dir+'/'+file, file)
						n_files += 1
					
			if n_files:
				os.makedirs(save_dir, exist_ok=True)
				print(save_dir+'/'+tar_name)
				shutil.copyfile(tar_name, save_dir+'/'+tar_name)
			os.remove(tar_name)
			
			
if 0:		
	dates = ['20240621', '20240630', '20240711']
	dates = ['20220117', '20230826', '20230827']
	directory = '/mnt/e/radar_data_NLradar/IMGW'
	for date in dates:
		print('IMGW', date)
		date_dir = directory+'/'+date
		radar_datasets = sorted(os.listdir(date_dir))
		for i, rd in enumerate(radar_datasets):
			radar, dataset = rd.split('_')
			dataset = 'precip' if dataset == 'Z' else ''
			source_dir = date_dir+'/'+rd
			radar = radar.lower()
			save_dir = f'{save_basedir}/imgw/{date[:6]}/{date}/{radar}'+'/precip'*(dataset == 'precip')
			tar_name = f'{date}_{radar}.tar'
			n_files = 0
			with tarfile.TarFile(tar_name, 'w') as f:
				for file in os.listdir(source_dir):
					if not os.path.exists(save_dir+'/'+file) or os.path.getsize(source_dir+'/'+file) != os.path.getsize(save_dir+'/'+file):
						print(file)
						f.add(source_dir+'/'+file, file)
						n_files += 1
					
			if n_files:
				os.makedirs(save_dir, exist_ok=True)
				print(save_dir+'/'+tar_name)
				shutil.copyfile(tar_name, save_dir+'/'+tar_name)
			os.remove(tar_name)
				
				
if 1:
	dates = ['20170812', '20210622', '20210623', '20220817', '20221016', '20240609', '20240831']
	directory = '/mnt/e/radar_data_NLradar/FMI'
	for date in dates:
		print('FMI', date)
		date_dir = directory+'/'+date
		radars = os.listdir(date_dir)
		for radar in radars:
			source_dir = date_dir+'/'+radar
			radar = radar.lower()
			save_dir = f'{save_basedir}/fmi/{date[:6]}/{date}/{radar}'
			tar_name = f'{date}_{radar}.tar'
			n_files = 0
			with tarfile.TarFile(tar_name, 'w') as f:
				for file in os.listdir(source_dir):
					if not os.path.exists(save_dir+'/'+file) or os.path.getsize(source_dir+'/'+file) != os.path.getsize(save_dir+'/'+file):
						print(file)
						f.add(source_dir+'/'+file, file)
						n_files += 1
					
			if n_files:
				os.makedirs(save_dir, exist_ok=True)
				print(save_dir+'/'+tar_name)
				shutil.copyfile(tar_name, save_dir+'/'+tar_name)
			os.remove(tar_name)
			

if 0:
	dates = ['20200608', '20210623']
	dates = ['20220712', '20221016', '20230830', '20240701']
	directory = '/mnt/e/radar_data_NLradar/ESTEA'
	for date in dates:
		print('ESTEA', date)
		date_dir = directory+'/'+date
		radars = os.listdir(date_dir)
		for radar in radars:
			source_dir = date_dir+'/'+radar
			radar = radar.lower()
			save_dir = f'{save_basedir}/estea/{date[:6]}/{date}/{radar}'
			tar_name = f'{date}_{radar}.tar'
			n_files = 0
			with tarfile.TarFile(tar_name, 'w') as f:
				for file in os.listdir(source_dir):
					if not os.path.exists(save_dir+'/'+file) or os.path.getsize(source_dir+'/'+file) != os.path.getsize(save_dir+'/'+file):
						print(file)
						f.add(source_dir+'/'+file, file)
						n_files += 1
					
			if n_files:
				os.makedirs(save_dir, exist_ok=True)
				print(save_dir+'/'+tar_name)
				shutil.copyfile(tar_name, save_dir+'/'+tar_name)
			os.remove(tar_name)
			
			
if 0:
	dates = ['20170710', '20210624', '20220818', '20230713', '20230718', '20230826', '20240609']
	directory = '/mnt/e/radar_data_NLradar/Austro Control'
	for date in dates:
		print('Austro Control', date)
		date_dir = directory+'/'+date
		radar_datasets = sorted(os.listdir(date_dir))
		for i, rd in enumerate(radar_datasets):
			if rd.endswith('_Z') and not (date == '20210624' and rd == 'Rauchenwarth_Z'):
				# Many Z datasets are actually a lower-res version of the V dataset, for testing purposes. These should not be uploaded to the server.
				continue
		
			radar, dataset = rd.split('_')
			dataset = 'precip' if dataset == 'Z' else ''
			source_dir = date_dir+'/'+rd
			radar = radar.lower()
			save_dir = f'{save_basedir}/austrocontrol/{date[:6]}/{date}/{radar}'+'/precip'*(dataset == 'precip')
			tar_name = f'{date}_{radar}.tar'
			n_files = 0
			with tarfile.TarFile(tar_name, 'w') as f:
				for file in os.listdir(source_dir):
					if not os.path.exists(save_dir+'/'+file) or os.path.getsize(source_dir+'/'+file) != os.path.getsize(save_dir+'/'+file):
						print(file)
						f.add(source_dir+'/'+file, file)
						n_files += 1
					
			if n_files:
				os.makedirs(save_dir, exist_ok=True)
				print(save_dir+'/'+tar_name)
				shutil.copyfile(tar_name, save_dir+'/'+tar_name)
			os.remove(tar_name)
			
			
if 0:
	dates = ['20140125', '20211020', '20211021', '20211031', '20221023', '20231101', '20231102', '20240926']
	dates = ['20120507', '20140810', '20231028', '20231227']
	directory = '/mnt/e/radar_data_NLradar/UKMO'
	for date in dates:
		print('UKMO', date)
		date_dir = directory+'/'+date
		radar_datasets = sorted(os.listdir(date_dir))
		for i, rd in enumerate(radar_datasets):
			radar, dataset = rd.split('_')
			dataset = 'precip' if dataset == 'Z' else ''
			source_dir = date_dir+'/'+rd
			radar = radar.lower()
			save_dir = f'{save_basedir}/ukmo/{date[:6]}/{date}/{radar}'+'/precip'*(dataset == 'precip')
			tar_name = f'{date}_{radar}.tar'
			n_files = 0
			with tarfile.TarFile(tar_name, 'w') as f:
				for file in os.listdir(source_dir):
					if not os.path.exists(save_dir+'/'+file) or os.path.getsize(source_dir+'/'+file) != os.path.getsize(save_dir+'/'+file):
						print(file)
						f.add(source_dir+'/'+file, file)
						n_files += 1
					
			if n_files:
				os.makedirs(save_dir, exist_ok=True)
				print(save_dir+'/'+tar_name)
				shutil.copyfile(tar_name, save_dir+'/'+tar_name)
			os.remove(tar_name)
