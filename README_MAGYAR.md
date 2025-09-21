# Ujvári Péter Személyes AI Asszisztens

Ez az alkalmazás egy teljesen működőképes beszédfelismerő asszisztens, amely Ujvári Péter személyes AI asszisztenseként működik. A rendszer a Twilio Voice API és az OpenAI Realtime API kombinációját használja valós idejű beszéd felismeréshez és AI válaszok generálásához.

## 🚀 Funkciók

- ✅ **Valós idejű beszéd felismerés** - Az AI azonnal válaszol
- ✅ **Magyar nyelvű kommunikáció** - Teljesen magyar nyelven beszél
- ✅ **Tegeződő stílus** - Barátságos és közvetlen hangnem
- ✅ **Automatikus ngrok URL** - Nem kell manuálisan módosítani
- ✅ **Telefonos hívások** - Bejövő és kimenő hívások kezelése
- ✅ **Személyes bemutatkozás** - Ujvári Péter nevében beszél

## 📋 Előfeltételek

- **Python 3.9+** - Letölthető a [python.org](https://www.python.org/downloads/)-ról
- **Twilio fiók** - Regisztrálj [itt](https://www.twilio.com/try-twilio)
- **Twilio telefonszám** Voice képességekkel
- **OpenAI fiók és API kulcs** - Regisztrálj [itt](https://platform.openai.com/)
- **ngrok** - Töltse le [itt](https://ngrok.com/download)

## ⚙️ Telepítés

### 1. Függőségek telepítése
```bash
pip install -r requirements.txt
```

### 2. Konfiguráció
A `main.py` fájlban módosítsd a következő adatokat:

```python
# ── HARDCODED ADATOK ─────────────────────────────────────────
TWILIO_ACCOUNT_SID = "your_twilio_account_sid"
TWILIO_AUTH_TOKEN  = "your_twilio_auth_token"
FROM_NUMBER        = "+36203663987"        # Verified Caller ID
TO_NUMBER          = "+36209997200"        # hívott szám
OPENAI_API_KEY     = "your_openai_api_key"
```

### 3. Twilio beállítás
- Menj a [Twilio Console](https://console.twilio.com/)-ba
- Válaszd ki a **Phone Numbers** → **Manage** → **Active Numbers** menüt
- Kattints a telefonszámra
- A **A call comes in** mezőben válaszd a **Webhook** opciót
- Add meg az URL-t: `https://your-ngrok-url.ngrok-free.app/incoming-call`

## 🚀 Használat

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

#### 1. Szerver indítása
```bash
cd /Users/ujvaripeter/Desktop/PythonProject/speech-assistant-openai-realtime-api-python
python3 main.py
```

#### 2. ngrok futtatása (másik terminálban)
```bash
/Users/ujvaripeter/ngrok http 5050
```

#### 3. Tesztelés (harmadik terminálban)
```bash
cd /Users/ujvaripeter/Desktop/PythonProject/speech-assistant-openai-realtime-api-python
python3 test_call.py
```

## 📞 Hívás funkciók

### Bejövő hívások
- A Twilio telefonszámot be kell állítani a `/incoming-call` endpointra
- Az AI automatikusan üdvözli a hívót

### Kimenő hívások
- API endpoint: `POST /make-call`
- Automatikus hívás indítása a beállított számra

### Hívás státusz
- API endpoint: `GET /call-status/{call_sid}`
- Hívás részleteinek lekérdezése

## 🎯 AI Személyiség

Az AI asszisztens a következőképpen mutatkozik be:

> "Helló! Én Ujvári Péter személyes MI asszisztense vagyok. Péter nevében beszélgetek veled. Péter jelenleg dolgozik, de én itt vagyok. Hogyan segíthetek?"

### Jellemzők:
- **Tegeződő stílus** - Barátságos és közvetlen
- **Magyar nyelv** - Teljesen magyar nyelven kommunikál
- **Szakmai bemutatkozás** - Péter képességeit mutatja be
- **Segítőkész** - Bárkivel tud beszélni

## 🔧 API Endpoints

- `GET /` - Szerver státusz
- `POST /make-call` - Kimenő hívás indítása
- `GET /call-status/{call_sid}` - Hívás státusz lekérdezése
- `GET/POST /incoming-call` - Bejövő hívás kezelése (TwiML)
- `WebSocket /media-stream` - Audio stream kezelése

## 🛠️ Hibaelhárítás

### Gyakori problémák:

1. **"Missing the OpenAI API key" hiba**
   - Ellenőrizd, hogy az OpenAI API kulcs helyes-e

2. **WebSocket kapcsolat hiba**
   - Ellenőrizd, hogy az ngrok fut-e
   - Az automatikus URL detektálás működik

3. **Twilio hívás nem működik**
   - Ellenőrizd a Twilio hitelesítő adatokat
   - Győződj meg róla, hogy a telefonszámok helyesek

4. **Audio nem hallható**
   - Ellenőrizd, hogy a mikrofon és hangszóró működik
   - A kód automatikusan kezeli a PCMU audio formátumot

## 📱 Telefonos tesztelés

### 1. Twilio Console beállítása:
1. Menj a [Twilio Console](https://console.twilio.com/)-ba
2. Válaszd ki a **Phone Numbers** → **Manage** → **Active Numbers** menüt
3. Kattints a telefonszámra
4. A **A call comes in** mezőben válaszd a **Webhook** opciót
5. Add meg az URL-t: `https://your-ngrok-url.ngrok-free.app/incoming-call`
6. Mentsd el a beállításokat

### 2. Hívás tesztelése:
- Hívd meg a beállított telefonszámot
- Az AI automatikusan üdvözöl és beszélgetni tud veled

### 3. Kimenő hívás tesztelése:
```bash
cd /Users/ujvaripeter/Desktop/PythonProject/speech-assistant-openai-realtime-api-python && python3 test_call.py
```

## 🎉 Gratulálok!

Most már teljesen működőképes a beszédfelismerő asszisztens! 

- ✅ Twilio Voice API működik
- ✅ OpenAI Realtime API működik  
- ✅ Telefonos hívások működnek
- ✅ Magyar nyelvű kommunikáció
- ✅ Automatikus ngrok URL detektálás
- ✅ Személyes AI asszisztens

**Ujvári Péter személyes AI asszisztense készen áll a használatra!** 🚀

## 📞 Kapcsolat

Ha bármilyen kérdésed van, vagy segítségre van szükséged, szívesen segítek!

**Ujvári Péter személyes AI asszisztense** 🤖

