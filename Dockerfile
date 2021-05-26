FROM python:3.8-slim-buster
COPY app.py /app/app.py
COPY start_app.sh /app/start_app.sh
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
RUN chmod +x /app/start_app.sh
WORKDIR /app
EXPOSE 8501
ENTRYPOINT ["/bin/bash"]
CMD ["./start_app.sh"]