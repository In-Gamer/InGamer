FROM python:3.10-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
      gcc \
      default-libmysqlclient-dev \
      pkg-config \
    && rm -rf /var/lib/apt/lists\*

RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    gnupg \
    ca-certificates \
    chromium \
    chromium-driver

# Selenium 실행 시 chromium 경로를 지정
ENV CHROME_BIN=/usr/bin/chromium

# RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
# RUN dpkg -i google-chrome-stable_current_amd64.deb || true

# RUN apt-get install -y -f
# RUN LATEST=$(curl -sS http://chromedriver.storage.googleapis.com/LATEST_RELEASE) && \
#     wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/${LATEST}/chromedriver_linux64.zip && \
#     unzip /tmp/chromedriver.zip -d /usr/local/bin/ && \
#     chmod +x /usr/local/bin/chromedriver
# RUN mkdir chrome
# RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/src/chrome

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8080

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]