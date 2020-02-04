from vodafone_api.extensions import db


class Datetime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DATETIME, nullable=False)
    comment = db.Column(db.VARCHAR(1000))

    def __init__(self, **kwargs):
        super(USer, self).__init__(**kwargs)

    def __repr__(self):
        return "<Datatime %s>" % self.datetime
