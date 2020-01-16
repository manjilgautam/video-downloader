from pytube import YouTube
import sys
import os
import urllib
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from core import YouTubeVideo

youtubeVideo = Youtube("https://www.youtube.com/watch?v=9bZkp7q19f0")

print(youtubeVideo)
