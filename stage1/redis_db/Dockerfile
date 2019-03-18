FROM redis

COPY redis.conf /usr/local/etc/redis/redis.conf

EXPOSE 6379

VOLUME /data

CMD [ "redis-server", "/usr/local/etc/redis/redis.conf" ]
#CMD ["redis-server"]

# Build the image
# sudo docker build -t redis
# Run the container
# sudo docker run -d -p 6379:6379 --name redisdb -v /var/cec:/data redis:latest