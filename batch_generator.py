class BatchGenerator:
    def __init__(self, array):
        self.array = array
    
    def generate(self):
        batch = []
        batch_size = 0
        has_been_yielded = False
        for item in self.array:
            item_size = len(item.encode("utf-8"))
            if item_size <= 1000000:
                if batch_size + item_size > 5000000 or len(batch) == 500:
                    has_been_yielded = True
                    yield batch
                    batch = [item]
                    batch_size = int(item_size)
                else:
                    batch.append(item)
                    batch_size += item_size
        if not has_been_yielded or len(batch) > 0:
            yield batch
    
    def array_of_batches(self):
        return [item for item in self.generate()]

