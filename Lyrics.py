import dbus
from bs4 import BeautifulSoup
import requests
import sys


class Lyrics:

    def __init__(self):
        try:
            self.artist = self.current_artist_song()['xesam:artist'][0]
            self.song = self.current_artist_song()['xesam:title']
        except TypeError:
            print('Start Spotify')

    @staticmethod
    def current_artist_song():
        try:
            session_bus = dbus.SessionBus()
            spotify_bus = session_bus.get_object("org.mpris.MediaPlayer2.spotify", "/org/mpris/MediaPlayer2")
            spotify_properties = dbus.Interface(spotify_bus, "org.freedesktop.DBus.Properties")
            metadata = spotify_properties.Get("org.mpris.MediaPlayer2.Player", "Metadata")
        except dbus.DBusException:
            print('Please Start Spotify')
            sys.exit(1)
        else:
            return metadata

    def get_artist(self):
        return self.artist

    def get_song(self):
        return self.song

    def get_lyrics(self):

        try:
            r = requests.get('http://lyrics.wikia.com/wiki/' + self.artist + ':' + self.song).content
            soup = BeautifulSoup(r, 'lxml')
            s_tags = soup.find_all(class_="lyricbox")

            if len(s_tags) == 0:
                lyrics = '<a href="https://www.google.com/#q=' + self.artist.replace(' ', '+')\
                         + '+' + self.song.replace(' ', '+') + '+lyrics">Search Lyrics online</a>'

            lyrics = str(s_tags[0]).replace('<[^>br]*>', '').replace('<br>', '\n')

        except requests.ConnectionError:
            print('Network problem')
        except requests.HTTPError as e:
            print('Http error: ' + e)
        except IndexError:
            print('lyrics not found ' + self.artist + ' ' + self.song)
        except requests.RequestException:
            print('Request')

        return lyrics

    def update(self):
        if self.song != self.current_artist_song()['xesam:title']:
            self.song = self.current_artist_song()['xesam:title']
            self.artist = self.current_artist_song()['xesam:artist'][0]
            return True
        return False
