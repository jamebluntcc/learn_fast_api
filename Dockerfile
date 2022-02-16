FROM python:3.6.12
ENV wd=/home/application
ADD ./ ${wd}
WORKDIR ${wd}
RUN pip install --no-cache-dir --upgrade -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]