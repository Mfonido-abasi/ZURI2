   # [assignment] Skeleton class. Add your code here
    def __init__(self,name,age,track, score):
        self.name = str(name)
        self.age = int(age)
        self.track = list(track)
        self.score = float(score)
        
      
    def change_name(Bob, newname):
        Bob.change_name = newname
       

    def change_age(Bob, newage):
        Bob.change_age = newage
        
    def add_track(Bob, newtrack):
        Bob.add_track = newtrack
        

    def get_score(Bob, score):
        Bob.get_score = score
        
Bob = Student(name="Bob", age=26, track=["FE","BE"], score=20.90)
print("Student on record is", Bob.name)
print("Bob is", Bob.age, "years old")
print("Bob's track is", Bob.track)
print("Bob's score is", Bob.score)

Bob.change_name = str(input("What's your name?"))
Bob.change_age= int(input("How old are you?"))
Bob.add_track = list(input("What's your track"))
Bob.get_score = Bob.score

print("The new Student is", Bob.change_name)
print("The new Student is", Bob.change_age, "years old")
print("The new Student's tracks is", Bob.add_track + Bob.track)
print("Student's score is", Bob.get_score)



