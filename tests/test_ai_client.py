import pytest
from src.ai_client import AIClient
from src.data_collector import DataCollector
import os
import json

@pytest.fixture
def ai_client():
    return AIClient()

@pytest.fixture
def data_collector():
    # Use a test directory
    test_dir = "test_telemetry_data"
    collector = DataCollector(output_dir=test_dir)
    yield collector
    
    # Cleanup after tests
    for file in os.listdir(test_dir):
        os.remove(os.path.join(test_dir, file))
    os.rmdir(test_dir)

def test_generate_response(ai_client):
    prompt = "Test prompt for OpenTelemetry"
    result = ai_client.generate_response(prompt)
    
    # Verify response structure
    assert "tokens" in result
    assert "latency_ms" in result
    assert "content" in result
    
    # Verify token counts
    assert result["tokens"]["total"] > 0
    assert result["tokens"]["completion"] > 0
    assert result["tokens"]["prompt"] > 0
    
    # Verify latency
    assert result["latency_ms"] > 0
    
    # Verify content
    assert isinstance(result["content"], str)
    assert len(result["content"]) > 0

def test_save_telemetry(ai_client, data_collector):
    # Generate response
    prompt = "Test prompt for telemetry"
    result = ai_client.generate_response(prompt)
    
    # Save telemetry
    filename = data_collector.save_telemetry({
        "prompt": prompt,
        **result
    })
    
    # Verify file exists
    assert os.path.exists(filename)
    
    # Read and verify content
    with open(filename, 'r') as f:
        data = json.load(f)
        assert data["prompt"] == prompt
        assert "tokens" in data
        assert "latency_ms" in data
        assert "content" in data

def test_error_handling(ai_client):
    with pytest.raises(Exception):
        # Test with invalid model
        AIClient(model="invalid-model").generate_response("Test prompt")