# Meshtastic Discord Integrations

A collection of Discord integrations for Meshtastic communities.  
Built in Python, powered by the [MeshView API](https://meshview.louisianamesh.org) (Meshtastic MQTT schema).  
Originally developed with the Louisiana Meshtastic community, but usable by any group running a MeshView backend.

---

## ✨ Features

- **Chat Relay**: Mirrors mesh chat packets from MeshView API into a Discord channel using webhooks.
- Lightweight Python service — easy to run inside a Linux container.
- Systemd integration for always-on operation.
- Modular design planned — future modules (node presence, stats, alerts) can be enabled independently.

---

## 📦 Requirements

- Debian 12+ (or similar Linux environment)
- Python 3.11+
- `requests` library (`apt install python3-requests -y`)

---

## ⚙️ Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/LouisianaMeshCommunit/meshtastic-discord-integrations.git
   cd meshtastic-discord-integrations
