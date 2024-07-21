FROM --platform=amd64 ubuntu:latest
RUN apt update
# Install process for node
RUN apt install -y curl
RUN curl -fsSL https://deb.nodesource.com/setup_22.x -o nodesource_setup.sh
RUN bash nodesource_setup.sh
RUN apt install -y nodejs
RUN node --version

# install process for python
RUN apt install -y python3-full python3-pip
ENV PYTHONPATH="src"

WORKDIR /app
COPY frontend /app/frontend
COPY backend /app/backend
COPY start.sh /app/start.sh
COPY install.sh /app/install.sh

RUN /app/install.sh

ENTRYPOINT [ "bash","/app/start.sh" ]