class library_manager(dict):
    def __init__(self, name):
        """
        get the library manager unique id and set the value.
        :param name:
        :return:
        """
        self['user'] = name


    def add_item(self, type, type_id, owner, borrow_status, avaliable):
        """
        the method create the dictionary of the list.
        :param type:
        :param type_id:
        :param owner:
        :param borrow_status:
        :param avaliable:
        :return:
        """
        self['user']['type'] = type
        self['user']['type']['type_id'] = type_id
        self['user']['type']['owner'] = owner
        self['user']['type']['borrow_status'] = borrow_status
        self['user']['type']['avaliable'] = avaliable

    def remove_item(self, type):
        """
        remove the item from the dictionary.
        :param type:
        :return:
        """
        try :
            del self[user][type]
        except:
            print "Not avaliable"

class Book:
    def __init__(self, title, author, description, year, review):
        """
        set the book detatils for the detailed.
        :param title:
        :param author:
        :param description:
        :param year:
        :param review:
        :return:
        """
        self.title = title
        self.author = author
        self.summary = description
        self.year = year
        self.review = review

    def set_title(self, value):
        self.title = value

    def set_author(self, author):
        self.author = author

    def set_summary(self, summary):
        self.summary = summary

    def set_year(self, year):
        self.year = year

    def set_review(self, review):
        self.review = review


class Movie:
    def __init__(self, title, rating, actors, summary):
        self.title = title
        self.rating = rating
        self.actors = actors
        self.summary = summary

    def set_title(self, value):
        self.title = value

    def set_rating(self, value):
        self.rating = value

    def set_actors(self, value):
        self.actors = value

    def set_summary(self, value):
        self.summary = value
