# 1. Official Microsoft Playwright image
FROM mcr.microsoft.com/playwright/python:v1.58.0-noble


# 2. System settings for Python stability
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Set the working directory
WORKDIR /app

# 4. EXCELLENT: Install OS-level dependencies for PostgreSQL
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 5. Copy and install Python requirements
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 6. Install Chromium and its Linux system dependencies
RUN playwright install chromium --with-deps

# 7. Copy your project files
COPY . .

# 8. Run tests
CMD ["pytest", "--browser", "chromium"]
