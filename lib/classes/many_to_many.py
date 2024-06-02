class Article:
    # A class-level list to keep track of all Article instances
    all = []

    def __init__(self, author, magazine, title):
        # Initialize the Article with the provided author, magazine, and title
        self.author = author
        self.magazine = magazine
        self.title = title
        # Add this Article instance to the author's article list
        author._articles.append(self)
        # Add this Article instance to the magazine's article list
        magazine._articles.append(self)
        # Add this Article instance to the class-level list
        Article.all.append(self)

    @property
    def title(self):
        # Getter for the title property
        return self._title

    @title.setter
    def title(self, value):
        # Setter for the title property, with validation to ensure it's a string between 5 and 50 characters
        # Also ensures the title is immutable after being set once
        if not isinstance(value, str) or not (5 <= len(value) <= 50) or hasattr(self, '_title'):
            raise ValueError("Title must be a string between 5 and 50 characters. No take backs!")
        self._title = value

    @property
    def author(self):
        # Getter for the author property
        return self._author

    @author.setter
    def author(self, value):
        # Setter for the author property, with validation to ensure it's an instance of Author
        if not isinstance(value, Author):
            raise ValueError("The author must be a genuine Author, not an impostor!")
        self._author = value

    @property
    def magazine(self):
        # Getter for the magazine property
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        # Setter for the magazine property, with validation to ensure it's an instance of Magazine
        if not isinstance(value, Magazine):
            raise ValueError("Magazine must be an instance of Magazine, not a figment of your imagination!")
        self._magazine = value


class Author:
    def __init__(self, name):
        # Initialize the Author with the provided name, with validation to ensure it's a non-empty string
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string. A mystery author won't do!")
        self._name = name
        # Initialize an empty list to keep track of the author's articles
        self._articles = []

    @property
    def name(self):
        # Getter for the name property
        return self._name

    def articles(self):
        # Returns the list of articles written by the author
        return self._articles

    def magazines(self):
        # Returns a list of unique magazines in which the author has published articles
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        # Creates a new article and associates it with the author and the specified magazine
        article = Article(self, magazine, title)
        return article

    def topic_areas(self):
        # Returns a list of unique categories of magazines in which the author has published articles
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))


class Magazine:
    # A class-level list to keep track of all Magazine instances
    _instances = []

    def __init__(self, name, category):
        # Initialize the Magazine with the provided name and category, with validation
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters. Let's keep it concise!")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string. Don't be vague!")
        self._name = name
        self._category = category
        # Initialize an empty list to keep track of the magazine's articles
        self._articles = []
        # Add this Magazine instance to the class-level list
        Magazine._instances.append(self)

    @property
    def name(self):
        # Getter for the name property
        return self._name

    @name.setter
    def name(self, value):
        # Setter for the name property, with validation to ensure it's a string between 2 and 16 characters
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters. Brevity is the soul of wit!")
        self._name = value

    @property
    def category(self):
        # Getter for the category property
        return self._category

    @category.setter
    def category(self, value):
        # Setter for the category property, with validation to ensure it's a non-empty string
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string. No mysteries allowed!")
        self._category = value

    def articles(self):
        # Returns the list of articles published in the magazine
        return self._articles

    def contributors(self):
        # Returns a list of unique authors who have published articles in the magazine
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        # Returns a list of titles of articles published in the magazine
        titles = [article.title for article in self._articles]
        return titles if titles else None

    def contributing_authors(self):
        # Returns a list of authors who have published more than 2 articles in the magazine
        from collections import Counter
        author_counts = Counter(article.author for article in self._articles)
        authors = [author for author, count in author_counts.items() if count > 2]
        return authors if authors else None

    @staticmethod
    def top_publisher():
        # Create a list of magazines from all articles
        all_articles_by_magazine = [article.magazine for article in Article.all]
        # Initialize a variable to keep track of the magazine with the highest number of articles
        highest_total = [None, 0]
        # Iterate over each unique magazine and count the number of articles it has
        for magazine in set(all_articles_by_magazine):
            if all_articles_by_magazine.count(magazine) > highest_total[1]:
                highest_total = [magazine, all_articles_by_magazine.count(magazine)]
        # Return the magazine with the highest number of articles
        return highest_total[0]
