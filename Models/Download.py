from abc import ABC, abstractmethod


class Download(ABC):
    """
    This class is a model abstract class for the class DownloadController
    """
    def __init__(self, playlist_url: str) -> None:
        """
        Insert the URI for the video
        :param playlist_url:
        """
        self.__playlist_url: str = playlist_url

    @abstractmethod
    def makeDownloadNow(self) -> None: ...  # abstract method to downloadcontroller class
