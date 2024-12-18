# OpenTelemetry AI Monitor

Production-grade monitoring solution for AI applications using OpenTelemetry. Track performance, costs, and behavior patterns of your AI applications in real-time.

## Quick Setup Guide

### 1. Clone and Setup
```bash
# Clone the repository
git clone https://github.com/mehmetdede1907/opentelemetry-ai-monitor.git
cd opentelemetry-ai-monitor

# Create virtual environment
python -m venv venv

# Activate environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Environment
```bash
# Copy example environment file
cp .env.example .env

# Edit .env file with your settings
# Required: Add your OpenAI API key
# Optional: Modify other settings if needed
```

### 3. Start Monitoring Services
```bash
# Start Jaeger and Aspire Dashboard
docker-compose up -d

# Verify services are running
docker ps
```

### 4. Run the Application
```bash
# Run with default settings
python main.py

# Run with specific model
python main.py --model gpt-4

# Run with custom temperature
python main.py --temperature 0.8
```

## Testing Guide

### 1. Manual Testing

Test the basic functionality:
```bash
# Create telemetry directory
mkdir telemetry_data

# Run sample prompts
python main.py --test

# Check telemetry files
ls telemetry_data/
```

Expected output:
```
Processing prompt: Explain what is OpenTelemetry in one sentence.
Response: [AI response will appear here]
Telemetry saved to: telemetry_data/telemetry_20241218_*.json
Tokens used: XXX
Latency: XXX.XX ms
```

### 2. Testing Different Models
```bash
# Test with GPT-3.5 Turbo
python main.py --model gpt-3.5-turbo

# Test with GPT-4 (if available)
python main.py --model gpt-4
```

### 3. Monitoring Tests

#### Check Jaeger UI:
1. Open http://localhost:16686
2. Select service: "genai-demo-service"
3. Click "Find Traces"
4. Verify:
   - Traces appear for each request
   - Spans show token usage
   - Latency information is present

#### Check Aspire Dashboard:
1. Open http://localhost:18888
2. Navigate to "Telemetry"
3. Verify:
   - Service metrics are visible
   - Request counts are updating
   - Error rates are tracked

### 4. Telemetry Data Validation

Check generated JSON files:
```bash
# View latest telemetry file
ls -t telemetry_data/ | head -1 | xargs cat
```

Expected format:
```json
{
  "prompt": "Your test prompt",
  "tokens": {
    "total": 150,
    "completion": 100,
    "prompt": 50
  },
  "latency_ms": 1234.56,
  "content": "AI response content"
}
```

## Troubleshooting Guide

### Common Issues

1. OpenAI API Error
```bash
# Check API key is set
echo $OPENAI_API_KEY

# Verify .env file
cat .env
```

2. Monitoring Services Not Running
```bash
# Check Docker containers
docker ps

# Restart services
docker-compose down
docker-compose up -d
```

3. No Telemetry Data
```bash
# Check directory exists
ls telemetry_data/

# Check permissions
chmod 755 telemetry_data/

# Verify OTEL endpoint
curl http://localhost:4318
```

### Log Files

Monitor application logs:
```bash
# View application logs
tail -f app.log

# View Docker logs
docker-compose logs -f
```

## Performance Testing

### 1. Basic Load Test
```bash
# Run multiple requests
for i in {1..5}; do
    python main.py --prompt "Test prompt $i"
    sleep 2
done
```

### 2. Parallel Testing
```python
# Create test_parallel.py
import asyncio
from src.ai_client import AIClient

async def test_parallel(prompts):
    client = AIClient()
    tasks = [client.generate_response(prompt) for prompt in prompts]
    return await asyncio.gather(*tasks)

# Run parallel tests
python test_parallel.py
```

### 3. Monitor Resource Usage
```bash
# Monitor CPU/Memory
top -pid $(pgrep -f "python main.py")

# Monitor network
netstat -an | grep 4318
```

## Maintenance

### Regular Tasks

1. Update dependencies:
```bash
pip freeze > requirements.txt.old
pip install --upgrade -r requirements.txt
pip freeze > requirements.txt
```

2. Clean up telemetry data:
```bash
# Remove old telemetry files
find telemetry_data/ -mtime +7 -delete
```

3. Backup configuration:
```bash
# Backup .env and telemetry data
tar -czf backup.tar.gz .env telemetry_data/
```

### Health Checks

Monitor system health:
```bash
# Check API health
curl http://localhost:4318/health

# Check disk space
df -h telemetry_data/

# Check service status
docker-compose ps
```

Would you like me to help you set up and test any specific part of the monitoring system?