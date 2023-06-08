from dictionary import db

class ITpassport(db.Model):
    __tablename__ = 'ITpassport'
    IT_word = db.Column('IT_word', db.String(10), primary_key = True)
    mean = db.Column('mean', db.String(50))    

    def __init__(self, IT_word=None, mean=None):
        self.IT_word = IT_word
        self.mean = mean

    def __repr__(self):
        return '<IT_word:{} mean:{}>'.format(self.IT_word, self.IT_word)