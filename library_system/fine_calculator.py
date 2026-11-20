
class FineCalculator:
    def calculate(self, days_overdue):
        if days_overdue <= 0:
            return 0

        fine = days_overdue * 5000

        if days_overdue > 10:
            fine = fine * 1.2

        return fine
