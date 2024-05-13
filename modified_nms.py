import numpy as np

def iou(boxA, boxB):
    """Compute the Intersection over Union (IoU) of two bounding boxes."""
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])

    interArea = max(0, xB - xA) * max(0, yB - yA)
    boxAArea = (boxA[2] - boxA[0]) * (boxA[3] - boxA[1])
    boxBArea = (boxB[2] - boxB[0]) * (boxB[3] - boxB[1])

    iou = interArea / float(boxAArea + boxBArea - interArea)
    return iou

def is_parent(child, parent, class_hierarchy):
    """Check if 'parent' is an ancestor of 'child' in the class hierarchy."""
    while child in class_hierarchy:
        if class_hierarchy[child] == parent:
            return True
        child = class_hierarchy[child]
    return False

def modified_nms(boxes, scores, classes, class_hierarchy, score_threshold, iou_threshold):
    """
    Apply the Modified Non-Maximum Suppression algorithm.

    Parameters:
    - boxes: List of bounding boxes [[x1, y1, x2, y2], ...]
    - scores: List of scores or confidences for each bounding box
    - classes: List of class labels for each bounding box
    - class_hierarchy: Dictionary mapping each class to its parent class
    - score_threshold: Minimum score for a box to be considered
    - iou_threshold: IoU threshold above which boxes are merged

    Returns:
    - List of indices of the boxes that are kept
    """
    # Filter boxes by score threshold
    indices = [i for i in range(len(scores)) if scores[i] >= score_threshold]
    boxes = [boxes[i] for i in indices]
    scores = [scores[i] for i in indices]
    classes = [classes[i] for i in indices]

    # Sort the bounding boxes by confidence score (descending)
    sorted_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)
    keep = []

    while sorted_indices:
        current_index = sorted_indices.pop(0)
        current_box = boxes[current_index]
        current_class = classes[current_index]
        keep.append(current_index)

        remove_indices = []
        for i in range(len(sorted_indices)):
            idx = sorted_indices[i]
            if iou(current_box, boxes[idx]) > iou_threshold:
                if classes[idx] == current_class:
                    # Case 2: Same class, lower confidence
                    remove_indices.append(i)
                elif is_parent(classes[idx], current_class, class_hierarchy):
                    # Case 3: Different classes, one is a parent of the other
                    remove_indices.append(i)
                elif is_parent(current_class, classes[idx], class_hierarchy):
                    keep.pop()  # Remove the current box because it is the parent
                    break

        sorted_indices = [idx for i, idx in enumerate(sorted_indices) if i not in remove_indices]

    return keep

# Example usage
if __name__ == "__main__":
    # Example bounding boxes (x1, y1, x2, y2 format)
    boxes = np.array([
        [100, 100, 200, 200],
        [150, 150, 250, 250],
        [120, 120, 180, 180],
        [300, 300, 400, 400]
    ])

    # Example scores
    scores = np.array([0.95, 0.9, 0.85, 0.88])

    # Example class labels
    classes = ['apple', 'apple', 'fruit', 'orange']

    # Example class hierarchy
    class_hierarchy = {'apple': 'fruit', 'orange': 'fruit'}

    # NMS parameters
    score_threshold = 0.8
    iou_threshold = 0.5

    # Apply modified NMS
    keep = modified_nms(boxes, scores, classes, class_hierarchy, score_threshold, iou_threshold)
    print("Indices of boxes to keep:", keep)
