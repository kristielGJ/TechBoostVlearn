FROM mcr.microsoft.com/devcontainers/base:ubuntu

RUN apt-get update && \
    apt-get install -y xz-utils

# install python 3.11 and pip and run pip install Flask flask-cors pdfminer.six chardet PyMuPDF
RUN curl -sL https://www.python.org/ftp/python/3.11.0/Python-3.11.0.tar.xz | tar -xJ && \
    cd Python-3.11.0 && \
    ./configure && \
    make -j 4 && \
    make install && \
    cd .. && \
    rm -rf Python-3.11.0 && \
    python3.11 -m pip install --upgrade pip && \
    python3.11 -m pip install Flask flask-cors pdfminer.six chardet PyMuPDF

# install nodejs, run npm install and npm start from Frontend/v-learn
RUN apt-get install -y nodejs npm && \
    cd Frontend/v-learn && \
    npm install && \
    npm start
