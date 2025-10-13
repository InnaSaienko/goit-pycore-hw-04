from pathlib import Path


def total_salary(path):
    total_salary = 0
    num_developers = 0
    try:
        with open(path, "r", encoding="utf-8") as employes:
            for line in employes:
                name, salary = line.strip().split(',')
                total_salary += float(salary)
                num_developers += 1
        return total_salary, round(total_salary / num_developers, 2)

    except FileNotFoundError:
        print(f"Error: File with path {path} doesn't exist.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    total, count = total_salary("./utils/salary.txt")
    print(f"Total salary: {total}, Average salary: {count}")
