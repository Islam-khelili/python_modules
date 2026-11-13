def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))

    def print_days_recursive(i, days):
        if i > days:
            print("Harvest time!")
            return
        print(f"Day {i}")
        print_days_recursive(i + 1, days)

    print_days_recursive(1, days)
