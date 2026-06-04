class Song:
    # Class Attributes (Shared across all instances)
    count = 0
    genre_count = {}
    artists_count = {}

    def __init__(self, name, artist, genre):
        # Instance Attributes (Unique to each song)
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Trigger all class methods upon creation
        Song.add_song_to_count()
        Song.add_to_genre_count(genre)
        Song.add_to_artists_count(artist)

    def __repr__(self):
        return f"Song(name='{self.name}', artist='{self.artist}', genre='{self.genre}')"

    # ── Class Methods ──────────────────────────────────────────────────────────
    @classmethod
    def add_song_to_count(cls):
        """Increments the total number of songs by 1."""
        cls.count += 1

    @classmethod
    def add_to_genre_count(cls, genre):
        """
        Increments the genre's count in genre_count. 
        If the genre doesn't exist yet, it is added with a starting value of 1.
        """
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def add_to_artists_count(cls, artist):
        """
        Increments the artist's count in artists_count. 
        If the artist doesn't exist yet, they are added with a starting value of 1.
        """
        cls.artists_count[artist] = cls.artists_count.get(artist, 0) + 1


