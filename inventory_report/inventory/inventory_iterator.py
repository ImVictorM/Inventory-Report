from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data):
        self.data = data
        self.current_index = 0

    def __next__(self):
        try:
            current_data = self.data[self.current_index]
        except IndexError:
            raise StopIteration()
        else:
            self.current_index += 1
            return current_data
