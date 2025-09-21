#!/usr/bin/env python3
"""
Test script to make outbound calls using the speech assistant API.
"""

import requests
import json
import subprocess

def get_ngrok_url():
    """Automatically detect ngrok URL"""
    try:
        result = subprocess.run(['curl', '-s', 'http://localhost:4040/api/tunnels'], 
                              capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            data = json.loads(result.stdout)
            for tunnel in data.get('tunnels', []):
                if tunnel.get('proto') == 'https':
                    return tunnel.get('public_url')
    except:
        pass
    return "https://03f2b7cfd36f.ngrok-free.app"  # fallback URL

# Configuration
BASE_URL = get_ngrok_url()

def test_make_call():
    """Test making an outbound call."""
    print("Making outbound call...")
    
    try:
        response = requests.post(f"{BASE_URL}/make-call")
        result = response.json()
        
        if "error" in result:
            print(f"❌ Error: {result['error']}")
        else:
            print(f"✅ {result['message']}")
            if "Call SID" in result['message']:
                call_sid = result['message'].split("Call SID: ")[1]
                print(f"Call SID: {call_sid}")
                return call_sid
    except Exception as e:
        print(f"❌ Request failed: {e}")
    
    return None

def test_call_status(call_sid):
    """Test getting call status."""
    if not call_sid:
        print("No call SID available to check status")
        return
    
    print(f"\nChecking status for call {call_sid}...")
    
    try:
        response = requests.get(f"{BASE_URL}/call-status/{call_sid}")
        result = response.json()
        
        if "error" in result:
            print(f"❌ Error: {result['error']}")
        else:
            print(f"✅ Call Status:")
            print(f"   SID: {result['call_sid']}")
            print(f"   Status: {result['status']}")
            print(f"   From: {result['from']}")
            print(f"   To: {result['to']}")
            print(f"   Duration: {result['duration']} seconds")
    except Exception as e:
        print(f"❌ Request failed: {e}")

def test_server_status():
    """Test if the server is running."""
    print("Checking server status...")
    
    try:
        response = requests.get(f"{BASE_URL}/")
        result = response.json()
        print(f"✅ Server is running: {result['message']}")
        return True
    except Exception as e:
        print(f"❌ Server not accessible: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Testing Speech Assistant API")
    print("=" * 40)
    
    # Test server status
    if not test_server_status():
        print("\n❌ Server is not running. Please start the server first:")
        print("   python main.py")
        exit(1)
    
    # Test making a call
    call_sid = test_make_call()
    
    # Test call status
    if call_sid:
        test_call_status(call_sid)
    
    print("\n🎉 Test completed!")