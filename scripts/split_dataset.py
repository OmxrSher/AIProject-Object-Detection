import os
import random
import shutil

random.seed(42)

SOURCE_IMAGES = "custom_dataset/all/images"
SOURCE_LABELS = "custom_dataset/all/labels"

TARGET_BASE = "custom_dataset"

SPLITS = {
    "train": 0.70,
    "valid": 0.15,
    "test": 0.15
}

def ensure_dirs():
    for split in SPLITS:
        split_path = os.path.join(TARGET_BASE, split)

        # 🔥 delete old split if exists
        if os.path.exists(split_path):
            shutil.rmtree(split_path)

        os.makedirs(os.path.join(split_path, "images"), exist_ok=True)
        os.makedirs(os.path.join(split_path, "labels"), exist_ok=True)
        
def get_image_files():
    valid_exts = (".jpg", ".jpeg", ".png")
    return [f for f in os.listdir(SOURCE_IMAGES) if f.lower().endswith(valid_exts)]

def split_files(files):
    random.shuffle(files)

    total = len(files)
    train_end = int(total * SPLITS["train"])
    valid_end = train_end + int(total * SPLITS["valid"])

    return {
        "train": files[:train_end],
        "valid": files[train_end:valid_end],
        "test": files[valid_end:]
    }

def copy_split(files_by_split):
    for split, files in files_by_split.items():
        for file in files:
            src_img = os.path.join(SOURCE_IMAGES, file)
            src_lbl = os.path.join(
                SOURCE_LABELS,
                os.path.splitext(file)[0] + ".txt"
            )

            dst_img = os.path.join(TARGET_BASE, split, "images", file)
            dst_lbl = os.path.join(TARGET_BASE, split, "labels", os.path.splitext(file)[0] + ".txt")

            shutil.copy(src_img, dst_img)

            if os.path.exists(src_lbl):
                shutil.copy(src_lbl, dst_lbl)

def main():
    ensure_dirs()
    files = get_image_files()
    files_by_split = split_files(files)
    copy_split(files_by_split)

    print("✅ Split complete.")
    for split, split_files_list in files_by_split.items():
        print(f"{split}: {len(split_files_list)} images")

if __name__ == "__main__":
    main()