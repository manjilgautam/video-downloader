from pytube import YouTube

# https://python-pytube.readthedocs.io/en/latest/user/quickstart.html


class YouTubeVideo:

    def __init__(self, link):
        self.yt = YouTube(link)

    def getVideoTitle(self):
        """Gets the video title

        Returns:
            str -- returns youtube video's title
        """
        return self.yt.title

    def getVideoThumbnail(self):
        """Gets the video thumbnail picture

        Returns:
            str -- URL to the youtube video
        """
        return f'https://img.youtube.com/vi/{self.yt.video_id}/maxresdefault.jpg'

    def getStreams(self):
        """Gets the streams

        Returns:
            list -- A list of all the streams
        """
        return self.yt.streams.all()


'''
if __name__ == "__main__":
    video = YouTubeVideo("https://www.youtube.com/watch?v=9bZkp7q19f0")
    print(video.getVideoTitle())
    input()
    print(video.getVideoTitle())
    '''

if __name__ == "__main__":
    video = YouTubeVideo("https://www.youtube.com/watch?v=9bZkp7q19f0")
    print(video.getVideoTitle())
    input()
    video.yt.streams.all()
    print(video.getVideoTitle())
