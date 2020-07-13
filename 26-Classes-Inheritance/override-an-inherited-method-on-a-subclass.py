class Teacher():
    def teach_class(self):
        print("Teaching stuff...")

    def grab_lunch(self):
        print('Yum! Yum!')

    def grade_tests(self):
        print('F! F! F!')


class UniLecturer(Teacher):
    def publish_book(self):
        print("Hooray! I'm an author.")

    # To override an inherited method, simply define another method in that subclass that bears the same name with the
    # ... method you intend to override

    def grade_tests(self):
        print("A! A! A!")



teacher = Teacher()
lecturer = UniLecturer()

teacher.grade_tests()
teacher.grab_lunch()

lecturer.grade_tests()
lecturer.grab_lunch()