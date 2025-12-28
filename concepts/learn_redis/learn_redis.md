## services:
  redis:
    image: redis:7-alpine
```

**Visual Breakdown:**
```
IMAGE SELECTION
┌─────────────────────────────────┐
│ redis:7-alpine                  │
│   │    │   │                    │
│   │    │   └─ Alpine Linux base │
│   │    │      (lightweight)     │
│   │    └───── Major version 7   │
│   └────────── Official Redis    │
│                                 │
│ Size: ~40MB vs ~150MB (debian)  │
└─────────────────────────────────┘

## ports:
      - "6379:6379"

**Port Mapping:**

YOUR MACHINE          DOCKER CONTAINER
┌─────────────┐      ┌──────────────┐
│             │      │              │
│ localhost:  │      │   Redis      │
│   6379   ───┼──────┼──> :6379     │
│             │      │              │
└─────────────┘      └──────────────┘
     ↑                      ↑
   Host port            Container port

Format: "host:container"
6379: Default Redis port
Why expose: Allows Python clients, tools to connect from your machine

## volumes:
      - redis_data:/data
      - ./redis.conf:/usr/local/etc/redis/redis.conf
```

**Volume Mental Model:**
```
CONTAINER LIFECYCLE
Without Volumes:
┌──────────────────────────┐
│ Container Dies           │
│    ↓                     │
│ Data Lost Forever ❌     │
└──────────────────────────┘

With Volumes:
┌──────────────────────────┐
│ Container Dies           │
│    ↓                     │
│ Data Persists ✓         │
│    ↓                     │
│ New Container Starts     │
│    ↓                     │
│ Data Still There ✓      │
└──────────────────────────┘
```

**Two Volume Types Here:**

1. **Named Volume** (`redis_data:/data`)
```
   redis_data          →     /data (inside container)
      ↑                           ↑
   Docker manages          Redis saves data here
   (survives restarts)
```

2. **Bind Mount** (`./redis.conf:...`)
```
   Your local file     →     Container path
   (live sync - changes reflect immediately)
   
## command: redis-server /usr/local/etc/redis/redis.conf
```

**Command Override:**
```
DEFAULT:
┌────────────────────────┐
│ redis-server           │  ← Default, no config
└────────────────────────┘

CUSTOM:
┌────────────────────────┐
│ redis-server           │
│   └── /path/to/config  │  ← Use our settings
└────────────────────────┘
What: Starts Redis with custom configuration
Why: Override defaults (memory limits, persistence, etc.)

## restart: unless-stopped
```

**Restart Policy Decision Tree:**
```
Container crashes?
│
├─── "no" → Don't restart (default)
├─── "always" → Always restart (even after reboot)
├─── "on-failure" → Only restart if error exit code
└─── "unless-stopped" → Restart unless manually stopped ✓

Why unless-stopped?

Survives Docker daemon restarts
Won't restart if you manually stop it
Production-safe behavior

networks:
      - redis-network
```

**Network Isolation:**
```
DEFAULT BRIDGE          CUSTOM NETWORK
┌───────────────┐        ┌──────────────┐
│ All containers│        │ Only redis & │
│ can talk      │        │ redis-insight│
│               │        │ can talk     │
│ Less secure   │        │              │
└───────────────┘        └──────────────┘
Why custom network: Container isolation + DNS resolution by name

healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 3s
      retries: 3
```

**Healthcheck Flow:**
```
EVERY 10 SECONDS
┌────────────────────────────┐
│ Docker runs: redis-cli ping│
│              ↓             │
│         Returns PONG?      │
│         ↙         ↘        │
│      YES           NO       │
│       ↓            ↓        │
│   Healthy      Unhealthy   │
│                    ↓        │
│            (after 3 retries)│
└────────────────────────────┘

Parameters:

interval: 10s → Check every 10 seconds
timeout: 3s → Wait max 3s for response
retries: 3 → Mark unhealthy after 3 failures

Check health:
bashdocker ps
# Look for: "healthy" in STATUS column

3. Redis Insight (Optional GUI)
yaml  redis-insight:
    image: redislabs/redisinsight:latest
    ports:
      - "8001:8001"
```

**What is Redis Insight?**
```
REDIS-CLI (Terminal)        REDIS INSIGHT (GUI)
┌─────────────────┐         ┌──────────────────┐
│ GET user:1000   │         │  ┌──────────────┐│
│ > "Garima"      │         │  │ Key: user:1000│
│                 │         │  │ Type: String  │
│ Manual typing   │         │  │ Value: Garima │
└─────────────────┘         │  │ TTL: -1       │
                            │  └──────────────┘│
                            │  [Visual charts] │
                            └──────────────────┘
Access: http://localhost:8001 (after starting containers)

yaml    depends_on:
      - redis
```

**Startup Order:**
```
WITHOUT depends_on:
┌─────────────────────────┐
│ Redis Insight starts    │
│        ↓                │
│ Tries to connect        │
│        ↓                │
│ Redis not ready! ❌     │
└─────────────────────────┘

WITH depends_on:
┌─────────────────────────┐
│ Redis starts first      │
│        ↓                │
│ Redis ready ✓           │
│        ↓                │
│ Redis Insight starts    │
│        ↓                │
│ Connection works ✓      │
└─────────────────────────┘

4. Volumes Declaration
yamlvolumes:
  redis_data:
    driver: local
  redisinsight_data:
    driver: local
Where is data stored?
bash# Docker stores named volumes here:
# Linux: /var/lib/docker/volumes/
# Mac: ~/Library/Containers/com.docker.docker/Data/
# Windows: \\wsl$\docker-desktop-data\data\docker\volumes\

# List volumes:
docker volume ls

# Inspect volume location:
docker volume inspect redis_data

5. Networks Declaration
yamlnetworks:
  redis-network:
    driver: bridge
```

**Bridge Network:**
```
HOST MACHINE
┌────────────────────────────────┐
│  redis-network (bridge)        │
│  ┌──────────┐   ┌────────────┐ │
│  │  redis   │   │redis-insight│ │
│  │ (6379)   │←──│  (8001)    │ │
│  └──────────┘   └────────────┘ │
│       ↑                         │
│       └─────── Can talk via DNS │
└────────────────────────────────┘

🔧 Custom Redis Configuration File
Create redis.conf in same directory:
conf# Persistence
appendonly yes
appendfsync everysec

# Memory management
maxmemory 256mb
maxmemory-policy allkeys-lru

# Security (disable for local learning)
# requirepass yourpassword

# Logging
loglevel notice

# Performance
save 900 1
save 300 10
save 60 10000
```

### Configuration Explained
```
PERSISTENCE STRATEGY
┌────────────────────────────────┐
│ appendonly yes                 │
│   ↓                            │
│ Every write → Append to file   │
│   ↓                            │
│ Crash recovery: Replay log     │
│                                │
│ appendfsync everysec           │
│   ↓                            │
│ Sync to disk every 1 second    │
│   (balance: performance vs safety)
└────────────────────────────────┘

MEMORY EVICTION
┌────────────────────────────────┐
│ maxmemory 256mb                │
│   ↓                            │
│ When limit reached...          │
│   ↓                            │
│ maxmemory-policy allkeys-lru   │
│   ↓                            │
│ Evict least recently used keys │
└────────────────────────────────┘

SNAPSHOTS (RDB)
┌────────────────────────────────┐
│ save 900 1                     │
│   └─ After 900s, if 1+ change  │
│                                │
│ save 300 10                    │
│   └─ After 300s, if 10+ changes│
│                                │
│ save 60 10000                  │
│   └─ After 60s, if 10k+ changes│
└────────────────────────────────┘

🚀 Usage Commands
Start Everything
bash# From directory with docker-compose.yml
docker-compose up -d

# Verify running
docker-compose ps
Access Redis CLI
bash# Method 1: Via docker-compose
docker-compose exec redis redis-cli

# Method 2: Via container name
docker exec -it redis-learning redis-cli

# Inside CLI:
127.0.0.1:6379> PING
PONG
View Logs
bash# All logs
docker-compose logs -f

# Only Redis logs
docker-compose logs -f redis

# Last 50 lines
docker-compose logs --tail=50 redis
Stop Services
bash# Stop (keeps data)
docker-compose stop

# Stop and remove containers (data persists in volumes)
docker-compose down

# Stop and DELETE all data
docker-compose down -v
Monitor Performance
bash# Inside redis-cli:
INFO stats
INFO memory
MONITOR  # Real-time command monitoring
```

---

## 🔍 Under the Hood: Docker Compose Architecture
```
DOCKER COMPOSE ORCHESTRATION
┌─────────────────────────────────────┐
│ docker-compose.yml                  │
│         ↓                           │
│   Docker Engine                     │
│         ↓                           │
│   ┌─────────────────────┐          │
│   │ Creates Network     │          │
│   │ Creates Volumes     │          │
│   │ Pulls Images        │          │
│   │ Starts Containers   │          │
│   │ Configures Health   │          │
│   └─────────────────────┘          │
│         ↓                           │
│   Running Services                  │
└─────────────────────────────────────┘

CONTAINER INTERNALS
┌─────────────────────────────────────┐
│ redis container                     │
│  ├── Alpine Linux (minimal OS)     │
│  ├── Redis Server Process          │
│  ├── /data (volume mount)          │
│  └── /usr/local/etc/redis/redis.conf│
│                                     │
│ Memory Layout:                      │
│  ├── Redis process: ~10-50MB       │
│  ├── Your data: up to maxmemory    │
│  └── OS overhead: ~5MB              │
└─────────────────────────────────────┘

✅ Verification Checklist
Run these after docker-compose up -d:
bash# 1. Containers running?
docker-compose ps
# Expected: STATE = Up (healthy)

# 2. Redis responding?
docker-compose exec redis redis-cli PING
# Expected: PONG

# 3. Persistence working?
docker-compose exec redis redis-cli SET test "hello"
docker-compose restart redis
docker-compose exec redis redis-cli GET test
# Expected: "hello" (survived restart!)

# 4. Redis Insight accessible?
# Open browser: http://localhost:8001
# Add database: localhost:6379

📊 Minimal vs Full Comparison
Minimal (for quick testing)
yamlversion: '3.8'
services:
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
Full (for learning/production)
yaml# The complete version above with:
# ✓ Data persistence
# ✓ Custom config
# ✓ Health checks
# ✓ GUI tool
# ✓ Network isolation
Recommendation: Start with minimal, add features as you learn
