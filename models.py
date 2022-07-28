import enum

from extensions import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)

    bar_id = db.Column(db.Integer, db.ForeignKey("bar.id"))
    bar = db.relationship("Bar", backref=db.backref("bar"))


class Gender(enum.IntEnum):
    MALE = enum.auto()
    FEMALE = enum.auto()
    OTHER = enum.auto()

    @staticmethod
    def from_string(gender_name: str):
        if gender_name.lower() == "female":
            return Gender.FEMALE
        elif gender_name.lower() == "male":
            return Gender.MALE
        return Gender.OTHER

    def __str__(self):
        match self:
            case Gender.MALE:
                return "male"
            case Gender.FEMALE:
                return "female"
            case Gender.OTHER:
                return "other"


class Profile(db.Model):
    __tablename__ = "profile"
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    gender = db.Column(db.Enum(Gender))

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User", backref=db.backref("user", uselist=False))


class Bar(db.Model):
    __tablename__ = "bar"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User", backref=db.backref("user"))
