## 가상환경 설정
```python
cd E:\gRPCSample\python
python -m venv venv
```

## gRPC 패키지 설치
```python
python -m pip install --upgrade pip
pip3 install grpcio
pip3 install grpcio-tools
```

## proto 빌드
```python
cd E:\gRPCSample\python\proto
python -m grpc_tools.protoc --python_out=. --grpc_python_out=. --proto_path=. ./bee4.proto
```