class Player:
    def __init__(self, name, position, skill, country):
        self.name = name
        self.country = country
        self.position = position
        self.skill = skill

    def show_full_info(self):
        print(f"Name: {self.name}\nNationality: {self.country}\nPosition: {self.position}\nSkill: {self.skill}")

    def show_info(self):
        print(f"{self.name} | {self.position} | {self.skill} | {self.country}")

    def get_skill(self):
        return self.skill

    def get_position(self):
        return self.position