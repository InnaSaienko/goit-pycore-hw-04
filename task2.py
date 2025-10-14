def get_cats_info(path):
    try:
        with open(path, "r", encoding="utf-8") as cats:
            cats_info= list(
                map(
                    lambda line: {"id": line.strip().split(',')[0],
                                    "name": line.strip().split(',')[1],
                                    "age": line.strip().split(',')[2]},
                cats))
        return cats_info

    except FileNotFoundError:
        print(f"Error: File with path {path} doesn't exist.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    cats = get_cats_info("./utils/cats_info.txt")
    print(f"List of all cats: {cats}")
