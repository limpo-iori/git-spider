import time
def progress_bar(tep):
	for i in range(tep):
		 print('['+'#'*int(i/tep*100)+']'+str(round(i/tep*100,2))+'%'+'\r',end='')

if __name__ == '__main__':
	progress_bar(200000)