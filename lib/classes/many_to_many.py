class Article:  # link between author and magazine
    all_articles = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or not 5 <= len(title) <= 50:
            raise ValueError("Title must be a string between 5 and 50 characters.")
        if not isinstance(author, Author):
            raise TypeError("Author must be in Author class.")
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be in Magazine class.")

        self._title = title
        self._author = author
        self._magazine = magazine
        Article.all_articles.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine


class Author:
    all_authors = []

    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")

        self._name = name
        Author.all_authors.append(self)

    @property
    def name(self):
        return self._name

    def articles(self):
        return [article for article in Article.all_articles if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        categories = list(set(article.magazine.category for article in self.articles()))
        return categories if categories else None


class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters long")

        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string")
        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, m_name):
        if isinstance(m_name, str) and 2 <= len(m_name) <= 16:
            self._name = m_name
        else:
            raise ValueError(
                "Magazine name must be a string between 2 and 16 characters long"
            )

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, m_category):
        if isinstance(m_category, str) and len(m_category) > 0:
            self._category = m_category
        else:
            raise ValueError("Category must be a non-empty string")

    def articles(self):
        return [article for article in Article.all_articles if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        author_count = {}
        for article in self.articles():
            author = article.author
            author_count[author] = author_count.get(author, 0) + 1

        contributors = [author for author, count in author_count.items() if count > 2]
        return contributors if contributors else None
