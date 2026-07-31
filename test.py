import torch

# 1. GPU 사용 가능 여부 출력
print("CUDA Available:", torch.cuda.is_available())

# 2. 장치 개수 및 이름 출력 (사용 가능한 경우)
if torch.cuda.is_available():
    print("GPU Count:", torch.cuda.device_count())
    print("GPU Name:", torch.cuda.get_device_name(0))

# 3. 디바이스 자동 설정 (GPU가 있으면 cuda, 없으면 cpu)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Using device:", device)