import data_operations


def make_inventory_list():
    inventory_list = data_operations.generate_list_from_txt('inventory.txt')
    return inventory_list

labels_list = ['typ/marka', 'nr inwentarzowy',
               'gdzie', 'stan']
