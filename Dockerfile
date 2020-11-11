FROM python
ADD . .
RUN pip install requests
ENTRYPOINT ["python" , "code.py"]