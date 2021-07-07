import os
path = "dummy/"
for folder in os.listdir(path):
	for count,filename in enumerate(os.listdir(path+'/'+folder)):
		dst = folder + str(count) +'.jpg'
		src = path + folder +'/' + filename
		dst = path + folder +'/' + dst
		os.rename(src,dst)