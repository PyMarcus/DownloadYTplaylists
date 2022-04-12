import getpass
import os
import platform
from Models.Download import Download
from pytube import Playlist, YouTube


class DownloadController(Download):
    """
    Make download of playlist
    """

    def __init__(self, playlist_uri: str) -> None:
        """
        Insert the playlist URI
        :param playlist_uri:
        """
        super().__init__(playlist_url=playlist_uri)
        self.__playlist: str = playlist_uri

    @property
    def playlist(self) -> str:
        return self.__playlist

    def makeDownloadNow(self) -> None:
        """
        this method makes download videos from uri
        :return:
        """
        user: getpass.getuser = getpass.getuser()
        path_to_videos: str = f"C:\\Users\\{user}\\Videos\\"
        if platform.system() == "Linux":
            path_to_videos.replace("C:", "/").replace("\\", "/").replace("Users", "home")
        os.chdir(path_to_videos)
        paths: list = []
        for files in os.listdir(path_to_videos):
            paths.append(path_to_videos + files)
        if path_to_videos + "playlists_downloads" not in paths: os.mkdir(path_to_videos + "playlists_downloads")
        playlist: Playlist = Playlist(self.playlist)
        [YouTube(video).streams.filter(only_audio=True).download(output_path=path_to_videos) for video in playlist]


if __name__ == '__main__':
    download = DownloadController("https://www.youtube.com/watch?v=GU0DhAlYCyI&list=PLh9R-kdGXNL4re22eMuWzQkapepohLWEu")
    download.makeDownloadNow()
