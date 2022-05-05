import yt_dlp
import ffmpy3
import os


def down(url, Path):
    url = url
    Path = Path + "\\"
    opts = {
        "outtmpl": Path + '%(title)s.%(ext)s'
    }
    ydl = yt_dlp.YoutubeDL(opts)
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
    url = "https://www.bilibili.com/video/BV1344y1379Q?spm_id_from=333.1007.extension.content.click"
    # Path:存储目录，最好是空的
    Path = r"D:\learn\video"
    down(url, Path)
