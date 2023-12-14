from models.db import db


class Team:
    def __init__(self, name, players=None, _id=None):
        self._id = _id
        self.name = name
        self.players = players or []

    def to_dict(self):
        return {
            "name": self.name,
            "players": [player.to_dict() for player in self.players],
        }

    def save(self):
        db.teams.insert_one(self.to_dict())

    @staticmethod
    def find_all():
        teams = db.teams.find()
        return [Team(**team) for team in teams]

    @staticmethod
    def find_by_name(name):
        team = db.teams.find_one({"name": name})
        if team:
            return Team(**team)
        return None

    def update(self):
        db.teams.update_one({"_id": self._id}, {"$set": self.to_dict()})

    def delete(self):
        db.teams.delete_one({"name": self.name})
