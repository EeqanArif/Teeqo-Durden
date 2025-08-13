import socket, cv2
UDP_IP = "192.168.X.X"; UDP_PORT = 1234
MAX_DGRAM = 1400
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cap = cv2.VideoCapture(0)
frame_id = 0

while True:
    ret, frame = cap.read()
    if not ret: break
    ret2, jpeg = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 70])
    data = jpeg.tobytes()
    chunks = [data[i:i+MAX_DGRAM] for i in range(0, len(data), MAX_DGRAM)]
    for i, chunk in enumerate(chunks):
        header = frame_id.to_bytes(2, 'big') + i.to_bytes(1, 'big') + len(chunks).to_bytes(1, 'big')
        sock.sendto(header + chunk, (UDP_IP, UDP_PORT))
    frame_id = (frame_id + 1) % 65536
