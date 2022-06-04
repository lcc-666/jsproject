import yt_dlp
import ffmpy3
import os
import sys


def down(url, path):
    if path is "":
        res=os.path.abspath(sys.argv[0])
        path=res.replace("youtube.py","")
    url = url
    if os.name == "nt":
        path = path + "\\"
    else:
        path = path + "/"
    opts = {
        "outtmpl": path + '%(title)s.%(ext)s'
    }
    ydl = yt_dlp.YoutubeDL(opts)
    ydl.download([url])
    # tomp4(Path)


def tomp4(Path):
    ls = os.listdir(Path)
    # 转MP4，先配置ffmpeg
    for item in ls:
        if item.split(".")[-1] == 'mp4':
            continue
        old = Path + item
        new = Path + item.split(".")[0] + '.mp4'
        # ffmpeg的bin目录
        FFmpeg = r"E:\ffmpeg\bin\ffmpeg.exe"
        ff = ffmpy3.FFmpeg(
            executable=FFmpeg,
            inputs={old: None},
            outputs={new: None}
        )
        ff.run()


if __name__ == '__main__':
    # url:youtube视频链接
    Url = input("请输入视频地址\n")
    # Path:存储目录，最好是空的
    Path = input("请输入存储目录(默认文件目录)\n")
    down(Url, Path)
