
import sys
import os
import urllib
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from core import YouTubeVideo


class Ui(QtWidgets.QMainWindow):
    """[summary]

    Arguments:
        QtWidgets {[type]} -- [description]
    """

    def __init__(self):
        super(Ui, self).__init__()

        # Gets current path to the file to avoid issue with dynamic path
        script_path = (os.path.dirname(os.path.realpath(__file__)))
        uic.loadUi(f'{script_path}/ui/qt.ui', self)

        # When object btnOk is pressed, Ui.enterURL is run
        self.btnOK.clicked.connect(self.enterURL)

        # Sets the text in the widget lineEditURL to be the link (For testing purposes)
        self.lineEditURL.setText("https://www.youtube.com/watch?v=9bZkp7q19f0")

        self.show()

    def processYouTubeVideo(self, link):
        video = YouTubeVideo(link)

        # Opens the tab Youtube Video
        self.tabYouTubeVideo

        # Inserts the video title into the widget labelVideoTitle
        self.labelVideoTitle.setText(video.getVideoTitle())

        # Obtains the thumbnail and inserts it in the widget
        thumbnail_data = urllib.request.urlopen(
            video.getVideoThumbnail()).read()
        pixmap = QPixmap()
        pixmap.loadFromData(thumbnail_data)
        pixmap = pixmap.scaled(
            230, 230, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.labelThumbnail.setPixmap(pixmap)

        #print(f"URL: {link}")
        # print(f"Video Title: {video.getVideoTitle()}")
        # print(f"Video Thumbnail: {video.getVideoThumbnail()}")
        # print(f"Video Streams: {video.getStreams()}")

    def processYouTubePlaylist(self, link):
        pass

    def errorURL(self, link):
        pass

    def enterURL(self):
        link = self.lineEditURL.text()
        # If you were to need to unshorten the URL in the future, place it here
        if "youtube" in link.lower():
            if "playlist?" in link.lower():
                print("Playlist")
                self.processYouTubePlaylist(link)
            else:
                print("Video")
                self.processYouTubeVideo(link)
        else:
            print("Other")
            self.errorURL(link)


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()

'''
~~~~~ Essential Widgets ~~~~~

Home tab
    lineHomeURL - Initial input box in tab "Home"
'''
