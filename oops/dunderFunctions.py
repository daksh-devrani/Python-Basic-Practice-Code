class  Student:
    def __init__(self):
        self.marks=[]

    def __len__(self):
        return len(self.marks)

    def __getitem__(self,i):
        return(self.marks[i])

    def __repr__(self):
        return f'<the object contains {len(daksh)} marks >'

    def __str__(self):
        return f'the object contains {len(daksh)} marks'

daksh=Student()
daksh.marks.append(99)
daksh.marks.append(99)
daksh.marks.append(99)
print(daksh)