from . import CONN
from . import CURSOR

class Movie:
    def __init__(self, title, runtime):
        self.id = None
        self.title = title
        self.runtime = runtime

    def __repr__(self):
        return f'<Movie id={self.id} title={self.title} runtime={self.runtime}>'
