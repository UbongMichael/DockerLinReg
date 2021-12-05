# from Ubuntu 20.04 base image
FROM ubuntu:20.04
# provide your contact info if you wish
MAINTAINER Ubong Michael
#run these commands
RUN apt-get update
RUN apt install -y python3-pip
RUN pip3 install pandas scikit_learn
# Copy this Python script from host machine to docker image
ADD linear-regression.py /
# As soon as a container starts, run this script using Python3
ENTRYPOINT ["python3","/linear-regression.py"]

