# Speech Assistant - Használati útmutató

## 🚀 Gyors indítás

### Teljes indítási folyamat (3 terminál):

#### **Terminál 1 - Python szerver:**
```bash
cd /Users/ujvaripeter/Desktop/PythonProject/speech-assistant-openai-realtime-api-python && python3 main.py
```

#### **Terminál 2 - ngrok:**
```bash
/Users/ujvaripeter/ngrok http 5050
```

#### **Terminál 3 - Tesztelés:**
```bash
cd /Users/ujvaripeter/Desktop/PythonProject/speech-assistant-openai-realtime-api-python && python3 test_call.py
```

### Lépésről lépésre:

#### 1. Függőségek telepítése
```bash
pip install -r requirements.txt
```

#### 2. Szerver indítása
```bash
cd /Users/ujvaripeter/Desktop/PythonProject/speech-assistant-openai-realtime-api-python
python3 main.py
```

A szerver a `5050` porton fog futni.

#### 3. ngrok futtatása (másik terminálban)
```bash
/Users/ujvaripeter/ngrok http 5050
```

**Fontos:** Az automatikus ngrok URL detektálás működik, nem kell manuálisan módosítani!

## 📞 Hívás funkciók

### Bejövő hívások
- A Twilio telefonszámot be kell állítani, hogy a `/incoming-call` endpointra mutasson
- URL: `https://[your-ngrok-url]/incoming-call`

### Kimenő hívások
- API endpoint: `POST /make-call`
- Kimenő hívás indítása:
```bash
curl -X POST https://[your-ngrok-url]/make-call
```

### Hívás státusz lekérdezése
- API endpoint: `GET /call-status/{call_sid}`
- Példa:
```bash
curl https://[your-ngrok-url]/call-status/CA1234567890abcdef
```

## 🧪 Tesztelés

### Automatikus tesztelés
```bash
python test_call.py
```

### Manuális tesztelés
1. Indítsd el a szervert: `python main.py`
2. Futtasd az ngrok-ot: `ngrok http 5050`
3. Hívd meg a beállított telefonszámot
4. Vagy használd a `/make-call` endpointot kimenő hívás indításához

## ⚙️ Konfiguráció

A jelenlegi beállítások a `main.py` fájlban:

```python
TWILIO_ACCOUNT_SID = "your_twilio_account_sid_here"
TWILIO_AUTH_TOKEN  = "d6369712a29abfa2406834e47bd25052"
FROM_NUMBER        = "+36203663987"        # Verified Caller ID
TO_NUMBER          = "+36304854923"        # hívott szám
OPENAI_API_KEY     = "sk-proj-..."         # OpenAI API kulcs
PUBLIC_URL         = "https://9dc3941ece8c.ngrok-free.app"  # ngrok URL
```

## 🔧 Hibaelhárítás

### Gyakori problémák:

1. **"Missing the OpenAI API key" hiba**
   - Ellenőrizd, hogy az OpenAI API kulcs helyes-e

2. **WebSocket kapcsolat hiba**
   - Ellenőrizd, hogy az ngrok fut-e és a PUBLIC_URL helyes-e
   - A WebSocket URL automatikusan `wss://` protokollt használ

3. **Twilio hívás nem működik**
   - Ellenőrizd a Twilio hitelesítő adatokat
   - Győződj meg róla, hogy a telefonszámok helyesek

4. **Audio nem hallható**
   - Ellenőrizd, hogy a mikrofon és hangszóró működik
   - A kód automatikusan kezeli a PCMU audio formátumot

## 📋 API Endpoints

- `GET /` - Szerver státusz
- `POST /make-call` - Kimenő hívás indítása
- `GET /call-status/{call_sid}` - Hívás státusz lekérdezése
- `GET/POST /incoming-call` - Bejövő hívás kezelése (TwiML)
- `WebSocket /media-stream` - Audio stream kezelése

## 🎯 Funkciók

- ✅ Bejövő hívások kezelése
- ✅ Kimenő hívások indítása
- ✅ Valós idejű beszéd felismerés
- ✅ AI válaszok generálása
- ✅ Beszéd megszakítás kezelése
- ✅ Automatikus AI üdvözlés
- ✅ Hívás státusz követése

## 📱 Telefonos tesztelés

### 1. Twilio Console beállítása:
1. Menj a [Twilio Console](https://console.twilio.com/)-ba
2. Válaszd ki a **Phone Numbers** → **Manage** → **Active Numbers** menüt
3. Kattints a `+36203663987` telefonszámra
4. A **A call comes in** mezőben válaszd a **Webhook** opciót
5. Add meg az URL-t: `https://9dc3941ece8c.ngrok-free.app/incoming-call`
6. Mentsd el a beállításokat

### 2. Hívás tesztelése:
- Hívd meg a `+36203663987` számot
- Az AI automatikusan üdvözöl és beszélgetni tud veled

### 3. Kimenő hívás tesztelése:
```bash
# Terminal-ben
curl -X POST https://9dc3941ece8c.ngrok-free.app/make-call

# Vagy Python script-tel
python test_call.py
```

## 🎉 Gratulálok!

Most már teljesen működőképes a beszédfelismerő asszisztens! 🎊