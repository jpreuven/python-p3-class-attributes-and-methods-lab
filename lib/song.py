class Song:
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}


    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        # Song.count += 1
        # Song.genres.append(genre)
        # Song.artists.append(artist)
        self.add_song_to_count()
        self.add_genre(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_genre(cls,genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls,artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in Song.genre_count.keys():
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in Song.artist_count.keys():
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1



        # print ("pop" in Song.genre_count.keys())
        # if Song.genre_count[genre]:
            # Song.genre_count[genre] += 1
            # print("in there")
        # else:
            # Song.genre_count[genre] = 1
            # print('not in there')
    pass

# Song("99 problems","Jay-Z", "rap")
# Song("99 problems","Jay-Z", "rap")
# Song("99 problems","Jay-Z", "rock")
# print(Song.genres)
# print(Song.genre_count)
# print(Song.count)