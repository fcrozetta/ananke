FROM --platform=amd64 ubuntu:latest

# Install essentials
RUN apt update
RUN apt install -y curl

# Install azure cli
RUN curl -sL https://aka.ms/InstallAzureCLIDeb -o azcli.sh
RUN bash azcli.sh
RUN rm azcli.sh
RUN az config set extension.use_dynamic_install=yes_without_prompt

# Install process for node
RUN curl -fsSL https://deb.nodesource.com/setup_22.x -o nodesource_setup.sh
RUN bash nodesource_setup.sh
RUN apt install -y nodejs
RUN node --version
RUN rm nodesource_setup.sh

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