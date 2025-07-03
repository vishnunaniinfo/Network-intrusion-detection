import subprocess

print("\n🔍 Step 1: Running Preprocessing Script...")
preprocess = subprocess.run(["python", "scripts/nids_preprocess.py"])
if preprocess.returncode == 0:
    print("✅ Preprocessing completed successfully.\n")
else:
    print("❌ Preprocessing failed.\n")

print("\n🔍 Step 2: Running Model Training Script...")
model_train = subprocess.run(["python", "scripts/nids_model.py"])
if model_train.returncode == 0:
    print("✅ Model trained and saved successfully.\n")
else:
    print("❌ Model training failed.\n")

print("\n🔍 Step 3: Running Attack Detection Script...")
detection = subprocess.run(["python", "scripts/nids_detector.py"])
if detection.returncode == 0:
    print("✅ Detection test completed successfully.\n")
else:
    print("❌ Detection test failed.\n")

print("\n✅ Full Project Test Completed!")
