# Get Youtube Channels [video name+views] per video
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

while '1' == '1':
	a = input("Channel Name:")
	if a == 'exit' or a == '':
		break
	driver = webdriver.Chrome()
	driver.get('http://www.youtube.com/'+a+'/videos')
	count = 1
	views = 0
	video_name = []
	video_count = []

	video_name_length = 55
	for i in range(100):
		pass
		try:
			driver.find_element_by_class_name('load-more-text').click()
		except:
			pass
	for i in driver.find_elements_by_class_name("channels-content-item"):
		try:
			temp = i.find_element_by_class_name('yt-lockup-meta-info').text
			i_video_name = i.find_element_by_class_name('yt-uix-tile-link').text.replace("'",'').encode('cp850',errors = 'replace').decode('cp850')
			view_count = 0
			try:
				view_count = int(temp[:temp.index('views')].strip().replace(',','').strip())
			except Exception as e:
				pass
			i_view_count = view_count
			views = views + view_count
			video_name.append(i_video_name)
			video_count.append(i_view_count)
			if len(i_video_name) < video_name_length:
				i_video_name_length_append = video_name_length - len(i_video_name)
				i_video_name = i_video_name + " "*i_video_name_length_append
			else:
				i_video_name = i_video_name[:video_name_length]
			print(str(count)+":  "+i_video_name + ": "+str(i_view_count))
		except Exception as e:
			print(e)
			pass
		count = count + 1
	print("Total Views: "+str(view_count))
	maximum = max(video_count)
	video_name2 = video_name[video_count.index(maximum)]
	print("Maximum View Gained:  " + video_name2.encode('cp850',errors = 'replace').decode('cp850') )
	driver.close()
