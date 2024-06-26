FROM python:3.7.17

## Step 1:
# Create a working directory
WORKDIR /app

## Step 2:
# Copy source code to working directory
COPY main.py requirements.txt /app/
COPY model_data /app/model_data/
COPY utils /app/utils/
COPY static /app/static/

# Run app.py at container launch

## Step 3:
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir --upgrade wheel && \
    pip install --no-cache-dir --upgrade setuptools && \
    pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

## Step 4:
EXPOSE 8765

## Step 5:
CMD ["streamlit" , "run", "main.py", "--server.port", "8765"]
