from pathlib import Path


def total_salary(path):
    total_salary = 0
    try:
        with open(path, "r", encoding="utf-8") as employees:
            for count, line in enumerate(employees, start=1):
                salary = line.strip().split(',')[1]
                total_salary += float(salary)
        return total_salary, round(total_salary / count, 2)

    except FileNotFoundError:
        print(f"Error: File with path {path} doesn't exist.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    total, count = total_salary("./utils/salary.txt")
    print(f"Total salary: {total}, Average salary: {count}")
