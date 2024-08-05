class Genres:
    def __init__(self):
        self.genres = {}
 
    def add_genre(self):
        name = input("What is the genre's name?: ")
        info = input("What is the genre's description?: ")
        self.genres[name]= {"name":name, "description":info}
        print(self.genres[name])

    def search_genres(self):
        genre = input("What is the name of the genre you're searching for?")
        if genre in self.genres:
            print(self.genres[genre])

    def display_genres(self):
        for name in self.genres:
            print(self.genres[name])


class Authors:
    def __init__(self):
        self.authors = {}
 
    def add_author(self):
        name = input("What is the author's name?: ")
        info = input("What is the autor's info?: ")
        self.authors[name]= {"name":name, "description":info}
        print(self.authors[name])

    def search_author(self):
        author = input("What is the name of the author you're searching for?")
        if author in self.authors:
            print(self.authors[author])

    def display_authors(self):
        for name in self.authors:
            print(self.authors[name])