import sys

inventory = {}

if __name__ == "__main__":
    print("=== Inventory System Analysis ===")

    for arg in sys.argv[1:]:
        parts = arg.split(":")

        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
        else:
            try:
                quantity = int(parts[1])
            except ValueError as e:
                print(f"Quantity error for '{parts[0]}': {e}")
                continue

            if parts[0] in inventory:
                print(f"Redundant item '{parts[0]}' - discarding")
            else:
                inventory[parts[0]] = quantity  # d["key"] = value

    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")

    total = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total}")

    for item in inventory:
        percentage = round(inventory[item] / total * 100, 1)
        print(f"Item {item} represents {percentage}%")

    most = max(inventory, key=inventory.get)    # key with the highest value
    least = min(inventory, key=inventory.get)
    print(f"Item most abundant: {most} with quantity {inventory[most]}")
    print(f"Item least abundant: {least} with quantity {inventory[least]}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")
