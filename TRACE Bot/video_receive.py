import socket
import cv2
import numpy as np

UDP_IP = "0.0.0.0"
UDP_PORT = 1234
MAX_DGRAM = 1400

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

buffer = {}
frame_expected_chunks = {}

while True:
    packet, addr = sock.recvfrom(65535)

    frame_id = int.from_bytes(packet[0:2], 'big')
    chunk_i = packet[2]
    total_chunks = packet[3]
    chunk_data = packet[4:]

    if frame_id not in buffer:
        buffer[frame_id] = [None] * total_chunks
        frame_expected_chunks[frame_id] = total_chunks

    buffer[frame_id][chunk_i] = chunk_data

    # Check if all chunks received
    if None not in buffer[frame_id]:
        # Reassemble full jpeg data
        full_data = b''.join(buffer[frame_id])
        img = cv2.imdecode(np.frombuffer(full_data, dtype=np.uint8), cv2.IMREAD_COLOR)
        if img is not None:
            cv2.imshow('UDP Video', img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        # Remove buffer for that frame_id
        del buffer[frame_id]
        del frame_expected_chunks[frame_id]

cv2.destroyAllWindows()
sock.close()
