from developer import Developer
from mission import Mission
from project import Project

def main():
    dev1 = Developer("jordan")
    dev2 = Developer("gilad")
    project = Project("My Project", "2023-09-19")
    mission1 = Mission("Mission 1", "2023-09-20", project, 5, 3,dev1)
    mission2 = Mission("Mission 2", "2023-09-21", project, 3,5, dev2)
    project.add_mission(mission1)
    print(mission1.payment)
    project.add_mission(mission2)
    print(project.calculate_end_date())
    project.find_missions_by_description("Mission 1 ")
    mission1.mark_as_done(dev1)
    mission2.mark_as_done(dev2)
    print(project.get_project_cost())
    print(project.project_completed())
if __name__ == "__main__":
    main()
