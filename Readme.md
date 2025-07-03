# Network Intrusion Detection System (NIDS) - NSL-KDD Based

## 📜 Project Overview
This project implements a Machine Learning-based Network Intrusion Detection System (NIDS) using the NSL-KDD dataset. It includes:

- Preprocessing of the NSL-KDD dataset.
- Building and training a Random Forest Classifier for intrusion detection.
- A live network packet monitor using Scapy that classifies packets in real-time.

---

## 📂 Project Structure

```
Nids_project/
├── Dataset/                  # Contains the NSL-KDD dataset files
├── models/                    # Saved ML models (.pkl)
├── scripts/
│   ├── nids_preprocess.py     # Dataset preprocessing script
│   ├── nids_model.py          # Model training and saving script
│   ├── nids_detector.py       # Single sample detection script
│   └── live_network_nids.py   # Real-time network packet detection using Scapy
├── Readme.md                  # Project documentation (this file)
├── requirements.txt           # Python dependencies
└── test_nids_project.py       # Script to test all the components
```

---

## ⚙️ Installation

1. **Clone the Repository:**

```bash
git clone <repo-url>
cd Nids_project
```

2. **Install Required Libraries:**

```bash
pip install -r requirements.txt
```

3. **(Windows Users)** Install [Npcap](https://npcap.com/#download) for live traffic capture.
   - ✔️ Enable "WinPcap API-compatible Mode."
   - ✔️ Enable "Support raw 802.11 traffic."

---

## 🚀 Running the Project

### 1. Preprocess Dataset
```bash
cd scripts
python nids_preprocess.py
```

### 2. Train Model
```bash
python nids_model.py
```

### 3. Test on a Single Sample
```bash
python nids_detector.py
```

### 4. Start Live Network Monitoring (Admin permissions required)
```bash
python live_network_nids.py
```
Press `Ctrl+C` to stop the monitor.

### 5. Run Full Project Test
```bash
cd ..
python test_nids_project.py
```

---

## 📊 Results Example

```
🔍 Starting Live Network Intrusion Detection... Press Ctrl+C to stop.
[+] Packet Detected - Protocol: TCP, Predicted Attack Type: 20
[+] Packet Detected - Protocol: UDP, Predicted Attack Type: 17
```

---

## 🛡️ Future Improvements

- Add more accurate packet feature extraction.
- Integrate advanced ML models like XGBoost or Deep Learning.
- Build a web interface for real-time monitoring.

---

## 👨‍💻 Author
Vishnu Vardhan Burri  
LinkedIn: [https://www.linkedin.com/in/vishnu-vardhanburri/](https://www.linkedin.com/in/vishnu-vardhanburri/)  
GitHub: [https://github.com/vishnunaniinfo](https://github.com/vishnunaniinfo)

---

## 📄 License
This project is for educational purposes.

---

✅ **Project Completed Successfully**.