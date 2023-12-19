# -*- coding: utf-8 -*-
# Time : 2023/12/6 10:32
# Author : Walter
# File : 下载视频.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc :

import requests
import shutil
import os
from moviepy.editor import VideoFileClip

def download_file(url, filename):
    with requests.get(url, stream=True) as r:
        with open(filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

# 使用response.iter_content迭代响应内容的数据块。我们将数据块写入本地文件，以达到逐块写入的效果。chunk_size参数指定了每次读取的数据块大小，这里设置为8192字节（8 KB）
# def download_file(url, filename):
#     response = requests.get(url, stream=True)
#     response.raise_for_status()  # 检查请求是否成功
#
#     with open(filename, 'wb') as f:
#         for chunk in response.iter_content(chunk_size=8192):
#             f.write(chunk)

def merge_files(filenames, output_filename):
    with open(output_filename, 'wb') as outfile:
        for filename in filenames:
            with open(filename, 'rb') as f:
                shutil.copyfileobj(f, outfile)

def download_and_merge(url, output_filename):
    response = requests.get(url)
    playlist = response.text
    base_url = url.rsplit('/', 1)[0]

    ts_files = []
    for line in playlist.split('\n'):
        if line.endswith('.ts'):
            ts_url = base_url + '/' + line
            ts_filename = line.rsplit('/', 1)[-1]
            download_file(ts_url, ts_filename)
            ts_files.append(ts_filename)

    result_video = merge_files(ts_files, output_filename)

    convert_video_to_audio(result_video, '王牌对王牌第四季02.01期.mp3')

    # 删除临时的.ts文件
    for filename in ts_files:
        os.remove(filename)

    # 将合并后的视频转换为音频
    audio_filename = output_filename.rsplit('.', 1)[0] + '.mp3'
    convert_video_to_audio(output_filename, audio_filename)

def convert_video_to_audio(video_path, audio_path):
    try:
        video = VideoFileClip(video_path)
        audio = video.audio
        audio.write_audiofile(audio_path, codec='mp3')
        video.close()
    except Exception as e:
        print(f"Error occurred: {str(e)}")


url = 'https://vip.lz-cdn7.com/20220404/295_81008906/1200k/hls/mixed.m3u8'
output_filename = '王牌对王牌第四季02.01期.mp4'

# 调用函数下载和合并视频
download_and_merge(url, output_filename)