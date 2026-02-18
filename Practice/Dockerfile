FROM python

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt

CMD ["python", "app.py"]

EXPOSE 5000
VOLUME ["/app/data"]
ENV FLASK_ENV=development
ENV FLASK_APP=app.py                    

ENV PYTHONUNBUFFERED=1  
ENV PYTHONIOENCODING=utf-8      
ENV PYTHONPATH=/app
