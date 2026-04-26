# ♻️ Campus Sustainability Monitoring using YOLOv8

## 📌 Project Overview
This project presents an AI-based object detection system for monitoring campus sustainability through automated waste detection. The model is designed to detect and classify key waste-related objects in real-world environments.

### 🎯 Target Classes
- Plastic Bottles  
- Paper Waste  
- Recycling Bins  
- General Waste Bins  

The system aims to support smarter waste management and improve sustainability practices on campus.

---

## 🧠 Model Architecture
- Model: YOLOv8 (Ultralytics)
- Task: Object Detection
- Variants Tested: YOLOv8n, YOLOv8s

YOLOv8 was selected due to its strong balance between detection accuracy and computational efficiency.

---

## 📂 Project Structure

AIPROJ/
│
├── scripts/ # Training and inference scripts
├── results/ # Final outputs and evaluation
│ ├── final_model_saved/
│ ├── val_results/
│ ├── unseen_test/
│ ├── unseen_test2/
│ ├── unseen_test3/
│ ├── predict_results/
│ └── final_metrics.csv
│
├── runs/ # Training logs, curves, and metrics
├── custom_dataset/ # Dataset (excluded from repository)
├── dataset_sources/ # Dataset sources (excluded)
├── demo_images/ # Demo/test images (excluded)


---

## ⚙️ Training Configuration
- Image Size: 512 × 512  
- Epochs: 60  
- Batch Size: 8  
- Early Stopping (Patience): Enabled  

### 🔄 Data Augmentation
- Rotation (degrees)
- Translation
- Scaling
- Horizontal flipping
- HSV color augmentation
- Mosaic augmentation

These techniques improve generalization and reduce bias.

---

## 📊 Results Summary

| Metric        | Value |
|--------------|------|
| Precision     | ~0.97 |
| Recall        | ~0.94 |
| mAP@0.5       | ~0.96 |

The model achieves strong performance across all classes, demonstrating effective detection capability.

---

## 📈 Evaluation

The repository includes full evaluation outputs:

- 📉 Training & validation loss curves (`runs/`)
- 📊 Confusion matrix
- 📈 Precision–Recall curve
- 📉 F1–Confidence curve
- 📄 Final metrics (`final_metrics.csv`)

### ✅ Key Observations
- Stable convergence during training
- No significant overfitting observed
- Strong generalization on unseen test images

---

## ⚠️ Limitations
- Reduced performance on:
  - Small objects  
  - Occluded or cluttered scenes  
- Dataset simplicity may influence high accuracy metrics  

---

## 🚀 How to Run

### 1️⃣ Install Dependencies
```bash
pip install ultralytics

2️⃣ Train the Model
python scripts/train.py

3️⃣ Run Inference
python scripts/predict.py

📌 Notes
Dataset is excluded due to size limitations
Full training outputs (runs/) are included for transparency
Results are reproducible using the provided scripts
