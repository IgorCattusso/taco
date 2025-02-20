FROM python:3.10 AS base_structure

WORKDIR /app

COPY . .

RUN apt-get update && \
    apt-get install -y tzdata && \
    apt-get install -y wget && \
    apt-get install -y default-mysql-client && \
    apt-get clean

# Set brazilian timezone
ENV TZ=America/Sao_Paulo

# RUN ln to set timezone in /etc/timezone
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN pip install --upgrade pip &&  \
    pip install -r requirements.txt

# Run taco.py
FROM base_structure AS taco_svc
CMD ["python", "-m", "src.taco"]
