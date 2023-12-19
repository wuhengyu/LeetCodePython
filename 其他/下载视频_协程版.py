# -*- coding: utf-8 -*-
# Time : 2023/12/6 11:17
# Author : Walter
# File : 下载视频_协程版.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc :


import asyncio
import aiohttp
import shutil
import os

from moviepy.video.io.VideoFileClip import VideoFileClip


async def download_file(session, url, filename):
    async with session.get(url) as response:
        with open(filename, 'wb') as f:
            while True:
                # 这里设置为8192字节（8KB）
                chunk = await response.content.read(8192)
                if not chunk:
                    break
                f.write(chunk)


async def merge_files(filenames, output_filename):
    with open(output_filename, 'wb') as outfile:
        for filename in filenames:
            with open(filename, 'rb') as f:
                shutil.copyfileobj(f, outfile)


async def download_and_merge(url, output_filename):
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        playlist = await response.text()
        base_url = url.rsplit('/', 1)[0]

        ts_files = []
        tasks = []
        for line in playlist.split('\n'):
            if line and line.endswith('.ts'):
                ts_url = base_url + '/' + line
                ts_filename = line.rsplit('/', 1)[-1]
                task = asyncio.create_task(download_file(session, ts_url, ts_filename))
                tasks.append(task)
                ts_files.append(ts_filename)

        await asyncio.gather(*tasks)

        await merge_files(ts_files, output_filename)

        # 删除临时的.ts文件
        for filename in ts_files:
            os.remove(filename)

        # 将合并后的视频转换为音频
        audio_filename = output_filename.rsplit('.', 1)[0] + '.mp3'
        await convert_video_to_audio(output_filename, audio_filename)


async def convert_video_to_audio(video_path, audio_path):
    try:
        video = VideoFileClip(video_path)
        audio = video.audio
        audio.write_audiofile(audio_path, codec='mp3')
        video.close()
    except Exception as e:
        print(f"Error occurred: {str(e)}")


url = 'https://vip.lz-cdn2.com/20220407/2560_9828ebdc/1200k/hls/mixed.m3u8'

if not os.path.exists('./电影'):
    os.mkdir('./电影')

output_filename = './电影/破坏之王.mp4'

# 调用函数下载和合并视频
asyncio.run(download_and_merge(url, output_filename))

# loop = asyncio.get_event_loop()
# loop.run_until_complete(download_and_merge(url, output_filename))
