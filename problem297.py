def find_file(folder, target):
    for item in folder:

        if isinstance(item, dict):
            result = find_file(item.values(), target)

            if result:
                return result

        elif item == target:
            return True

    return False