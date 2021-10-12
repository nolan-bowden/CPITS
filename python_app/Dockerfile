FROM python
COPY ./python_app/app.py .
COPY ./python_app/requirements.txt .
RUN pip3 install -r requirements.txt
CMD ["python3","app.py"]
