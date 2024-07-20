# استفاده از تصویر پایه Python
FROM python:3.9

# تنظیم دایرکتوری کاری
WORKDIR /app

# کپی فایل‌های پروژه به دایرکتوری کاری
COPY . .

# نصب وابستگی‌ها
RUN pip install --no-cache-dir -r requirements.txt

# اجرای مهاجرت‌های پایگاه داده
RUN python manage.py migrate

# جمع‌آوری فایل‌های استاتیک
RUN python manage.py collectstatic --noinput

# تنظیم فرمان پیش‌فرض
CMD ["gunicorn", "config.wsgi", "--bind", "0.0.0.0:8000"]
