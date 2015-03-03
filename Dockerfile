#Dockerfile for Pytcker
#
#Includes:
# - Ubuntu
# - Python 2.7
# - Flask
# - Simple WebApp

FROM  ubuntu:14.04
MAINTAINER abodalevsky@hotmail.com

# install python, pip, Flask, and pymongo
RUN apt-get update && apt-get install -y python2.7 python-pip git
RUN pip install Flask

EXPOSE 5000

CMD ["python", "webapp.py"]
