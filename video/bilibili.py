import youtube_dl
import os


def down(url, Path):
    url = url
    Path = Path + "\\"
    opts = {
        "outtmpl": Path + '%(title)s.%(ext)s'
    }
    ydl = youtube_dl.YoutubeDL(opts)
    ydl.download([url])
    tomp4(Path)


def tomp4(Path):
    ls = os.listdir(Path)
    # 转MP4，先配置ffmpeg
    for item in ls:
        if item.split(".")[-1] == 'mp4':
            continue
        old = Path + item
        new = Path + item.split(".")[0] + '.mp4'
        #ffmpeg的bin目录
        FFmpeg = r"E:\ffmpeg\bin\ffmpeg.exe"
        cmd = FFmpeg + " -i {} {}".format(old, new)
        os.system(cmd)
        os.remove(old)


if __name__ == '__main__':
    # url:b站视频链接
    url = "https://www.bilibili.com/video/BV1Er4y1n7N3?t=1.4"
    # Path:存储目录，最好是空的
    Path = r"D:\learn\video"
    down(url, Path)
