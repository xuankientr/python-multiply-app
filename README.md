# Python Multiply App

Ứng dụng Python đơn giản với hàm multiply và CI/CD pipeline hoàn chỉnh.

## Tính năng

- ✅ Hàm `multiply(a, b)` để nhân hai số
- ✅ Unit tests với pytest
- ✅ GitHub Actions CI/CD pipeline
- ✅ Docker containerization
- ✅ Tự động test trên nhiều phiên bản Python (3.8, 3.9, 3.10, 3.11)

## Cấu trúc dự án

```
.
├── app.py                    # Ứng dụng chính với hàm multiply
├── test_app.py              # Unit tests
├── requirements.txt         # Python dependencies
├── Dockerfile              # Docker configuration
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions workflow
└── README.md               # Tài liệu này
```

## Cách sử dụng

### Chạy trực tiếp với Python

```bash
# Cài đặt dependencies
pip install -r requirements.txt

# Chạy ứng dụng
python app.py

# Chạy tests
python -m unittest test_app.py -v
# hoặc với pytest
python -m pytest test_app.py -v
```

### Chạy với Docker

```bash
# Build Docker image
docker build -t python-multiply-app .

# Chạy container
docker run --rm python-multiply-app
```

## Kết quả mong đợi

Khi chạy ứng dụng, bạn sẽ thấy output:

```
multiply(3, 4) = 12
multiply(5, 6) = 30
multiply(2.5, 4) = 10.0
multiply(-3, 7) = -21
```

## Tests

Unit tests bao gồm:
- ✅ Test với số nguyên dương: `multiply(3, 4) == 12`
- ✅ Test với số 0
- ✅ Test với số âm
- ✅ Test với số thập phân
- ✅ Test với số lớn

## CI/CD Pipeline

GitHub Actions tự động:
1. Chạy tests trên Python 3.8, 3.9, 3.10, 3.11
2. Build Docker image
3. Chạy container để verify

## Yêu cầu hệ thống

- Python 3.8+
- Docker (tùy chọn)
- pytest (cho testing)

