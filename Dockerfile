FROM python:3.9.19-bookworm

# Expose API port
EXPOSE 8000
EXPOSE 80
# Copy over app files
WORKDIR /usr/src/app
COPY . .

# Install all packages
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]