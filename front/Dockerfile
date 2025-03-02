# 使用 Nginx 作為 Web 伺服器
FROM nginx:alpine

# 複製 HTML/CSS/JS 到 Nginx 目錄
COPY . /usr/share/nginx/html

# 開放 80 端口
EXPOSE 80

# 啟動 Nginx
CMD ["nginx", "-g", "daemon off;"]

