# -*- coding: utf-8 -*-
# Time : 2023/12/6 16:14
# Author : Walter
# File : 下载视频_协程版升级版.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc :

import os
import aiohttp
import asyncio
import requests
from tqdm import tqdm
from moviepy.editor import VideoFileClip, concatenate_videoclips


async def download_file(url, filename):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response.raise_for_status()
            total_size = int(response.headers.get('content-length', 0))
            block_size = 1024
            progress_bar = tqdm(total=total_size, unit='B', unit_scale=True)

            with open(filename, 'wb') as file:
                downloaded_size = 0
                async for data in response.content.iter_any():
                    file.write(data)
                    downloaded_size += len(data)
                    progress_bar.update(len(data))

            progress_bar.close()


async def download_and_merge(url, output_filename):
    response = await aiohttp.ClientSession().get(url)
    playlist = await response.text()
    base_url = url.rsplit('/', 1)[0]

    ts_files = []
    downloaded_ts_size = 0

    tasks = []
    for line in playlist.split('\n'):
        if line and line.endswith('.ts'):
            ts_url = base_url + '/' + line
            ts_filename = line.rsplit('/', 1)[-1]
            task = asyncio.ensure_future(download_file(ts_url, ts_filename))
            tasks.append(task)

            ts_files.append(ts_filename)

    await asyncio.gather(*tasks)

    total_ts_size = sum(os.path.getsize(ts_filename) for ts_filename in ts_files)
    downloaded_ts_size = sum(os.path.getsize(ts_filename) for ts_filename in ts_files)

    progress = downloaded_ts_size / total_ts_size * 100
    print(f'Downloaded {progress:.2f}%')

    merge_files(ts_files, output_filename)

    # 删除临时的.ts文件
    for filename in ts_files:
        os.remove(filename)

    # 将合并后的视频转换为音频
    audio_filename = output_filename.rsplit('.', 1)[0] + '.mp3'
    convert_video_to_audio(output_filename, audio_filename)


def merge_files(ts_files, output_filename):
    clips = []
    for ts_file in ts_files:
        clip = VideoFileClip(ts_file)
        clips.append(clip)

    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile(output_filename, codec='libx264')
    final_clip.close()


def convert_video_to_audio(video_path, audio_path):
    try:
        video = VideoFileClip(video_path)
        audio = video.audio
        audio.write_audiofile(audio_path, codec='mp3')
        video.close()
    except Exception as e:
        print(f"Error occurred: {str(e)}")


url = 'https://v.cdnlz1.com/20231205/24391_68c300f1/2000k/hls/mixed.m3u8'
output_filename = '电视剧/南海归墟15.mp4'

# 调用函数下载和合并视频
asyncio.run(download_and_merge(url, output_filename))

# loop = asyncio.get_event_loop()
# loop.run_until_complete(download_and_merge(url, output_filename))
