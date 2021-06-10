FROM postgres:latest
ENV POSTGRES_PASSWORD=secret
ENV POSTGRES_USER=username
ENV POSTGRES_DB=database
COPY results.sql /docker-entrypoint-initdb.d/results.sql