# hierarchy-parser
This project provides a Python-based tool to parse class hierarchies from text files and to perform various operations to explore the relationships between classes. The tool reads data from two files: hierarchy.txt, which defines the parent-child relationships between classes, and id_to_name.txt, which maps class identifiers to human-readable names.

## Project Structure
- hierarchy.txt: This file contains the hierarchical relationships between classes in the format parent_id child_id.
- id_to_name.txt: This file maps class identifiers to their names in the format class_id class_name.
- class_hierarchy.py: This Python script contains the data structures and functions necessary to parse the files and answer queries about the class hierarchy.
## Setup
To run this project, you will need Python 3.6 or higher. No additional libraries are required beyond the Python Standard Library.

Clone the Repository: First, clone this repository to your local machine using:

```
git clone https://github.com/ttkien2035/hierarchy-parser.git
```

Prepare Your Data Files: Ensure hierarchy.txt and id_to_name.txt are placed in the project directory.

## Usage
To use this tool, you need to run the class_hierarchy.py script. Here's how you can execute and use the script:

Run the Script:

```
python class_hierarchy.py
```

## Functionality
### Data Structure
The main data structure used in this project is the ClassHierarchy class, which provides efficient storage and querying capabilities for class hierarchies.

Attributes:
children: A dictionary mapping each class to a set of its child classes.
parents: A dictionary mapping each class to its parent class.
name_map: A dictionary mapping each class identifier to its name.
### Operations
The ClassHierarchy class supports the following operations:

Find Siblings of a Class:

Method: find_siblings(class_id)
Description: Returns the sibling classes of the given class, i.e., other classes that share the same parent.
Find Parent of a Class:

Method: find_parent(class_id)
Description: Returns the parent class of the given class.
Find Ancestors of a Class:

Method: find_ancestors(class_id)
Description: Returns all ancestor classes of the given class, tracing up the hierarchy.
Check Common Ancestors:

Method: are_same_ancestors(class1, class2)
Description: Checks if the two given classes share any common ancestor.
