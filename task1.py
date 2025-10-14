from functools import reduce


def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as employees:
            salaries = (float(line.strip().split(',')[1]) for line in employees)
            count, total_salary = reduce(lambda l, r: (r[0], l[1] + r[1]), enumerate(salaries, start=1))
        return total_salary, total_salary / count


    except FileNotFoundError:
        print(f"Error: File with path {path} doesn't exist.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    total_salary, average_salary = total_salary("./utils/salary.txt")
    print(f"Total salary: {total_salary}, Average salary: {average_salary}")
