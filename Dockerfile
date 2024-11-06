FROM python:3.11.4-slim-buster

WORKDIR /app

COPY Scripts Scripts
RUN chmod +x Scripts/*.sh

# CMD ["bash", "Scripts/entrypoint-simple.sh"]
CMD ["tail", "-f", "/dev/null"]