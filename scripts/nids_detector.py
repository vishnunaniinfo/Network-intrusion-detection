import pandas as pd
import joblib

# Load model
model = joblib.load("nids_model.pkl")

# Attack labels
attack_labels = {
    0: 'back', 1: 'buffer_overflow', 2: 'ftp_write', 3: 'guess_passwd', 4: 'imap',
    5: 'ipsweep', 6: 'land', 7: 'loadmodule', 8: 'multihop', 9: 'neptune',
    10: 'nmap', 11: 'normal', 12: 'perl', 13: 'phf', 14: 'pod', 15: 'portsweep',
    16: 'rootkit', 17: 'satan', 18: 'smurf', 19: 'spy', 20: 'teardrop', 21: 'warezclient'
}

# Example input
sample_data = {
    'duration': 0,
    'protocol_type': 1,
    'service': 1,
    'flag': 0,
    'src_bytes': 491,
    'dst_bytes': 0,
    'land': 0,
    'wrong_fragment': 0,
    'urgent': 0,
    'hot': 0,
    'num_failed_logins': 0,
    'logged_in': 0,
    'num_compromised': 0,
    'root_shell': 0,
    'su_attempted': 0,
    'num_root': 0,
    'num_file_creations': 0,
    'num_shells': 0,
    'num_access_files': 0,
    'num_outbound_cmds': 0,
    'is_host_login': 0,
    'is_guest_login': 0,
    'count': 2,
    'srv_count': 2,
    'serror_rate': 0.0,
    'srv_serror_rate': 0.0,
    'rerror_rate': 0.0,
    'srv_rerror_rate': 0.0,
    'same_srv_rate': 0.0,
    'diff_srv_rate': 0.0,
    'srv_diff_host_rate': 0,
    'dst_host_count': 150,
    'dst_host_srv_count': 25,
    'dst_host_same_srv_rate': 0.17,
    'dst_host_diff_srv_rate': 0.03,
    'dst_host_same_src_port_rate': 0.0,
    'dst_host_srv_diff_host_rate': 0.0,
    'dst_host_serror_rate': 0.0,
    'dst_host_srv_serror_rate': 0.0,
    'dst_host_rerror_rate': 0.0,
    'dst_host_srv_rerror_rate': 0.0,
}

# Predict
df = pd.DataFrame([sample_data])
predicted = model.predict(df)[0]

# Show attack type
print("Predicted Attack Type:", attack_labels.get(predicted, "Unknown"))
