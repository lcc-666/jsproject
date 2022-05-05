import youtube_dl
import youtube

def down(url, Path):
    url = url
    Path = Path + "\\"
    opts = {
        "outtmpl": Path + '%(title)s.%(ext)s'
    }
    ydl = youtube_dl.YoutubeDL(opts)
    ydl.download([url])
    youtube.tomp4(Path)


if __name__ == '__main__':
    # url:b站视频链接
    url = "https://www.bilibili.com/video/BV1344y1379Q?spm_id_from=333.1007.extension.content.click"
    # Path:存储目录，最好是空的
    Path = r"D:\learn\video"
    down(url, Path)
