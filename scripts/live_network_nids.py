# live_network_nids.py

from scapy.all import sniff, TCP, UDP, ICMP
import joblib
import numpy as np

# Load trained NIDS model
model = joblib.load("../models/nids_model.pkl")


# Dummy encoder mappings (update as per your preprocessing)
protocol_map = {'tcp': 0, 'udp': 1, 'icmp': 2, 'other': 3}

# Packet processing function
def process_packet(packet):
    try:
        # Extract protocol type
        if TCP in packet:
            protocol_type = 'tcp'
        elif UDP in packet:
            protocol_type = 'udp'
        elif ICMP in packet:
            protocol_type = 'icmp'
        else:
            protocol_type = 'other'

        protocol_encoded = protocol_map.get(protocol_type, 3)

        # Example dummy feature vector (replace these with real features)
        # [duration, protocol_type, service, flag, src_bytes, dst_bytes, land, wrong_fragment, urgent, hot, ...]
        features = [
            0,                              # duration (dummy)
            protocol_encoded,               # protocol_type
            0,                              # service (dummy)
            0,                              # flag (dummy)
            len(packet.payload),            # src_bytes
            0,                              # dst_bytes (dummy)
            0, 0, 0, 0,                     # land, wrong_fragment, urgent, hot (dummy)
            # Fill remaining fields with 0 or estimates
        ]
        features += [0] * (41 - len(features))  # Fill up to 41 features (NSL-KDD has 41)

        # Predict using the model
        sample = np.array([features])
        prediction = model.predict(sample)

        print(f"[+] Packet Detected - Protocol: {protocol_type.upper()}, Predicted Attack Type: {prediction[0]}")

    except Exception as e:
        print(f"[!] Error processing packet: {e}")


if __name__ == "__main__":
    print("\n🔍 Starting Live Network Intrusion Detection... Press Ctrl+C to stop.\n")

    sniff(prn=process_packet, store=False)
