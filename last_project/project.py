from loggers.loggers import logger2, logger


class FlatIterator:
    def __init__(self, list_of_list):
        self.flat_list = []
        self.set_flat(list_of_list)
        self.counter = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        if self.counter >= len(self.flat_list):
            raise StopIteration
        return self.flat_list[self.counter]

    def set_flat(self, list_of_lists):
        for pos, element in enumerate(list_of_lists):
            if type(element) is list:
                self.set_flat(list_of_lists[pos])
            else:
                self.flat_list.append(element)


@logger
@logger2("log_4.log")
def project_run():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    return FlatIterator(list_of_lists_1)
