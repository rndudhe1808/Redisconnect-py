#vi elasticache_redis.py 
from decouple import config
from redis.cluster import RedisCluster, ClusterNode

redis_host = config('REDIS_HOST')
redis_port = config('REDIS_PORT')
nodes = [ClusterNode(redis_host, redis_port)]
redis = RedisCluster(
            startup_nodes=nodes,
            decode_responses=True,
            skip_full_coverage_check=True,
            ssl=True # Given we enabled Encryption in Transit
        )

# Once the connection has been established we use Redis APIs as Open Source Redis
if __name__ == "__main__":
    redis.set('key', 'ElastiCache for Redis')
    print(redis.get('key'))
  
#connection check  
python elasticache_redis.py
#output will be 
ElastiCache for Redis
