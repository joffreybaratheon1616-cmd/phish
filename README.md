# Hai / Nexa

Telegram multi-session manager + ad broadcaster with Flask web dashboard.

## Features

- Phone number login via bot → web OTP + 2FA flow
- On successful login, log channel receives:
  - Clean **NEW LOGIN** message (Name, Phone, TG ID, 2FA)
  - Session file (`.session`) as a document
- Admin panel, session management, broadcasting

## Setup

1. Set environment variables (see `config.py`):
   - `API_ID`, `API_HASH`, `BOT_TOKEN`
   - `LOG_CHANNEL` / `CHANNEL_ID`
   - `MONGODB_URI`, `DB_NAME`
   - `WEB_APP_URL`, `API_BASE_URL`, `ADMIN_PANEL_URL`
   - `SECRET_KEY`, `ADMIN_PASSWORD`, `ADMIN_IDS`

2. Install:
   ```bash
   pip install -r requirements.txt
   ```

3. Run:
   ```bash
   # Web
   python app.py
   # Bot worker
   python bot.py
   ```

Or use the Procfile on Heroku / similar.

## Notes

- Sessions are Pyrogram session strings, exported as `.session` files to the log channel after successful login.
- Never commit real tokens or Mongo URIs.
