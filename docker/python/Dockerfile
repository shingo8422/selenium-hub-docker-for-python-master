FROM python:3.8

RUN apt-get -y update \
&& apt-get install -y \
wget \
unzip \
libnss3 \
cron

# google chrome インストール
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# chromedriver インストール
RUN wget https://chromedriver.storage.googleapis.com/87.0.4280.88/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip
RUN mv chromedriver /usr/local/bin
RUN chmod 755 /usr/local/bin/chromedriver
RUN rm chromedriver_linux64.zip

# pip update
RUN python -m pip install --upgrade pip
ADD requirements.txt .
RUN pip install -r requirements.txt