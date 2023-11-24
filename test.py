class Course:
  def __init__(self, course_name, 
               course_id, course_credits):
    self.course_name = course_name
    self.course_id = course_id
    self.course_credits = course_credits

    def __str__(self):
      return f"Course Name: {self.course_name}\nCourse ID = {self.course_id}\nCourse credits = {self.course_credits}"

class Student:
  def __init__(self, stu_name, stu_id):
    self.stu_name = stu_name
    self.stu_id = stu_id

  def __str__(self):
    return f"Name: {self.stu_name}\nID = {self.stu_id}"
  
  def addCourse(self, object):
    self.course = object

c1 = Course(course_name="套裝軟體應用", 
            course_id="(G0D17M01",
            course_credits=3)
s1 = Student(stu_name="潘紘毓", stu_id="4b1g0133")
s1.addCourse(c1)
print(s1)
