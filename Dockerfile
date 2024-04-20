FROM continuumio/miniconda3

# Switch shell from sh to bash, make working dir and copy over files
SHELL [ "/bin/bash", "--login", "-c"]
# Expose API port
EXPOSE 8000
# Copy over app files
WORKDIR /usr/src/app
COPY . .

# Make conda env and run server
RUN conda init bash
RUN . ~/.bashrc
RUN conda env create --name fastapi --file environment.yml
RUN conda activate fastapi && python main.py