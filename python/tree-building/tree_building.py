class Record:
    def __init__(self, record_id: int, parent_id: int):
        self.record_id: int = record_id
        self.parent_id: int = parent_id

class Node:
    def __init__(self, node_id: int):
        self.node_id: int = node_id
        self.children: list = []

def BuildTree(records: list[Record]):
    records.sort(key=lambda record: record.record_id)
    node_dict: dict[int, Node] = {record.record_id: Node(record.record_id) for record in records}
    record_ids = [record.record_id for record in records]
    root: None | Node = None

    # Empty case
    if not records:
        return None
    
    # Non-continuous record ids
    if not all(i == record_id for i, record_id in enumerate(record_ids)):
        raise ValueError("Record id is invalid or out of order.")

    for record in records:
        # Root node parent_id should be 0
        if record.record_id == 0 and record.parent_id != 0:
            raise ValueError("Node parent_id should be smaller than it's record_id.")
        
        # Non-root node parent_id is equal to it's record_id
        if record.record_id != 0 and record.parent_id == record.record_id:
            raise ValueError("Only root should have equal record and parent id.")

        # Non-root node parent_id should be smaller than it's record_id
        if record.record_id != 0 and record.parent_id >= record.record_id:
            raise ValueError("Node parent_id should be smaller than it's record_id.")
        
        # Root case
        if record.record_id == 0:
            root = node_dict[record.record_id]

        # Normal case
        if record.record_id != record.parent_id:
            try:
                node_dict[record.parent_id].children.append(node_dict[record.record_id])
            except KeyError:
                raise ValueError("Record id is invalid or out of order.")
        
    # Root does not exist
    if root is None:
        raise ValueError("Record id is invalid or out of order.")
    
    return root
    
# TEST

records = [
            Record(6, 2),
            Record(0, 0),
            Record(3, 1),
            Record(2, 0),
            Record(4, 1),
            Record(5, 2),
            Record(1, 0)
        ]
root = BuildTree(records)
print(root)
    