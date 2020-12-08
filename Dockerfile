FROM python:3.6

WORKDIR /home/flasks
COPY . .


# 安装依赖
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/


CMD ["gunicorn", "main:app", "-c", "gunicorn.py"]