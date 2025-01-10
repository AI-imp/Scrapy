import requests
import os
import time
import subprocess
if not os.path.exists('video_segments'):
    os.makedirs('video_segments')
links_to_retry = []
header = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding':'gzip, deflate, br, zstd',
    'Accept-Language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'connection':'keep-alive',
    'Cache-Control':'max-age=0',
    'Sec-Fetch-Dest':'document',
    'Sec-Fetch-Mode':'navigate',
    'Sec-Fetch-Site':'none',
    'Sec-Fetch-User':'?1',
    'Upgrade-Insecure-Requests':'1',
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",}
# 从本地m3u8文件中提取.ts文件的链接
#https://vod1eu16.128100.xyz/hls/KNhsHiD9KHw/拼接
# 从本地m3u8文件中提取.ts文件的链接
m3u8_file = r"E:\python\learningproject\spider\attachmentvideo1\failed_links.txt"
with open(m3u8_file, 'r') as file:
    m3u8_content = file.read()
    ts_files=m3u8_content.split('\n')
#下载每个.ts文件/视频片段
# 下载视频片段
for ts_file in ts_files:
    ts_url = f"{ts_file}"
    file_name = ts_url.split('/')[-1].split('.ts')[0]
    try:
        start_time = time.time()
        ts_content = requests.get(ts_url, headers=header).content
        if len(ts_content) < 100000:  # Check if content size is less than 100KB错误信息一般比ts小得多
            raise Exception("Content size less than 100KB")  # Simulate download failure
        with open(f"video_segments/{file_name}.ts", 'wb') as f:
            f.write(ts_content)
        end_time = time.time()
        print(f"Downloaded: {file_name}.ts (Time taken: {end_time - start_time:.2f} seconds)")
    except (requests.exceptions.RequestException, Exception) as e:
        print(f"Failed to download {file_name}.ts: {e}")
        links_to_retry.append(ts_file)
    time.sleep(10)

print("First batch downloaded successfully.")
time.sleep(20)

# 重新尝试下载失败的链接
failed_links = []
for ts_file in links_to_retry:
    file_name = ts_file.split('/')[-1].split('.ts')[0]
    try:
        start_time = time.time()
        ts_content = requests.get(ts_file).content
        if len(ts_content) < 100000:  # Check if content size is less than 100KB
            raise Exception("Content size less than 100KB")  # Simulate download failure
        with open(f"video_segments/{file_name}.ts", 'wb') as f:
            f.write(ts_content)
        end_time = time.time()
        print(f"Downloaded (retry): {file_name}.ts (Time taken: {end_time - start_time:.2f} seconds)")
    except (requests.exceptions.RequestException, Exception) as e:
        print(f"Failed to download {file_name}.ts on retry: {e}")
# 将第二次都下载失败的链接写入txt文件
with open("failed_links_final.txt", "w") as file:
    for link in failed_links:
        file.write(f"{link}\n")
