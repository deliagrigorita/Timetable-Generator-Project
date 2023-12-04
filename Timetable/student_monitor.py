class StudentCountMonitor:
    student_count = 0

    def max_student_count(self):
        """Property: Maximum allowed student count is 100"""
        return self.student_count <= 4

    def violation_handler(self, prop_name):
        print(f"Violation: Property {prop_name} violated - Student count exceeds!")

    def validation_handler(self, prop_name):
        print(f"Validation: Property {prop_name} holds - Student count is within limits")


def simulate_student_addition(student_monitor):

   for _ in range(11):
       student_monitor.student_count += 1
       if not student_monitor.max_student_count():
           student_monitor.violation_handler('max_student_count')

