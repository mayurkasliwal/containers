FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 12345
ENTRYPOINT [ "python" ]
CMD [ "helloworld.py" ]