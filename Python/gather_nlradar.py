import os
import shutil
import tarfile

savedir = '/mnt/e/radar_data_NLradar'

directory = '/mnt/srv3_essl/work/gather_data'
tars = [f for f in os.listdir(directory) if '.tar' in f]
for tar in tars:
	print(tar)
	if not os.path.exists(savedir+'/'+tar):
		shutil.copyfile(directory+'/'+tar, savedir+'/'+tar)
		
		with tarfile.open(savedir+'/'+tar, 'r:gz') as f:
			f.extractall(savedir)
			
	os.remove(savedir+'/'+tar)
