class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        if len(name) == 0:
            raise Exception("Name cannot be empty")
        self._name = name

    @property
    def name(self):
        return self._name

    # Make name immutable by not providing a setter
    @name.setter
    def name(self, value):
        # Ignore changes to name to keep it immutable as per tests
        pass

    def articles(self):
        # Return list of Article instances where self is author
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        # Return unique list of Magazine instances for articles by this author
        magazines = {article.magazine for article in self.articles()}
        return list(magazines)

    def add_article(self, magazine, title):
        # Create and return a new Article with self as author
        return Article(self, magazine, title)

    def topic_areas(self):
        # Return unique list of categories of magazines the author wrote for
        mags = self.magazines()
        if not mags:
            return None
        return list({mag.category for mag in mags})
class Magazine:
    all = []

    def __init__(self, name, category):
        self._name = None
        self._category = None

        self.name = name       # use setter to validate
        self.category = category  # use setter to validate

        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # Only allow string names between 2 and 16 chars inclusive
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            # Ignore invalid change, keep old value if exists
            if self._name is None:
                raise Exception("Name must be a string 2 to 16 characters long")
            return
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        # Category must be non-empty string
        if not isinstance(value, str) or len(value) == 0:
            # Ignore invalid change, keep old value if exists
            if self._category is None:
                raise Exception("Category must be a non-empty string")
            return
        self._category = value

    def articles(self):
        # Return list of Article instances associated with this magazine
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        # Return unique list of Authors who have written for this magazine
        authors = {article.author for article in self.articles()}
        return list(authors)

    def article_titles(self):
        # Return list of article titles, or None if no articles
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        # Return authors who have more than 2 articles for this magazine
        authors = self.contributors()
        contributing = [author for author in authors if len([a for a in self.articles() if a.author == author]) > 2]
        return contributing if contributing else None

    # Optional if you want to implement the commented-out test
    # @classmethod
    # def top_publisher(cls):
    #     if not cls.all:
    #         return None
    #     # Count articles per magazine
    #     article_counts = {mag: 0 for mag in cls.all}
    #     for article in Article.all:
    #         if article.magazine in article_counts:
    #             article_counts[article.magazine] += 1
    #     # Find magazine with max articles
    #     max_magazine = max(article_counts, key=article_counts.get, default=None)
    #     if article_counts[max_magazine] == 0:
    #         return None
    #     return max_magazine
class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or not title:
            raise Exception("Title must be a non-empty string")

        self.author = author
        self.magazine = magazine
        self._title = title  # store title privately

        Article.all.append(self)

    @property
    def title(self):
        return self._title

    # Make title immutable by not providing a setter

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            raise Exception("Author must be an instance of Author")
        self._author = new_author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            raise Exception("Magazine must be an instance of Magazine")
        self._magazine = new_magazine
