import marimo

__generated_with = "0.9.14"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    from datetime import datetime
    return datetime, mo


@app.cell
def __(mo, datetime):
    mo.md(
        f"""
        # 🎨 DOSSIER FREEPIK - BUSINESS ANALYST
        ## Preparación Específica para Entrevista
        
        **Candidato:** Iván Reyes Laguna  
        **Empresa:** Freepik (Málaga, España)  
        **Fecha:** {datetime.now().strftime("%B %Y")}  
        **Rol objetivo:** Business Analyst | Financial Planner (Data-driven)
        
        ---
        
        ## 🚀 **FREEPIK EN NÚMEROS (2024)**
        - **52+ millones** de usuarios mensuales
        - **23,000+ colaboradores** en todo el mundo
        - **Presencia en 99%** de países
        - **Valoración:** 200-300M € (EQT, 2020)
        - **Fundada:** 2010 en Málaga
        - **Mercados principales:** India, Brasil, España, EEUU
        """
    )
    return


@app.cell
def __(mo):
    # Información específica de Freepik
    mo.md(
        """
        ## 🏢 **ANÁLISIS PROFUNDO DE FREEPIK**
        
        ### **🎯 Modelo de Negocio:**
        - **Freemium:** Contenido gratuito + Suscripciones Premium
        - **Suite Creativa IA:** Transición de banco de imágenes a plataforma integral
        - **Múltiples productos:** Freepik, Slidesgo, Flaticon, Wepik, Videvo, Storyset, Iconfinder
        
        ### **🤖 Estrategia IA (Clave para BA):**
        - **IA Generativa:** Creación de imágenes por descripciones
        - **Pikaso:** Herramienta de IA para generación visual
        - **Wepik:** Editor online con IA integrada
        - **Upscale Conf:** Evento mundial sobre IA generativa
        
        ### **📊 KPIs Críticos para BA:**
        - **User Engagement:** Downloads, tiempo en plataforma
        - **Conversion Rate:** Free → Premium
        - **Content Performance:** Trending assets, search patterns  
        - **Revenue Metrics:** ARPU, LTV, Churn rate
        - **Geographic Expansion:** Market penetration por país
        
        ### **🌍 Expansión Internacional:**
        - **2023:** Entrada agresiva en mercado estadounidense
        - **Oficinas:** Málaga (HQ), Cartagena, Copenhague, Oxford
        - **Adquisiciones:** Videvo (UK), Iconfinder (DK), Original Mockups (CO)
        """
    )
    return


@app.cell
def __(mo):
    # Competencia y posicionamiento
    mo.md(
        """
        ## 🏆 **ANÁLISIS COMPETITIVO**
        
        ### **Competidores Principales:**
        - **Shutterstock:** Líder tradicional en stock media
        - **Canva:** Competidor directo en design tools
        - **Adobe Stock:** Integrado con Creative Suite
        - **Getty Images:** Premium stock photography
        
        ### **Diferenciadores de Freepik:**
        ✅ **Modelo freemium** más accesible  
        ✅ **Suite integrada** de herramientas  
        ✅ **IA generativa** avanzada  
        ✅ **Comunidad de creadores** global  
        ✅ **Precio competitivo** vs Shutterstock  
        
        ### **Oportunidades para BA:**
        - **Análisis de pricing** vs competencia
        - **User journey optimization** free → premium
        - **Geographic expansion** metrics y strategy
        - **Product performance** analysis cross-platform
        - **AI adoption** impact on business metrics
        """
    )
    return


@app.cell
def __(mo):
    # Preguntas específicas para Freepik
    pregunta_selector = mo.ui.dropdown(
        options=[
            "Modelo de Negocio Freemium",
            "Estrategia IA y Datos", 
            "Expansión Internacional",
            "Análisis Competitivo",
            "KPIs y Métricas Clave"
        ],
        label="🎯 Selecciona área de preparación:",
        value="Modelo de Negocio Freemium"
    )
    
    mo.md(f"## 🔍 **PREPARACIÓN ESPECÍFICA FREEPIK**\n\n{pregunta_selector}")
    return pregunta_selector,


@app.cell
def __(mo, pregunta_selector):
    if pregunta_selector.value == "Modelo de Negocio Freemium":
        situacion = mo.ui.text_area(
            label="📍 Situación (Freepik context):",
            value="En Avatel trabajé con modelos de suscripción y análisis de conversion rates...",
            rows=3
        )
        
        analisis = mo.ui.text_area(
            label="📊 Tu análisis del modelo freemium:",
            value="El modelo freemium de Freepik es brillante porque permite sampling del producto antes del pago, similar a como analicé el customer journey en Avatel...",
            rows=4
        )
        
        propuesta = mo.ui.text_area(
            label="💡 Tu propuesta de mejora:",
            value="Implementaría análisis predictivo para identificar usuarios con alta probabilidad de conversión, similar a mi trabajo de forecasting en Avatel...",
            rows=3
        )
        
        content = mo.vstack([
            mo.md(
                """
                ### **Pregunta: ¿Cómo analizarías la efectividad del modelo freemium de Freepik?**
                
                #### **🎯 Framework de respuesta:**
                """
            ),
            situacion,
            analisis,
            propuesta,
            mo.md(
                """
                #### **💡 Puntos clave a mencionar:**
                - **Conversion funnel analysis:** Free users → Trial → Paid
                - **Cohort analysis:** Retention patterns por segmento
                - **Feature usage tracking:** Qué funciones impulsan conversión
                - **Price sensitivity analysis:** Optimal pricing strategy
                - **Geographic differences:** Conversion rates por mercado
                """
            )
        ])
        
    elif pregunta_selector.value == "Estrategia IA y Datos":
        experiencia_ia = mo.ui.text_area(
            label="🤖 Tu experiencia con IA:",
            value="Mi TFM con Matrícula de Honor fue sobre IA aplicada a detección de riesgo en imágenes, usando deep learning...",
            rows=3
        )
        
        aplicacion_freepik = mo.ui.text_area(
            label="🎨 Cómo aplicarías IA en Freepik:",
            value="Implementaría modelos de recomendación personalizados basados en comportamiento del usuario, similar a mi experiencia con data marts en Avatel...",
            rows=4
        )
        
        metricas_ia = mo.ui.text_area(
            label="📈 Métricas para medir éxito IA:",
            value="CTR en recomendaciones, tiempo de búsqueda reducido, satisfaction score, adoption rate de herramientas IA...",
            rows=3
        )
        
        content = mo.vstack([
            mo.md(
                """
                ### **Pregunta: ¿Cómo medirías el impacto de las herramientas de IA en el negocio de Freepik?**
                
                #### **🤖 Framework IA + Business:**
                """
            ),
            experiencia_ia,
            aplicacion_freepik,
            metricas_ia,
            mo.md(
                """
                #### **🎯 KPIs específicos para IA en Freepik:**
                - **User Engagement:** Tiempo en plataforma con IA tools
                - **Content Quality:** User ratings de contenido generado por IA
                - **Efficiency Metrics:** Tiempo de creación reducido
                - **Revenue Impact:** Premium conversions por uso de IA
                - **Technical Metrics:** Model accuracy, response time
                """
            )
        ])
        
    elif pregunta_selector.value == "Expansión Internacional":
        experiencia_internacional = mo.ui.text_area(
            label="🌍 Tu experiencia con mercados internacionales:",
            value="En mi negocio propio analicé mercados locales vs turísticos, y en Avatel trabajé con clientes de diferentes regiones...",
            rows=3
        )
        
        analisis_expansion = mo.ui.text_area(
            label="🎯 Tu análisis de la expansión de Freepik:",
            value="La estrategia de Freepik en EEUU es inteligente - mercado maduro con alto poder adquisitivo. Mi approach sería...",
            rows=4
        )
        
        content = mo.vstack([
            mo.md(
                """
                ### **Pregunta: ¿Cómo abordarías el análisis de la expansión internacional de Freepik?**
                
                #### **🌎 Framework de expansión:**
                """
            ),
            experiencia_internacional,
            analisis_expansion,
            mo.md(
                """
                #### **📊 Métricas clave para expansión:**
                - **Market Penetration:** Users per capita por país
                - **Localization Impact:** Conversion rates contenido localizado
                - **Competitive Landscape:** Market share vs competidores locales
                - **Revenue Diversification:** Geographic revenue distribution
                - **Cultural Adaptation:** Content preference por región
                
                #### **🎯 Mercados prioritarios según datos:**
                1. **India:** Mayor tráfico actual
                2. **Brasil:** Segundo mercado
                3. **EEUU:** Expansión estratégica 2023
                4. **Europa:** Consolidación post-adquisiciones
                """
            )
        ])
        
    elif pregunta_selector.value == "Análisis Competitivo":
        analisis_competencia = mo.ui.text_area(
            label="🏆 Tu análisis de la competencia:",
            value="Freepik compite directamente con Shutterstock en stock media, pero su ventaja está en el modelo freemium y la integración de IA...",
            rows=4
        )
        
        ventajas_freepik = mo.ui.text_area(
            label="✅ Ventajas competitivas identificadas:",
            value="Modelo más accesible, suite integrada, IA avanzada, comunidad global, precio competitivo...",
            rows=3
        )
        
        content = mo.vstack([
            mo.md(
                """
                ### **Pregunta: ¿Cómo posicionarías a Freepik frente a sus competidores principales?**
                
                #### **🎯 Análisis competitivo:**
                """
            ),
            analisis_competencia,
            ventajas_freepik,
            mo.md(
                """
                #### **📊 Framework de análisis competitivo:**
                
                **vs Shutterstock:**
                - ✅ Precio más accesible
                - ✅ Modelo freemium
                - ⚠️ Menos contenido premium
                
                **vs Canva:**
                - ✅ Mejor biblioteca de assets
                - ✅ IA más avanzada
                - ⚠️ Menor facilidad de uso
                
                **vs Adobe Stock:**
                - ✅ Standalone platform
                - ✅ Precio competitivo
                - ⚠️ Menor integración profesional
                """
            )
        ])
        
    else:  # KPIs y Métricas Clave
        kpis_experiencia = mo.ui.text_area(
            label="📈 Tu experiencia con KPIs:",
            value="En Avatel desarrollé dashboards para tracking de KPIs financieros: tasa de impago, tiempo de cobranza, eficiencia operacional...",
            rows=3
        )
        
        kpis_freepik = mo.ui.text_area(
            label="🎯 KPIs que propondrías para Freepik:",
            value="User Acquisition Cost, Customer Lifetime Value, Monthly Active Users, Conversion Rate, Content Engagement Score...",
            rows=4
        )
        
        dashboard_propuesta = mo.ui.text_area(
            label="📊 Tu propuesta de dashboard:",
            value="Dashboard ejecutivo con métricas en tiempo real: MAU, conversions, revenue, geographic performance, AI tool adoption...",
            rows=3
        )
        
        content = mo.vstack([
            mo.md(
                """
                ### **Pregunta: ¿Qué KPIs implementarías para medir el éxito de Freepik?**
                
                #### **📊 Framework de KPIs:**
                """
            ),
            kpis_experiencia,
            kpis_freepik,
            dashboard_propuesta,
            mo.md(
                """
                #### **🎯 KPIs Críticos por Categoría:**
                
                **User Metrics:**
                - MAU (Monthly Active Users)
                - User Acquisition Cost (UAC)
                - User Retention Rate
                
                **Revenue Metrics:**
                - ARPU (Average Revenue Per User)
                - LTV (Lifetime Value)
                - Conversion Rate Free→Premium
                
                **Content Metrics:**
                - Download Volume
                - Content Engagement Score
                - Search Success Rate
                
                **Product Metrics:**
                - Feature Adoption Rate
                - AI Tool Usage
                - Platform Performance
                """
            )
        ])
    
    content
    return analisis, analisis_competencia, analisis_expansion, aplicacion_freepik, content, dashboard_propuesta, experiencia_ia, experiencia_internacional, kpis_experiencia, kpis_freepik, metricas_ia, propuesta, situacion, ventajas_freepik


@app.cell
def __(mo):
    # Elevator pitch específico para Freepik
    pitch_freepik = """Soy Business Analyst con 2+ años de experiencia en telecomunicaciones y finanzas, 
especializado en convertir datos complejos en insights accionables. Mi background único combina 
Master en Business Analytics, experiencia empresarial propia, y expertise técnico en Python, SQL y Tableau.

En Avatel, lideré proyectos de automatización que liberaron 20+ horas semanales y contribuyeron a 
mejorar KPIs financieros clave. Mi TFM con Matrícula de Honor aplicó IA a casos reales, alineado 
perfectamente con la estrategia de IA generativa de Freepik.

Me emociona la oportunidad de aplicar mi experiencia en modelos freemium, análisis predictivo y 
optimización de conversion funnels para impulsar el crecimiento de Freepik en mercados internacionales, 
especialmente aprovechando mi comprensión de métricas de suscripción y user journey analytics."""
    
    pitch_editor = mo.ui.text_area(
        value=pitch_freepik,
        label="🎨 Elevator Pitch personalizado para Freepik:",
        rows=10
    )
    
    mo.vstack([
        mo.md("## 🎯 **ELEVATOR PITCH - FREEPIK SPECIFIC**"),
        pitch_editor,
        mo.md(f"**Palabras:** {len(pitch_freepik.split())} | **Tiempo:** ~{len(pitch_freepik.split()) * 0.5:.0f} segundos")
    ])
    return pitch_editor, pitch_freepik


@app.cell
def __(mo):
    # Preguntas inteligentes para hacer a Freepik
    mo.md(
        """
        ## ❓ **PREGUNTAS ESTRATÉGICAS PARA FREEPIK**
        
        ### **🎯 Para C-level/Founders:**
        - ¿Cuál es la visión a 5 años para la suite de IA de Freepik?
        - ¿Cómo ven el balance entre contenido generado por IA vs contenido de creadores?
        - ¿Qué mercados geográficos son prioritarios para 2024-2025?
        - ¿Cómo miden el éxito de las adquisiciones recientes (Videvo, Iconfinder)?
        
        ### **🔧 Para Technical/Product Leaders:**
        - ¿Qué herramientas de analytics y BI utilizan actualmente?
        - ¿Cómo miden la performance de los algoritmos de recomendación?
        - ¿Qué challenges tienen con la integración de datos cross-platform?
        - ¿Cómo balancean la personalización vs la serendipity en recommendations?
        
        ### **📊 Para Data/Analytics Team:**
        - ¿Qué KPIs consideran más críticos para el business?
        - ¿Cómo estructuran el data warehouse con múltiples productos?
        - ¿Qué herramientas usan para A/B testing y experimentation?
        - ¿Cómo miden el impacto de las features de IA en user engagement?
        
        ### **🌍 Para International Expansion:**
        - ¿Qué aprendizajes han tenido de la expansión en EEUU?
        - ¿Cómo adaptan el contenido y pricing por mercado?
        - ¿Qué métricas usan para evaluar market fit en nuevos países?
        """
    )
    return


@app.cell
def __(mo):
    # Checklist específico para Freepik
    checklist_freepik = mo.ui.array([
        mo.ui.checkbox(label="✅ Investigación profunda sobre Freepik (historia, productos, estrategia)"),
        mo.ui.checkbox(label="✅ Análisis de competidores (Shutterstock, Canva, Adobe Stock)"),
        mo.ui.checkbox(label="✅ Comprensión del modelo freemium y métricas SaaS"),
        mo.ui.checkbox(label="✅ Conocimiento de herramientas IA de Freepik (Pikaso, Wepik)"),
        mo.ui.checkbox(label="✅ Preparación de ejemplos STAR específicos"),
        mo.ui.checkbox(label="✅ Elevator pitch adaptado a Freepik"),
        mo.ui.checkbox(label="✅ Preguntas inteligentes preparadas"),
        mo.ui.checkbox(label="✅ Portfolio/ejemplos de análisis de datos"),
        mo.ui.checkbox(label="✅ Conocimiento de mercados internacionales (India, Brasil, EEUU)"),
        mo.ui.checkbox(label="✅ Comprensión de KPIs de content platforms"),
    ])
    
    progreso_freepik = len([c.value for c in checklist_freepik.value if c.value]) / 10 * 100
    
    mo.vstack([
        mo.md(
            f"""
            ## ✅ **CHECKLIST PREPARACIÓN FREEPIK**
            
            **Progreso:** {progreso_freepik:.0f}% completo
            
            {'🎨 ¡Listo para Freepik!' if progreso_freepik == 100 else '🟡 Casi listo' if progreso_freepik >= 70 else '🔴 Necesitas más preparación'}
            """
        ),
        checklist_freepik,
        mo.md(
            f"""
            ### **Estado actual:**
            - **Completado:** {len([c.value for c in checklist_freepik.value if c.value])}/10 tareas
            - **Pendiente:** {10 - len([c.value for c in checklist_freepik.value if c.value])} tareas
            """
        )
    ])
    return checklist_freepik, progreso_freepik


@app.cell
def __(mo):
    # Notas específicas para Freepik
    notas_freepik = mo.ui.text_area(
        placeholder="Información adicional sobre Freepik, noticias recientes, contactos, etc.",
        label="🎨 Notas específicas sobre Freepik:",
        rows=4
    )
    
    estrategia_personal = mo.ui.text_area(
        placeholder="Tu estrategia personal para destacar en Freepik...",
        label="🎯 Tu estrategia para esta entrevista:",
        rows=4
    )
    
    puntos_clave = mo.ui.text_area(
        placeholder="Puntos clave que NO quieres olvidar mencionar...",
        label="⭐ Puntos clave a recordar:",
        rows=3
    )
    
    mo.vstack([
        mo.md("## 📝 **NOTAS PERSONALES - FREEPIK**"),
        notas_freepik,
        estrategia_personal,
        puntos_clave
    ])
    return estrategia_personal, notas_freepik, puntos_clave


@app.cell
def __(mo):
    # Resumen final específico para Freepik
    mo.md(
        """
        ---
        
        ## 🚀 **¡ÉXITO EN TU ENTREVISTA CON FREEPIK!**
        
        ### **🎯 Tu propuesta de valor única para Freepik:**
        - **Experiencia híbrida:** Técnico + Business + Financiero
        - **IA aplicada:** TFM con Matrícula de Honor alineado con estrategia IA
        - **Modelos de suscripción:** Experiencia en Avatel con conversion analytics
        - **Visión internacional:** Comprensión de expansión geográfica
        - **Data-driven mindset:** Resultados medibles y KPIs claros
        
        ### **🎨 Recuerda el contexto Freepik:**
        - **Suite creativa IA** (no solo banco de imágenes)
        - **52M+ usuarios** globales que necesitan insights
        - **Expansión agresiva** en EEUU y otros mercados
        - **Modelo freemium** que requiere optimization continua
        - **Cultura de innovación** y crecimiento rápido
        
        ### **📱 Recursos finales:**
        - **CV actualizado**: `index.html`
        - **Esta app**: Para repaso final
        - **Portfolio**: Ejemplos de análisis y dashboards
        
        **¡Vas a brillar en Freepik! 🎨✨**
        """
    )
    return


if __name__ == "__main__":
    app.run()
