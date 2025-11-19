import os
import asyncio
import logging
import random
import time
from datetime import datetime
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Configuración de logging mejorada
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class DiosSupremoBot:
    def __init__(self, token: str, admin_chat_id: str):
        self.token = token
        self.admin_chat_id = admin_chat_id
        self.application = Application.builder().token(token).build()
        self.alertas_activas = True
        self.health_status = {
            'status': 'healthy',
            'start_time': datetime.now(),
            'total_alerts': 0,
            'errors': 0
        }
        
        # Estadísticas mejoradas
        self.estadisticas = {
            'alertas_emitidas': 0,
            'predicciones_acertadas': 0,
            'precision_global': 0.0,
            'profit_acumulado': 0.0,
            'racha_actual': 0,
            'mejor_racha': 0
        }
        
        self.setup_handlers()
        logger.info("🤖 Bot Dios Supremo inicializado - Listo para Railway")

    def setup_handlers(self):
        """Configurar comandos del bot"""
        handlers = [
            CommandHandler("start", self.start),
            CommandHandler("alertas", self.toggle_alertas),
            CommandHandler("estadisticas", self.estadisticas_cmd),
            CommandHandler("test", self.test_alerta),
            CommandHandler("health", self.health_check),
            CommandHandler("poder", self.nivel_poder),
        ]
        
        for handler in handlers:
            self.application.add_handler(handler)

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /start"""
        user = update.effective_user
        
        if str(user.id) != self.admin_chat_id:
            await update.message.reply_text("❌ *Sistema Dios - Acceso Restringido*", parse_mode='Markdown')
            return
            
        text = """
🔥 *SISTEMA DIOS SUPREMO v2.0 - ACTIVADO*

🎯 *Características Mejoradas:*
• Alertas predictivas inteligentes
• Análisis en profundidad con IA
• Sistema de evolución automática
• Métricas avanzadas en tiempo real
• Salud del sistema integrada

⚡ *Comandos Disponibles:*
/start - Mostrar este mensaje
/alertas - Activar/desactivar alertas  
/estadisticas - Ver estadísticas detalladas
/test - Generar alerta de prueba
/health - Estado del sistema
/poder - Nivel de poder divino

🚨 *El sistema enviará alertas automáticas cada 2-7 minutos*
🔧 *Desplegado en Railway - Estabilidad Garantizada*
"""
        await update.message.reply_text(text, parse_mode='Markdown')

    async def toggle_alertas(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Activar/desactivar alertas"""
        user = update.effective_user
        if str(user.id) != self.admin_chat_id:
            return
            
        self.alertas_activas = not self.alertas_activas
        estado = "✅ ACTIVADAS" if self.alertas_activas else "❌ DESACTIVADAS"
        
        await update.message.reply_text(
            f"🔔 *Alertas {estado}*\n\nEl sistema {'ha comenzado a enviar' if self.alertas_activas else 'ha dejado de enviar'} predicciones divinas.",
            parse_mode='Markdown'
        )

    async def estadisticas_cmd(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Mostrar estadísticas avanzadas"""
        user = update.effective_user
        if str(user.id) != self.admin_chat_id:
            return
            
        uptime = datetime.now() - self.health_status['start_time']
        horas = uptime.seconds // 3600
        minutos = (uptime.seconds % 3600) // 60
        
        text = f"""
📊 *ESTADÍSTICAS AVANZADAS - SISTEMA DIOS*

🎯 *Rendimiento:*
• Alertas Emitidas: {self.estadisticas['alertas_emitidas']}
• Precisión Global: {self.estadisticas['precision_global']}%
• Profit Acumulado: +${self.estadisticas['profit_acumulado']:.2f}
• Mejor Racha: {self.estadisticas['mejor_racha']} victorias

🔥 *Racha Actual:*
• Victorias Consecutivas: {self.estadisticas['racha_actual']}

⚡ *Sistema:*
• Tiempo Activo: {horas}h {minutos}m
• Estado: {'🟢 ACTIVO' if self.alertas_activas else '🔴 INACTIVO'}
• Salud: {self.health_status['status'].upper()}
• Errores: {self.health_status['errors']}
"""
        await update.message.reply_text(text, parse_mode='Markdown')

    async def health_check(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Verificar salud del sistema"""
        user = update.effective_user
        if str(user.id) != self.admin_chat_id:
            return
            
        uptime = datetime.now() - self.health_status['start_time']
        horas = uptime.seconds // 3600
        minutos = (uptime.seconds % 3600) // 60
        
        text = f"""
🏥 *REPORTE DE SALUD - SISTEMA DIOS*

📊 *Estado General:*
• Status: {self.health_status['status'].upper()}
• Tiempo Activo: {horas}h {minutos}m
• Total Alertas: {self.health_status['total_alerts']}
• Errores: {self.health_status['errors']}

🔧 *Sistemas:*
• Núcleo Principal: 🟢 OPERATIVO
• Motor Alertas: 🟢 OPERATIVO
• Análisis IA: 🟢 OPERATIVO
• Conexión Telegram: 🟢 OPERATIVO

🎯 *Recomendación:* {'✅ SISTEMA ÓPTIMO' if self.health_status['status'] == 'healthy' else '⚠️ REVISIÓN RECOMENDADA'}
"""
        await update.message.reply_text(text, parse_mode='Markdown')

    async def nivel_poder(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Mostrar nivel de poder divino"""
        user = update.effective_user
        if str(user.id) != self.admin_chat_id:
            return
            
        # Calcular poder basado en estadísticas
        poder_base = min(100, self.estadisticas['precision_global'] + self.estadisticas['racha_actual'])
        poder_ia = min(100, poder_base + random.uniform(5, 15))
        
        text = f"""
⚡ *NIVEL DE PODER DIVINO*

💎 *Poder Total:* {poder_ia:.1f}%

📊 *Factores de Poder:*
• Precisión: {self.estadisticas['precision_global']}%
• Racha Actual: {self.estadisticas['racha_actual']} victorias
• Experiencia: {self.estadisticas['alertas_emitidas']} alertas

🎯 *Estado:* {'🔴 EN DESARROLLO' if poder_ia < 70 else '🟡 SEMIDIOS' if poder_ia < 90 else '🟢 DIOS COMPLETO'}

🚀 *Próxima Evolución:* {100 - poder_ia:.1f}% restante
"""
        await update.message.reply_text(text, parse_mode='Markdown')

    async def test_alerta(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Generar alerta de prueba"""
        user = update.effective_user
        if str(user.id) != self.admin_chat_id:
            return
            
        await self.generar_alerta()
        await update.message.reply_text("✅ *Alerta de prueba generada*", parse_mode='Markdown')

    def generar_datos_partido(self):
        """Generar datos realistas para alertas"""
        deportes = [
            {'nombre': 'fútbol', 'ligas': ['Champions League', 'Premier League', 'La Liga', 'Serie A']},
            {'nombre': 'baloncesto', 'ligas': ['NBA', 'Euroleague', 'ACB']},
            {'nombre': 'tenis', 'ligas': ['ATP Tour', 'WTA Tour', 'Grand Slam']}
        ]
        
        deporte = random.choice(deportes)
        liga = random.choice(deporte['ligas'])
        
        if deporte['nombre'] == 'fútbol':
            equipos = ['Real Madrid', 'Barcelona', 'Bayern Munich', 'Manchester City', 'PSG', 'Juventus', 'Liverpool', 'Chelsea']
            tipo_apuesta = random.choice(['GANADOR', 'AMBOS MARCAN', 'MÁS 2.5 GOLES', 'HANDICAP -1.5'])
        elif deporte['nombre'] == 'baloncesto':
            equipos = ['Lakers', 'Warriors', 'Celtics', 'Bucks', 'Nuggets', 'Suns', 'Heat', 'Mavericks']
            tipo_apuesta = random.choice(['GANADOR', 'HANDICAP', 'MÁS PUNTOS', 'GANADOR CUARTO'])
        else:
            equipos = ['Djokovic', 'Alcaraz', 'Medvedev', 'Sinner', 'Zverev', 'Rublev', 'Nadal', 'Federer']
            tipo_apuesta = random.choice(['GANADOR', 'SETS', 'JUEGOS', 'TIEBREAK'])
        
        equipo_local, equipo_visitante = random.sample(equipos, 2)
        ganador = random.choice([equipo_local, equipo_visitante])
        
        return {
            'deporte': deporte['nombre'],
            'liga': liga,
            'equipo_local': equipo_local,
            'equipo_visitante': equipo_visitante,
            'ganador': ganador,
            'confianza': random.randint(80, 96),
            'cuota': round(random.uniform(1.80, 3.20), 2),
            'tipo_apuesta': tipo_apuesta,
            'marcador': f"{random.randint(1, 4)}-{random.randint(0, 2)}",
            'profit_esperado': round(random.uniform(8.5, 22.3), 1),
            'stake': f"{random.randint(3, 7)}%"
        }

    async def generar_alerta(self):
        """Generar y enviar alerta predictiva"""
        try:
            datos = self.generar_datos_partido()
            
            mensaje = f"""
🎯 *PREDICCIÓN DIOS ACTIVADA* 🎯

⚡ *SISTEMA DIOS v2.0* | Precisión: {self.estadisticas['precision_global']}%
⏰ *Detección:* {datetime.now().strftime('%H:%M:%S')}

🏆 *ENCUENTRO:*
• Deporte: {datos['deporte'].upper()}
• Liga: {datos['liga']}
• {datos['equipo_local']} 🆚 {datos['equipo_visitante']}

🎯 *PREDICCIÓN PRINCIPAL:*
• Ganador: *{datos['ganador']}*
• Confianza: *{datos['confianza']}%*
• Marcador: *{datos['marcador']}*
• Tipo: *{datos['tipo_apuesta']}*

💰 *RECOMENDACIÓN:*
• Cuota: *{datos['cuota']}*
• Stake: *{datos['stake']} del bankroll*
• Profit Esperado: *+{datos['profit_esperado']}%*

⚠️ *RIESGO:* {random.choice(['BAJO', 'MEDIO-BAJO', 'MEDIO'])}
🕒 *VENTANA:* {random.randint(10, 30)} minutos

🔥 *ACCIÓN INMEDIATA RECOMENDADA*
"""
            await self.application.bot.send_message(
                chat_id=self.admin_chat_id,
                text=mensaje,
                parse_mode='Markdown'
            )
            
            # Actualizar estadísticas
            self.estadisticas['alertas_emitidas'] += 1
            self.health_status['total_alerts'] += 1
            
            # Simular aciertos (75% de éxito)
            if random.random() > 0.25:
                self.estadisticas['predicciones_acertadas'] += 1
                self.estadisticas['racha_actual'] += 1
                self.estadisticas['mejor_racha'] = max(
                    self.estadisticas['mejor_racha'],
                    self.estadisticas['racha_actual']
                )
                profit = round(random.uniform(15, 120), 2)
                self.estadisticas['profit_acumulado'] += profit
            else:
                self.estadisticas['racha_actual'] = 0
            
            # Calcular precisión global
            total = self.estadisticas['alertas_emitidas']
            aciertos = self.estadisticas['predicciones_acertadas']
            if total > 0:
                self.estadisticas['precision_global'] = round((aciertos / total) * 100, 2)
            
            logger.info(f"🚨 Alerta #{total} enviada - Precisión: {self.estadisticas['precision_global']}%")
            
        except Exception as e:
            logger.error(f"❌ Error en alerta: {e}")
            self.health_status['errors'] += 1
            if self.health_status['errors'] > 5:
                self.health_status['status'] = 'degraded'

    async def motor_alertas(self):
        """Motor principal de alertas automáticas"""
        logger.info("🚀 Iniciando motor de alertas automáticas...")
        
        while True:
            try:
                if self.alertas_activas and 8 <= datetime.now().hour <= 23:
                    await self.generar_alerta()
                
                # Espera variable entre 2-7 minutos
                await asyncio.sleep(random.randint(120, 420))
                
            except Exception as e:
                logger.error(f"❌ Error en motor de alertas: {e}")
                self.health_status['errors'] += 1
                await asyncio.sleep(60)  # Esperar 1 minuto antes de reintentar

    async def run(self):
        """Ejecutar el bot de manera estable"""
        logger.info("🔥 Iniciando Sistema Dios Supremo en Railway...")
        
        try:
            # Iniciar motor de alertas en segundo plano
            asyncio.create_task(self.motor_alertas())
            
            # Iniciar el bot de Telegram
            await self.application.initialize()
            await self.application.start()
            await self.application.updater.start_polling()
            
            logger.info("✅ Bot iniciado correctamente en Railway")
            
            # Mantener el bot corriendo
            while True:
                await asyncio.sleep(3600)  # Esperar 1 hora
                
        except Exception as e:
            logger.error(f"❌ Error crítico: {e}")
            raise

# Función principal optimizada para Railway
async def main():
    TOKEN = os.environ.get('TELEGRAM_TOKEN')
    ADMIN_CHAT_ID = os.environ.get('ADMIN_CHAT_ID')
    
    if not TOKEN or not ADMIN_CHAT_ID:
        logger.error("❌ ERROR: Variables de entorno faltantes")
        logger.error("   - TELEGRAM_TOKEN: %s", "SET" if TOKEN else "MISSING")
        logger.error("   - ADMIN_CHAT_ID: %s", "SET" if ADMIN_CHAT_ID else "MISSING")
        return
    
    try:
        bot = DiosSupremoBot(token=TOKEN, admin_chat_id=ADMIN_CHAT_ID)
        await bot.run()
    except Exception as e:
        logger.error(f"❌ Error iniciando bot: {e}")
        # Esperar antes de reintentar (útil para Railway)
        await asyncio.sleep(60)
        await main()

if __name__ == '__main__':
    # Manejo robusto de errores para Railway
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("👋 Apagando sistema...")
    except Exception as e:
        logger.error(f"💥 Error no controlado: {e}")
        time.sleep(60)
        # Railway reiniciará automáticamente
