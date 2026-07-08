import os
import requests

# Recogemos tus credenciales secretas de GitHub
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def correr_simulacion():
    print("🤖 Iniciando simulación de prueba para el bot...")
    
    # Mensaje de prueba directo a tu celular
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": "🚀 **¡Simulación Exitosa!** Tu bot de JCF está perfectamente conectado con GitHub. Si estás leyendo esto, significa que las notificaciones a tu celular ya funcionan correctamente. ¡Listo para activar el monitor real!",
        "parse_mode": "Markdown"
    }
    
    try:
        print("📤 Enviando mensaje a Telegram...")
        respuesta = requests.post(url, json=payload, timeout=10)
        
        if respuesta.status_code == 200:
            print("✅ ¡ÉXITO! El mensaje fue enviado. Revisa tu celular en este momento.")
        else:
            print(f"❌ ERROR de Telegram: {respuesta.status_code}")
            print(f"Detalle del error: {respuesta.text}")
            print("\n💡 Tip: Revisa si copiaste bien el Token o el Chat ID en los Secrets de GitHub.")
            
    except Exception as e:
        print(f"❌ Error de red al conectar con Telegram: {e}")

if __name__ == "__main__":
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        print("❌ ERROR CRÍTICO: No se encontraron las variables TELEGRAM_TOKEN o TELEGRAM_CHAT_ID en los Secrets de GitHub.")
        print("Por favor, agrégalas en Settings -> Secrets and variables -> Actions antes de correr la prueba.")
    else:
        correr_simulacion()
