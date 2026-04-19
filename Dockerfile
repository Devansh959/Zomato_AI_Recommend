FROM python:3.9-slim

# Set up a non-root user
RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

WORKDIR $HOME/app

# Copy requirements and install
COPY --chown=user requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy all application files
COPY --chown=user . .

# Make the start script executable
RUN chmod +x start.sh

# Expose the port used by Hugging Face Spaces
EXPOSE 7860

# Run the startup script
CMD ["./start.sh"]
