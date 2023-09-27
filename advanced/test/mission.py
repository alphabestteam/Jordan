
import datetime 
class Mission:
    def __init__ (self, description, opening_date, project, working_days ,complicated_mission, developer = None):
        self.description = description
        self.opening_date = opening_date 
        self.project = project
        self.end_date = None
        self.working_days = working_days
        self.complicated_mission = complicated_mission
        self.developer= developer
        self._payment = 0
        self._is_done = False

    def calculate_end_date(self):
        if self.developer is None:
            raise ValueError("there isn't any developer belongs to the mission so end date can't be calculate")
        current_date = datetime.datetime.strptime(self.opening_date, '%Y-%m-%d')  
        while self.working_days > 0:
            current_date += datetime.timedelta(days=1)
            self.working_days -= 1
        self.end_date = current_date.strftime('%Y-%m-%d')
        return self.end_date

    def developer_to_mission(self, developer1):
        if self.developer is None:
            self.developer = developer1
        else:
            raise ValueError("the mission was already given to another developer")

    def mark_as_done(self, developer1):
        if self.developer is developer1:
            self._is_done = True
        else:
            raise ValueError("developer is not supposed to do that mission")

    @property
    def payment(self):
        if self.developer is None:
            return 0
        self._payment = self.developer.experience * (self.complicated_mission / self.working_days)
        return self._payment

    def set_complication(self, value):
        if value < 1 or value > 5:
            raise ValueError("has to be between 1 to 5")
        self.complicated_mission = value
    
    def __str__(self):
        return f"mission : {self.description}, {self.opening_date}, {self.project}, {self.end_date}, {self.working_days},{self.complicated_mission},{self.developer}, {self._payment}, {self._is_done}"
