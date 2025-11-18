import os
import asyncio
import logging
import random
from datetime import datetime
from typing import Dict, List, Tuple

# Configuración de logging mejorada
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('dios_supremo.log')
    ]
)
logger = logging.getLogger(__name__)

try:
    from telegram import Update
    from telegram.ext import Application, CommandHandler, ContextTypes
    from dotenv import load_dotenv
    load_dotenv()
    DEPENDENCIAS_CARGADAS = True
except ImportError as e:
    logger.error(f"❌ Error importando dependencias: {e}")
    DEPENDENCIAS_CARGADAS = False

class DiosSupremoRender:
    def __init__(self):
        if not DEPENDENCIAS_CARGADAS:
            raise ImportError("Dependencias no disponibles")
        
        self.token = os.getenv('TELEGRAM_TOKEN')
        self.admin_chat_id = os.getenv('ADMIN_CHAT_ID')
        
        if not self.token or not self.admin_chat_id:
            raise ValueError("❌ Configura TELEGRAM_TOKEN y ADMIN_CHAT_ID en Render")
            
        self.application = Application.builder().token(self.token).build()
        
        # 🔥 CONFIGURACIÓN OPTIMIZADA PARA RENDER
        self.estado_sistema = {
            'omnisciencia': 95.5,
            'omnipresencia': 45,
            'omnipotencia': 96.2,
            'experiencia': 1.0,
            'alertas_activas': True,
            'racha_actual': 0,
            'precision_global': 0.0,
            'total_alertas': 0,
            'aciertos': 0
        }
        
        self.habilidades = [
            "Predicción Básica", "Análisis Táctico", "Detección de Momentum",
            "Visión Cuántica", "Optimización Inteligente"
        ]
        
        # 🎯 DATOS DEPORTIVOS OPTIMIZADOS
        self.deportes = {
            'futbol': {
                'equipos': ['Real Madrid', 'Bayern', 'Man City', 'PSG', 'Barcelona', 'Liverpool'],
                'ligas': ['Champions', 'Premier League', 'La Liga', 'Serie A']
            },
            'baloncesto': {
                'equipos': ['Lakers', 'Warriors', 'Celtics', 'Bucks', 'Nuggets'],
                'ligas': ['NBA', 'Euroleague']
            },
            'tenis': {
                'jugadores': ['Djokovic', 'Alcaraz', 'Medvedev', 'Sinner', 'Zverev'],
                'torneos': ['Wimbledon', 'US Open', 'Roland Garros', 'Australian Open']
            }
        }
        
        self.setup_handlers()
        self._iniciar_subsistemas()
        logger.info("✅ DIOS SUPREMO INICIALIZADO EN RENDER")

    def _iniciar_subsistemas(self):
        """Iniciar todos los sistemas en segundo plano"""
        asyncio.create_task(self._motor_principal())
        asyncio.create_task(self._sistema_evolucion())
        logger.info("🔧 Subsistemas activados")

    async def _motor_principal(self):
        """Motor principal de alertas optimizado para Render"""
        while self.estado_sistema['alertas_activas']:
            try:
                # Intervalos más largos para evitar timeouts en Render
                wait_time = random.randint(300, 600)  # 5-10 minutos
                await asyncio.sleep(wait_time)
                
                if 9 <= datetime.now().hour <= 23:  # Horario activo extendido
                    await self._generar_alerta_inteligente()
                    
            except Exception as e:
                logger.error(f"⚠️ Error en motor principal: {e}")
                await asyncio.sleep(60)  # Espera antes de reintentar

    async def _sistema_evolucion(self):
        """Sistema de evolución automática"""
        while True:
            await asyncio.sleep(1800)  # Cada 30 minutos
            # Mejora gradual de capacidades
            self.estado_sistema['omnisciencia'] = min(100.0, 
                self.estado_sistema['omnisciencia'] + 0.1)
            self.estado_sistema['experiencia'] += 0.05
            
            # Desbloquear habilidades en niveles específicos
            if (self.estado_sistema['experiencia'] >= 3.0 and 
                "Predicción Multidimensional" not in self.habilidades):
                self.habilidades.append("Predicción Multidimensional")
                await self._enviar_evolucion("🔮 Predicción Multidimensional desbloqueada!")

    async def _generar_alerta_inteligente(self):
        """Generar alerta optimizada"""
        try:
            datos = self._generar_datos_partido()
            mensaje = self._formatear_alerta(datos)
            
            await self.application.bot.send_message(
                chat_id=self.admin_chat_id,
                text=mensaje,
                parse_mode='Markdown'
            )
            
            # 📊 ACTUALIZAR ESTADÍSTICAS
            self.estado_sistema['total_alertas'] += 1
            
            # Simular acierto (75% de precisión)
            if random.random() > 0.25:
                self.estado_sistema['aciertos'] += 1
                self.estado_sistema['racha_actual'] += 1
            else:
                self.estado_sistema['racha_actual'] = 0
                
            # Calcular precisión
            total = self.estado_sistema['total_alertas']
            aciertos = self.estado_sistema['aciertos']
            if total > 0:
                self.estado_sistema['precision_global'] = round((aciertos / total) * 100, 2)
            
            logger.info(f"📨 Alerta {total} enviada - Precisión: {self.estado_sistema['precision_global']}%")
            
        except Exception as e:
            logger.error(f"❌ Error enviando alerta: {e}")

    def _generar_datos_partido(self) -> Dict:
        """Generar datos de partido realistas"""
        deporte = random.choice(['futbol', 'baloncesto', 'tenis'])
        
        if deporte == 'futbol':
            equipo_local, equipo_visitante = random.sample(self.deportes['futbol']['equipos'], 2)
            liga = random.choice(self.deportes['futbol']['ligas'])
        elif deporte == 'baloncesto':
            equipo_local, equipo_visitante = random.sample(self.deportes['baloncesto']['equipos'], 2)
            liga = random.choice(self.deportes['baloncesto']['ligas'])
        else:
            equipo_local, equipo_visitante = random.sample(self.deportes['tenis']['jugadores'], 2)
            liga = random.choice(self.deportes['tenis']['torneos'])
        
        return {
            'deporte': deporte,
            'liga': liga,
            'equipo_local': equipo_local,
            'equipo_visitante': equipo_visitante,
            'ganador_predicho': equipo_local if random.random() > 0.4 else equipo_visitante,
            'confianza': random.randint(85, 96),
            'marcador': f"{random.randint(1, 3)}-{random.randint(0, 2)}",
            'tipo_apuesta': random.choice([
                "GANADOR", "AMBOS MARCAN", "MÁS 2.5 GOLES", 
                "HANDICAP -1.5", "DOBLE OPORTUNIDAD"
            ]),
            'cuota': round(random.uniform(1.70, 2.80), 2),
            'stake': f"{random.randint(2, 6)}%",
            'ventana': f"{random.randint(10, 25)} min",
            'hora': datetime.now().strftime("%H:%M"),
            'profit_esperado': round(random.uniform(8.5, 22.3), 1)
        }

    def _formatear_alerta(self, datos: Dict) -> str:
        """Formatear alerta para Telegram"""
        return f"""
🎯 *ALERTA DIOS SUPREMO* 🎯

⚡ *Sistema v3.0* | Precisión: {self.estado_sistema['precision_global']}%
🕒 *Hora:* {datos['hora']}

🏆 *ENCUENTRO:*
• {datos['equipo_local']} 🆚 {datos['equipo_visitante']}
• {datos['liga']} | {datos['deporte'].upper()}

🎯 *PREDICCIÓN:*
• Ganador: *{datos['ganador_predicho']}*
• Confianza: *{datos['confianza']}%*
• Marcador: *{datos['marcador']}*

💰 *INVERSIÓN:*
• Apuesta: *{datos['tipo_apuesta']}*
• Cuota: *{datos['cuota']}*
• Stake: *{datos['stake']} del bankroll*
• Profit Esperado: *+{datos['profit_esperado']}%*

⚠️ *Acción recomendada en los próximos {datos['ventana']}*

🔥 *Sistema activo - Rachas: {self.estado_sistema['racha_actual']}*
"""

    async def _enviar_evolucion(self, mensaje: str):
        """Enviar mensaje de evolución"""
        try:
            await self.application.bot.send_message(
                chat_id=self.admin_chat_id,
                text=f"*🔮 EVOLUCIÓN:* {mensaje}",
                parse_mode='Markdown'
            )
        except Exception as e:
            logger.error(f"Error enviando evolución: {e}")

    def setup_handlers(self):
        """Configurar comandos de Telegram"""
        handlers = [
            CommandHandler("start", self.comando_start),
            CommandHandler("alertas", self.comando_alertas),
            CommandHandler("estadisticas", self.comando_estadisticas),
            CommandHandler("sistema", self.comando_sistema),
            CommandHandler("test", self.comando_test),
        ]
        
        for handler in handlers:
            self.application.add_handler(handler)

    async def comando_start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando de inicio"""
        user = update.effective_user
        
        if str(user.id) != self.admin_chat_id:
            await update.message.reply_text("❌ *Acceso restringido*", parse_mode='Markdown')
            return
            
        texto = f"""
🤖 *DIOS SUPREMO - ACTIVADO*

✅ *Sistema operativo en Render*
🎯 *Precisión actual:* {self.estado_sistema['precision_global']}%
🔮 *Habilidades:* {len(self.habilidades)}

⚡ *Comandos disponibles:*
/alertas - Activar/desactivar alertas
/estadisticas - Ver métricas avanzadas  
/sistema - Estado del sistema
/test - Generar alerta de prueba

🚨 *Alertas automáticas cada 5-10 minutos*
"""
        await update.message.reply_text(texto, parse_mode='Markdown')

    async def comando_alertas(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Activar/desactivar alertas"""
        user = update.effective_user
        if str(user.id) != self.admin_chat_id:
            return
            
        self.estado_sistema['alertas_activas'] = not self.estado_sistema['alertas_activas']
        estado = "✅ ACTIVADAS" if self.estado_sistema['alertas_activas'] else "❌ DESACTIVADAS"
        
        await update.message.reply_text(
            f"🔔 *Alertas {estado}*\n\nEl sistema {'está enviando' if self.estado_sistema['alertas_activas'] else 'ha parado'} predicciones.",
            parse_mode='Markdown'
        )

    async def comando_estadisticas(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Mostrar estadísticas"""
        user = update.effective_user
        if str(user.id) != self.admin_chat_id:
            return
            
        texto = f"""
📊 *ESTADÍSTICAS AVANZADAS*

🎯 *Rendimiento:*
• Alertas Totales: {self.estado_sistema['total_alertas']}
• Precisión: {self.estado_sistema['precision_global']}%
• Racha Actual: {self.estado_sistema['racha_actual']}
• Aciertos: {self.estado_sistema['aciertos']}

⚡ *Sistema:*
• Experiencia: {self.estado_sistema['experiencia']:.2f}
• Habilidades: {len(self.habilidades)}
• Estado: {'🟢 ACTIVO' if self.estado_sistema['alertas_activas'] else '🔴 INACTIVO'}
"""
        await update.message.reply_text(texto, parse_mode='Markdown')

    async def comando_sistema(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Estado del sistema"""
        user = update.effective_user
        if str(user.id) != self.admin_chat_id:
            return
            
        texto = f"""
🔧 *ESTADO DEL SISTEMA*

🧠 *Núcleo Divino:*
• Omnisciencia: {self.estado_sistema['omnisciencia']:.1f}%
• Omnipotencia: {self.estado_sistema['omnipotencia']:.1f}%
• Nodos Activos: {self.estado_sistema['omnipresencia']}

🎯 *Habilidades Desbloqueadas:*
{chr(10).join(f'• {hab}' for hab in self.habilidades)}

📈 *Próxima Evolución:*
• Experiencia necesaria: {3.0 - self.estado_sistema['experiencia']:.2f}
• Tiempo estimado: {max(1, int((3.0 - self.estado_sistema['experiencia']) / 0.05 * 0.5))} horas
"""
        await update.message.reply_text(texto, parse_mode='Markdown')

    async def comando_test(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Generar alerta de prueba"""
        user = update.effective_user
        if str(user.id) != self.admin_chat_id:
            return
            
        await self._generar_alerta_inteligente()
        await update.message.reply_text("✅ *Alerta de prueba generada*", parse_mode='Markdown')

    async def run_webhook(self):
        """Ejecutar con webhook para Render"""
        try:
            port = int(os.environ.get('PORT', 8443))
            webhook_url = os.getenv('RENDER_EXTERNAL_URL')
            
            if webhook_url:
                await self.application.bot.set_webhook(
                    url=f"{webhook_url}/webhook"
                )
                logger.info(f"🌐 Webhook configurado: {webhook_url}")
            
            await self.application.run_webhook(
                listen="0.0.0.0",
                port=port,
                webhook_url=f"{webhook_url}/webhook" if webhook_url else None,
            )
        except Exception as e:
            logger.error(f"❌ Error webhook: {e}")

    async def run_polling(self):
        """Ejecutar con polling para desarrollo"""
        await self.application.run_polling()

# 🚀 INICIALIZACIÓN OPTIMIZADA PARA RENDER
async def main():
    try:
        bot = DiosSupremoRender()
        
        # Determinar modo de ejecución
        if os.getenv('RENDER'):
            logger.info("🚀 Iniciando en modo WEBHOOK para Render")
            await bot.run_webhook()
        else:
            logger.info("🔧 Iniciando en modo POLLING para desarrollo")
            await bot.run_polling()
            
    except Exception as e:
        logger.error(f"❌ Error crítico: {e}")
        # Esperar antes de reintentar en caso de error
        await asyncio.sleep(60)

if __name__ == '__main__':
    asyncio.run(main())
