class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        new_salary = salary[1:-1]
        mean_salary = sum(new_salary) / len(new_salary)
        
        return mean_salary
