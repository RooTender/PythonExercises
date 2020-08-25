def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(k + ': ' + str(v))
        item_total += v
    print("All items count: " + str(item_total) + "\n")

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1

# game
playerInventory = {'torches': 4, 'arrows': 23, 'gold': 15, 'raw steak': 5}
displayInventory(playerInventory)

dragonLoot = ['torches', 'gold', 'gold', 'raw steak', 'gold']
addToInventory(playerInventory, dragonLoot)
displayInventory(playerInventory)
