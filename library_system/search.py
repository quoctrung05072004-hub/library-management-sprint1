class BookSearch:
    def __init__(self, repository):
        self.repository = repository

    def search_by_title(self, keyword):
        query = keyword.strip().casefold()
        return [book for book in self.repository.get_all()
                if query and query in book.title.casefold()]

    def search_by_author(self, keyword):
        query = keyword.strip().casefold()
        return [book for book in self.repository.get_all()
                if query and query in book.author.casefold()]
