FROM python

ADD . .
# Install required dependencies
RUN pip install requests

ENTRYPOINT ["python" , "code.py"]