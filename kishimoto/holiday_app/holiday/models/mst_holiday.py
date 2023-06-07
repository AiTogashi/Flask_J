from holiday import db 
from datetime import datetime 


#データベースからデータを取得
class Holiday(db.Model): 
    __tablename__ = 'holiday' 
    holi_date = db.Column(db.DateTime, primary_key = True)
    holi_text = db.Column(db.String(20))

    def __init__(self, holi_date=None, holi_text=None):
        self.holi_date = holi_date
        self.holi_text = holi_text

    # def __repr__(self): 
    #     return '<Entry id:{} title:{} text:{}>'.format(self.id, self.title, self.text)

