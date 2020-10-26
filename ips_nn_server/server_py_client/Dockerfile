FROM python:3.7
COPY ./ /app/	
WORKDIR /app
RUN pip install -r requirements.txt
#ENTRYPOINT ["/app/get_nn_result.py"]
CMD ["python3", "get_nn_result.py"]
