# استفاده از تصویر پایه پایتون
FROM python:3.8

# تنظیم دایرکتوری کاری
WORKDIR /app

# کپی کردن وابستگی‌ها
COPY requirements.txt .

# نصب وابستگی‌ها
RUN pip install -r requirements.txt

# کپی کردن کد اپلیکیشن
COPY . .

# اجرای اپلیکیشن
CMD ["gunicorn", "config.wsgi", "--bind", "0.0.0.0:8080"]
