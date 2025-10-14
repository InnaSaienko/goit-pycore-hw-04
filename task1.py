def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as employees:
            salaries = [float(line.strip().split(',')[1]) for line in employees]
            total_salary = sum(salaries)
        return total_salary, total_salary / len(salaries)

    except FileNotFoundError:
        print(f"Error: File with path {path} doesn't exist.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    total_salary, average_salary = total_salary("./utils/salary.txt")
    print(f"Total salary: {total_salary}, Average salary: {average_salary}")
