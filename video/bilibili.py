import youtube_dl
import os

# url:b站视频链接
url = "https://www.bilibili.com/video/BV1hr4y1H7SP?spm_id_from=333.851.b_7265636f6d6d656e64.1"
# Path:存储目录，最好是空的
Path = r'D:\learn\video\\'

opts = {
    "outtmpl": Path + '%(title)s.%(ext)s'
}
ydl = youtube_dl.YoutubeDL(opts)
ydl.download([url])

ls = os.listdir(Path)
# 转MP4，先配置ffmpeg
for item in ls:
    old = Path + item
    new = Path + item.split(".")[0] + '.mp4'
    FFmpeg = r"E:\ffmpeg\bin\ffmpeg.exe"
    cmd = FFmpeg + " -i {} {}".format(old, new)
    os.system(cmd)
    os.remove(old)
