
class Developer:
    def __init__(self, name):
        self.name = name
        self.completed_missions = []
        self.total_working_days = 0
        self._total_payment = 0
        self.to_do_missions = []
        self.experience = 1.0

    def complete_mission(self, mission):
        if mission.developer is not None and mission.developer != self:
            raise ValueError("developer not supposed to do that mission")
        mission.mark_as_done()
        self.completed_missions.append(mission)
        self.total_working_days += mission.working_days
        self._total_payment += mission.payment()
        self.experience += mission.complicated_mission

    def get_incomplete_missions(self):
        return self.to_do_missions
    
    def __str__(self):
        return f"developer : {self.name}, {self.completed_missions} {self.total_working_days}, {self._total_payment}, {self.to_do_missions}, {self.experience} "