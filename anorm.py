import os
import cv2
#txt 가져오기
file_path ='C:\\anormary\\test.txt'
f = open(file_path)

id_list = []
alltime_list = []
dir_list = []

for line in f.readlines():
    line = line.strip()
    parts = line.split('\t')

    dir_list.append(parts[0])
    id_list.append(parts[1])
    alltime_list.append(parts[2])

print(dir_list)
print(id_list)
print(alltime_list)

part_time_list = []
#시간별 쪼개기
for i in range(len(alltime_list)):
    part = alltime_list[i].split()
    part_time_list = part_time_list + part

print('part_time_list:')
print(part_time_list)


#path 설정
for j in range(len(dir_list)):
    video_path = os.path.join('Z:/Anomaly_Data_Set', dir_list[j], id_list[j])
    print(video_path)
    videoFile = video_path + '.mp4'
    print(videoFile)
    #비디오 들고와
    vidcap = cv2.VideoCapture(videoFile)
    count = 0

    time = []
    for k in range(len(part_time_list)):
        part2 = part_time_list[k].split(':')
        print(part2)
        while (vidcap.isOpened()):
            ret, image = vidcap.read()
            image = cv2.resize(image, (680, 480))
            if(int(vidcap.get(1)) >= int(part2[0])):
                print('Saved frame number : ' + str(int(vidcap.get(1))))
                break
        vidcap.release()


'''
#20초 나누기

time = []
for k in range(len(part_time_list)):
    part2 = part_time_list[k].split(':')
    #print(part2)
    #좀 더 생각
    time = time + part2
    #print(time)

    #동영상 20초 frame

print('part2')
print(time)
'''