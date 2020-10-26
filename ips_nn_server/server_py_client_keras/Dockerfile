FROM gw000/keras:2.1.4-py3
COPY ./ /app/	
WORKDIR /app
#RUN apt-get update && apt-get install -y python-pip
RUN pip3 install -r requirements.txt
#ENTRYPOINT ["/app/get_nn_result.py"]
CMD ["python3", "get_nn_result.py"]
