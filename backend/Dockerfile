# 使用 Python 3.9 作為基礎環境
FROM python:3.9

# 設定工作目錄
WORKDIR /app

# 複製需求套件並安裝
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 複製 Python 代碼
COPY backend/ .

# 開放 FastAPI 端口
ENV PORT=8080
EXPOSE 8080

# 啟動 FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
