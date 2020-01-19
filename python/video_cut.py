import cv2

if __name__ == '__main__':
	#创建显示窗口
	#cv2.namedWindow('Video')
	# 导入视频文件，参数：0 自带摄像头，1 USB摄像头，为文件名时读取视频文件
	video_capture = cv2.VideoCapture("C:\\Users\\dodo\\Desktop\\FP说明\\origin_fp.MP4")
	# 获取读入视频的参数
	fps = video_capture.get(cv2.CAP_PROP_FPS)
	width = video_capture.get(cv2.CAP_PROP_FRAME_WIDTH)
	height = video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
	fourcc = int(video_capture.get(cv2.CAP_PROP_FOURCC))
	print('fps:',fps)
	print('width:', width)
	print('height:', height)
	# 定义截取尺寸,后面定义的每帧的h和w要于此一致，否则视频无法播放
	size = (int(600), int(500)) # (width, height)
	# 创建视频写入对象
	video_writer = cv2.VideoWriter("D:\\test.avi",
									cv2.VideoWriter_fourcc('M', 'P', '4', '2'),
									fps,
									size)
	#读取视频帧，然后写入文件并在窗口显示
	success, frame = video_capture.read()
	while success and not cv2.waitKey(1) == 27:
		# 定义ROI的位置
		frame2 = frame[0:500, 0:600] # [height, width] 要与上面定义的size参数一致，注意参数的位置
		frame2 = cv2.resize(frame2,(600,500),interpolation=cv2.INTER_CUBIC)
		cv2.imshow("video", frame2)
		cv2.waitKey(24)
		video_writer.write(frame2) # 写入视频文件
		success, frame = video_capture.read()
	#回收资源
	video_writer.release()
	video_capture.release()
	#cv2.destroyWindow("video")