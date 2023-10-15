class Garden:
    def __init__(
        self,
        diagram,
        students=[
            "Alice",
            "Bob",
            "Charlie",
            "David",
            "Eve",
            "Fred",
            "Ginny",
            "Harriet",
            "Ileana",
            "Joseph",
            "Kincaid",
            "Larry",
        ],
    ):
        self.diagram = diagram.split("\n")
        self.students = sorted(students)
        self.num_students = len(self.students)

    def get_plant(self, plant):
        match plant:
            case "V":
                return "Violets"
            case "R":
                return "Radishes"
            case "C":
                return "Clover"
            case "G":
                return "Grass"
            case _:
                return None

    def plants(self, student):
        index = self.students.index(student)
        plants = []
        for i in range(2):
            for j in range(2):
                plants.append(self.get_plant(self.diagram[i][index * 2 + j]))
        return plants
