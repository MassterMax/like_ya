from yandex_music import Client
from yandex_music.playlist.playlist import Playlist

# https://oauth.yandex.ru/authorize?response_type=token&client_id=23cabbbdc6cd418abb4b39c32c41195d
API_TOKEN = "insert"
PLAYLIST_NAME = "Любимое в Spotify"


def get_playlist_by_name(client: Client, name: str) -> Playlist:
    playlists = client.users_playlists_list()
    for playlist in playlists:
        if playlist['title'] == name:
            return playlist


def main():
    client = Client(API_TOKEN)
    client.init()

    playlist = get_playlist_by_name(client, PLAYLIST_NAME)
    tracks = playlist.fetch_tracks()
    track_ids = [t['id'] for t in tracks]
    client.users_likes_tracks_add(track_ids=track_ids)


if __name__ == "__main__":
    main()
