"""
Fantasy Game Inventory.
"""

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42,
         'dagger': 1, 'arrow': 12, 'map fragments': 3}


def displayInventory(inventory):
    """
    Print contents and total number of items in inventory.
    """
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print('Total number of items : ' + str(item_total))


displayInventory(stuff)

print()  # For display reasons when running both projects
