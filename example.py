def sweap_max(items: list) -> list:
    max_pos = 0
    for i in range(len(items)):
        if items[i] >= items[max_pos]:
            max_pos = i
    items[0], items[max_pos] = items[max_pos], items[0]
    return items


if __name__ == "__main__":
    items = [1, 10, 12, 100, 6]
    print(sweap_max(items))
