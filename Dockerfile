# Використовуємо офіційний Python образ
FROM python:3.8

# Встановлення Python-залежностей
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Завантаження SpaCy моделі
RUN python -m spacy download en_core_web_sm

# Завантаження всіх необхідних NLTK ресурсів
RUN python -m nltk.downloader all

# Копіюємо всі скрипти в контейнер
COPY . /app

# Встановлюємо робочу директорію
WORKDIR /app

# Команда для запуску скрипту
CMD ["python", "news_analysis.py"]

