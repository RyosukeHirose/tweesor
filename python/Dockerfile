FROM python:3.7

# 作業ディレクトリを設定  
WORKDIR /code/
ADD requirements.txt /code 

RUN apt-get update \
&& pip install --upgrade pip \
&& pip install django-environ \
&& pip install -r requirements.txt \
# mecab
&& apt-get -y install mecab \
&& apt-get -y install libmecab-dev \
&& apt-get -y install mecab-ipadic-utf8 \
# && pip3 install mecab-python3 \
&& pip install mecab-python3==0.996.5 \
&& pip install cython \
&& pip install fasttext \
&& pip3 install twitter \
&& pip install requests-oauthlib

# mecabがないなら
# pip install mecab-python3==0.996.5
# これは多分しらんけど一応
# pip install unidic-lite

# ディレクトリでgit clone https://github.com/facebookresearch/fastText.gitを実行しておく
# make
# python manage.py runserver 0:9000