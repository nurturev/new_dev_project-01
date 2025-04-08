FROM public.ecr.aws/lambda/python:3.9

# Set working directory
WORKDIR /var/task

# Install Python dependencies
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy source code
COPY . .

# Command to run the Lambda function
CMD ["lambda_handler.lambda_handler"]
