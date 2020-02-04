from vodafone_api.extensions import db


class Datetime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.Datetime, nullable=False)
    comment = db.Column(db.string())

    def __init__(self, **kwargs):
        super(USer, self).__init__(**kwargs)

    def __repr__(self):
        return "<Datatime %s>" % self.datetime
