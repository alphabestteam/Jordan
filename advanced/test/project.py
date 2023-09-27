from datetime import datetime, timedelta
class Project:
    def __init__(self, description, start_date):
        self.description = description
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d')
        self.missions = [] 
        self.developers = []
        self.end_date = None
        self.completed_missions = []
        self.missions_to_do = []
        self._total_cost = 0
        self._is_completed = False
       
    def add_mission(self, mission):
        if mission.project is not None and mission.project != self:
            raise ValueError("mission belongs to another project")
        self.missions.append(mission)
        if mission._is_done:
            self.completed_missions.append(mission)
        else:
            self.missions_to_do.append(mission)
        mission.project = self
        self.calculate_end_date()  

    def remove_mission(self, mission):
        if mission in self.missions:
            self.missions.remove(mission)
            if mission._is_done:
                self.completed_missions.remove(mission)
            else:
                self.missions_to_do.remove(mission)
            mission.project = None
            self.developers.remove(mission.developer)
            self.calculate_end_date() 
        else:
            raise ValueError("mission already not in project")


    def add_developer(self, developer):
        if developer not in self.developers:
            self.developers.append(developer)
        else:
            raise ValueError("developer is already in this project ")

    def calculate_end_date(self):
        working_days = sum(mission.working_days for mission in self.missions)
        current_date = self.start_date
        while working_days > 0:
            current_date += timedelta(days=1)
            working_days -= 1
        self.end_date = current_date.strftime('%Y-%m-%d')
        return self.end_date
    
    def find_missions_by_description(self, description):
        return [mission for mission in self.missions if description in mission.description]

    def get_project_cost(self):
        return sum(mission.payment for mission in self.completed_missions)
    
    def project_completed(self):
        return all(mission._is_done for mission in self.missions)
          