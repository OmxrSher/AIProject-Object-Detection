import os
from collections import defaultdict

DATASET_BASE = r"C:\Users\omars\OneDrive\Desktop\AIProj\custom_dataset"

CLASS_NAMES = {
    0: "plastic_bottle",
    1: "can",
    2: "paper_waste",
    3: "general_bin",
    4: "recycling_bin",
}

def main():
    image_counts = defaultdict(int)
    annotation_counts = defaultdict(int)

    for split in ["train", "valid", "test"]:
        label_dir = os.path.join(DATASET_BASE, split, "labels")
        if not os.path.exists(label_dir):
            continue

        for label_file in os.listdir(label_dir):
            if not label_file.endswith(".txt"):
                continue

            path = os.path.join(label_dir, label_file)
            present = set()

            with open(path, "r") as f:
                for line in f:
                    parts = line.strip().split()
                    if len(parts) < 5:
                        continue
                    cls = int(parts[0])
                    annotation_counts[cls] += 1
                    present.add(cls)

            for cls in present:
                image_counts[cls] += 1

    print("\n===== FINAL MERGED DATASET COUNTS =====")
    total_images_across_classes = 0
    for cls_id in range(5):
        img_count = image_counts[cls_id]
        ann_count = annotation_counts[cls_id]
        total_images_across_classes += img_count
        status = "PASS" if img_count >= 200 else "FAIL"
        print(f"{CLASS_NAMES[cls_id]} -> images: {img_count}, annotations: {ann_count}, requirement: {status}")

    print(f"\nCombined image appearances across classes: {total_images_across_classes}")
    print("Note: one image may contain multiple classes, so this is not the unique dataset image count.")

if __name__ == "__main__":
    main()