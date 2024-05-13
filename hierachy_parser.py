

def read_hierarchy_file(file_path):
    """
    Reads a hierarchy file where each line is in the format 'parent child'.
    
    :param file_path: Path to the hierarchy file.
    :return: A list of tuples, where each tuple represents a (parent, child) relationship.
    """
    hierarchy = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 2:
                hierarchy.append((parts[0], parts[1]))
    return hierarchy

def read_id_to_name_file(file_path):
    """
    Reads an ID to name file where each line is in the format 'id name'.
    
    :param file_path: Path to the id_to_name file.
    :return: A dictionary mapping class IDs to names.
    """
    id_to_name = {}
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(maxsplit=1)
            if len(parts) == 2:
                id_to_name[parts[0]] = parts[1]
    return id_to_name


class ClassHierarchy:
    def __init__(self):
        self.children = {}
        self.parents = {}
        self.name_map = {}

    def load_hierarchy_from_file(self, file_path):
        hierarchy = read_hierarchy_file(file_path)
        for parent, child in hierarchy:
            if parent not in self.children:
                self.children[parent] = set()
            self.children[parent].add(child)
            self.parents[child] = parent

    def load_id_to_name_from_file(self, file_path):
        self.name_map = read_id_to_name_file(file_path)

    def find_siblings(self, class_id):
        if class_id not in self.parents:
            return set()
        parent = self.parents[class_id]
        return self.children[parent] - {class_id}

    def find_parent(self, class_id):
        return self.parents.get(class_id, None)

    def find_ancestors(self, class_id):
        ancestors = set()
        current = class_id
        while current in self.parents:
            current = self.parents[current]
            ancestors.add(current)
        return ancestors

    def are_same_ancestors(self, class1, class2):
        ancestors1 = self.find_ancestors(class1)
        ancestors2 = self.find_ancestors(class2)
        return not ancestors1.isdisjoint(ancestors2)

    def get_name(self, class_id):
        return self.name_map.get(class_id, "Unknown")

if __name__ == "__main__":
    # Create the hierarchy structure
    h = ClassHierarchy()

    # Load data from files
    h.load_hierarchy_from_file('hierarchy.txt')
    h.load_id_to_name_from_file('id_to_name.txt')

    # Example operations
    print("Siblings of n02473983:", h.find_siblings("n02473983"))
    print("Parent of n02473983:", h.get_name(h.find_parent("n02473983")))
    print("Ancestors of n02473983:", {h.get_name(anc) for anc in h.find_ancestors("n02473983")})
    print("Same Ancestors (n02473983, n02478875):", h.are_same_ancestors("n02473983", "n02478875"))

