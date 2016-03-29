import unittest
from contacts import contact,contacts_manager
from library import Book,Movie,library_manager


class MyTest(unittest.TestCase):
    def test_create_contact(self):
        a = contact(1,'Ashish','pundir.ashish@live.com','9787619875','Thano, dehradun')
        b = contact(2,'Anurag','pundir.ashish1@live.com','9787629875','Thano, dehradun')
        c = contact(3,'Kuldeep','pundir.ashish2@live.com','9787639875','Thano, dehradun')
        d = contact(4,'Rachit','pundir.ashish3@live.com','9787649875','Thano, dehradun')
        e = contact(5,'Omkar','pundir.ashish4@live.com','9787659875','Thano, dehradun')
        f = contact(6,'Krishna','pundir.ashish5@live.com','9787669875','Thano, dehradun')
        g = contact(7,'Pandey','pundir.ashish6@live.com','9787679875','Thano, dehradun')
        h = contact(8,'Vaibhav','pundir.ashish7@live.com','9787689875','Thano, dehradun')
        i = contact(9,'Anil','pundir.ashish8@live.com','9787699875','Thano, dehradun')
        cm = contacts_manager([a,b,c,d,e,f,g,h,i])
        self.assertEqual(len(cm.view_contacts()),9)

    def test_create_book(self):
        try:
            a = Book("ABC", "Collins", "laksjfls jlks dglk ; jsdj;l jlsd ; ", "2014", "4/5")
            b = Book("DEF", "Collins", "laksjfls jlks dglk ; jsdj;l jlsd ; ", "2014", "4/5")
            c = Book("GHI", "Robbins", "laksjfls jlks dglksdj;l jlsd ; ", "2011", "3.3/5")
            count = 0
        except:
            count = 1
        self.assertEqual(count,0)

    def test_create_library(self):
        try:
            a = Book("ABC", "Collins", "laksjfls jlks dglk ; jsdj;l jlsd ; ", "2014", "4/5")
            b = Book("DEF", "Collins", "laksjfls jlks dglk ; jsdj;l jlsd ; ", "2014", "4/5")
            c = Book("GHI", "Robbins", "laksjfls jlks dglksdj;l jlsd ; ", "2011", "3.3/5")
            lm = library_manager
            lm.add_item(a, 001, 'ASHISH', 'OWNED', 'NO')
            count = 0
        except:
            count = 1
        self.assertEqual(count,0)


if __name__ == '__main__':
    unittest.main()