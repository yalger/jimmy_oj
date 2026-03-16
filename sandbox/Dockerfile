FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    python3 \
    g++ \
    openjdk-17-jdk \
    golang \
    coreutils \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y \
    time \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY runner.py .

CMD ["python3", "runner.py"]