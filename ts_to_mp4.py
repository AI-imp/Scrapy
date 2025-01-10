import os
import subprocess
# 获取video_segments文件夹下的所有文件
video_segments = os.listdir('video_segments')
# 根据文件名中的'CLS-'后面的数字对文件进行排序
video_segments.sort(key=lambda x: int(x.split('CLS-')[1].split('-')[0]))
# 拼接所有ts文件成为一个视频文件output.mp4
output_video = 'output.mp4'
cmd = f'ffmpeg -i "concat:{"|".join([os.path.join("video_segments", segment) for segment in video_segments])}" -c copy {output_video}'
subprocess.call(cmd, shell=True)
print("Video downloaded, merged, and saved as output.mp4 successfully!")