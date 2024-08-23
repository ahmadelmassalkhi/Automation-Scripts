

class Mark:
    def __init__(self, grade: float, credits: int) -> None:
        self.setGrade(grade)
        self.credits = credits

    def setGrade(self, grade: float):
        if grade < 0 or grade > 100:
            raise ValueError("Grade should be between 0 and 100 !")
        self.grade = grade

    def calculate_total(marks, totalCredits: int) -> float:
        # Ensure marks is a list of Mark objects
        if not all(isinstance(mark, Mark) for mark in marks):
            raise ValueError("`marks` should be a list of Mark objects")
        
        # Ensure total credits match totalCredits parameter
        if sum(mark.credits for mark in marks) != totalCredits:
            raise ValueError("Total credits in marks do not match totalCredits parameter")

        return sum(mark.grade * mark.credits for mark in marks) / totalCredits
    
    # optional
    def setName(self, name:str):
        self.name = name

marks = []
marks.append(Mark(78, 3))
marks.append(Mark(66, 4))
marks.append(Mark(63, 4))
marks.append(Mark(18, 4))
marks.append(Mark(28, 4))
marks.append(Mark(55, 3))
marks.append(Mark(41, 3))
marks.append(Mark(67, 5))

print(Mark.calculate_total(marks, 30))