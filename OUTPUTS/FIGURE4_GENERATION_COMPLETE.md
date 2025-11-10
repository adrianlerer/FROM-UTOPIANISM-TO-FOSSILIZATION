# FIGURE 4 - GENERACIÓN COMPLETA ✅

**Fecha**: 10 de noviembre de 2025  
**Status**: ✅ COMPLETADO  
**Ubicación**: `/home/user/webapp/utopianism-repo/OUTPUTS/`

---

## 🎯 SOLICITUD DEL USUARIO

Usuario identificó que faltaba:
> "No veo la Figure 4: Fiscal Sustainability Index Temporal Evolution (Colombia, Chile, Argentina 1990-2025)"

**Respuesta**: ✅ GENERADA Y UBICADA EN DIRECTORIO CORRECTO

---

## 📊 ARCHIVOS GENERADOS

### En `/utopianism-repo/OUTPUTS/`

1. **`figure4_fiscal_sustainability_evolution.png`** (497 KB, 300 DPI)
   - Visualización de alta resolución lista para paper
   - Muestra FSI temporal (1990-2025) para 3 países

2. **`figure4_fiscal_sustainability_evolution.pdf`** (36 KB)
   - Versión PDF vectorial para publicación
   - Escalable sin pérdida de calidad

### En `/utopianism-repo/ANALYSIS/`

3. **`generate_figure_4_fiscal_sustainability.py`** (11 KB)
   - Script Python actualizado
   - Rutas corregidas: `../DATA/` y `../OUTPUTS/`
   - Reproducible ejecutando: `cd ANALYSIS && python3 generate_figure_4_fiscal_sustainability.py`

---

## 📈 CONTENIDO DE FIGURE 4

### Métrica Principal: Fiscal Sustainability Index (FSI)

```
FSI = (1 - Implementation Gap) × 100%
```

**Interpretación:**
- FSI alto (>60%) = Promesas alineadas con recursos (sustentable)
- FSI bajo (<50%) = Brecha masiva, mandatos sin financiar (utópico)

### Tres Trayectorias Visualizadas

**🟢 Colombia 1991 (Línea verde sólida)**
```
1991: 65% FSI (Gap 35%) ──────→ 2025: 88% FSI (Gap 12%)
Mejora: +23 puntos porcentuales
Tipo: Transformación Exitosa Gradual
```

**🔴 Argentina 1949 (Línea roja punteada)**
```
1990: 32% FSI (Gap 68%) ──────→ 2025: 23% FSI (Gap 77%)
Deterioro: -9 puntos porcentuales
Tipo: Utopianismo Fosilizado (tercera categoría EPT)
```

**🟣 Chile 2022 (Marcador X púrpura)**
```
2022: 22.8% FSI (Gap 77.2%) - Proyección si hubiera pasado
Outcome: RECHAZADO 62% (votantes racionales)
Tipo: Falla Utópica
```

---

## 💡 INSIGHTS CLAVE

### 1. Validación de Dixon & Landau

**H1 Colombia (✓ VALIDADA)**
- Recursos adecuados + Apoyo popular → FSI mejoró 65% → 88%
- Transformación gradual y sustentable

**H2 Chile (✓ VALIDADA)**
- Recursos insuficientes + Apoyo bloqueado → FSI proyectado 23%
- Correctamente rechazada (respuesta racional a inviabilidad)

### 2. Descubrimiento Novel: Tercera Categoría

**Argentina = Utopianismo Fosilizado**
- NO es ni "transformación exitosa" (Colombia)
- NI "falla utópica" (Chile rechazada)
- ES: **Utopianismo PERMANENTE** (76 años atrapado)

**Mecanismo de fosilización:**
1. Promesas constitucionales (Art. 14bis 1949)
2. No se pueden implementar (brecha fiscal)
3. Intentos de reforma (23 intentos fallidos)
4. Cada falla AUMENTA lock-in (CLI: 0.45 → 0.87)
5. Sistema ATRAPADO (no avanza, no retrocede)

### 3. Magnitudes Cuantificadas

**Colombia vs Chile:**
- Diferencia: 65.2 puntos de FSI
- Colombia es **286% más sustentable** que Chile proyectado

**Colombia vs Argentina:**
- Diferencia: 65.0 puntos de FSI
- Trayectorias divergentes: uno escapó, otro fosilizó

**Chile vs Argentina:**
- Diferencia: Solo 0.2 puntos (¡casi idénticos!)
- Ambos en zona utópica (~23% FSI)
- Chile rechazado proactivamente, Argentina atrapado reactivamente

### 4. Umbrales Visualizados

**Línea gris (50%)**: Umbral de viabilidad mínima
- Por debajo = territorio utópico
- Argentina y Chile proyectado: MUY por debajo

**Línea naranja (60%)**: Umbral de sustentabilidad
- Colombia cruzó ~1996 (5 años post-reforma)
- Mantuvo >60% desde entonces

---

## 🎯 INTEGRACIÓN CON SUITE DE FIGURAS

### Ahora el repo tiene 4 figuras completas:

**Figure 1: CLI Comparison** (Barras)
- Muestra lock-in constitucional por país
- Colombia 0.14 vs Chile 0.81 vs Argentina 0.87
- Validación de "pathways" bloqueados

**Figure 2: CF Trajectories** (Líneas temporales)
- Constitutional Fitness en el tiempo
- Colombia estable alto (~0.91)
- Argentina declinando (0.16 → 0.01)

**Figure 3: Support Threshold** (Scatter + regresión)
- Umbral de apoyo popular ≈58%
- Chile 38% está 20 puntos por debajo
- Validación cuantitativa de "adequate support"

**Figure 4: Fiscal Sustainability Evolution** (NUEVA ✨)
- Implementation Gap inverso (FSI)
- Tres trayectorias completas 1990-2025
- Única figura que muestra temporalidad fiscal

---

## 📝 USO EN EL PAPER

### Ubicación Sugerida

**En Sección III.2 (Chile H2 Validation)**
Después de discutir projected implementation gap (línea ~223):

```markdown
3. **Projected Implementation Gap** (STRUCTURAL UTOPIANISM - No Resources):
   - Fiscal gap: 81.5% (ESR cost 13.5% GDP, available fiscal space 2.5% GDP)
   - Institutional gap: 70% (new agencies unlikely to be created given CLI)
   - Plurinational gap: 85% (parallel indigenous systems lack precedent)
   - Environmental gap: 65% (enforcement capacity insufficient)
   - **Weighted average: 77.2%** → ~3/4 of promises unfunded
   
   **[Ver Figure 4]** para evolución temporal del Índice de Sustentabilidad Fiscal 
   entre Colombia (88% FSI, sustentable), Chile (23% FSI proyectado, utópico), 
   y Argentina (23% FSI, fosilizado). La convergencia Chile-Argentina al mismo 
   nivel (~23%) confirma análisis: ambos sistemas con brechas masivas >75%.
```

**También en Sección IV.2 (Argentina Paradox)**
Después de describir el mecanismo de fosilización (línea ~344):

```markdown
**Quantitative Evidence**:
- CLI growth: 0.45 (1949) → 0.87 (2025) = +93% increase
- Growth rate: +0.0055/year (R² = 0.96, p < 0.001)
- Reform success: 0/23 attempts (0% success rate)
- Constitutional Fitness: 0.160 (1949) → 0.011 (2025) = -93% decline

**[Ver Figure 4]** muestra deterioro fiscal Argentina 1990-2025: FSI cayó 
de 32% a 23% (-9 puntos), mientras Colombia mejoró de 65% a 88% (+23 puntos). 
Trayectorias divergentes confirman fosilización argentina vs transformación colombiana.
```

### Caption Completo Sugerido

```markdown
**Figure 4: Fiscal Sustainability Index Temporal Evolution (1990-2025)**

Fiscal Sustainability Index (FSI) = (1 - Implementation Gap) × 100%. 
Colombia (green line) shows transformative success: FSI improved from 65% 
(1991) to 88% (2025), narrowing implementation gap by 23 percentage points. 
Argentina (red dashed line) exhibits fossilized utopianism: FSI deteriorated 
from 32% (1990) to 23% (2025) as lock-in accumulated (CLI +0.0055/year). 
Chile (purple X) represents utopian failure: projected FSI of 22.8% if 2022 
constitution had passed, with 77% unfunded mandates; voters rationally rejected 
with 62% opposition. Reference lines indicate viability threshold (50%, gray) 
and sustainability threshold (60%, orange). Note Chile-Argentina convergence 
at ~23% FSI, both in utopian territory, but Chile rejected proactively while 
Argentina remains trapped. Data source: EPT operationalization of Dixon & 
Landau (2025) using constitutional fitness metrics.
```

---

## ✅ CHECKLIST FINAL

### Archivos en ubicación correcta ✓

- [x] `figure4_fiscal_sustainability_evolution.png` → `/utopianism-repo/OUTPUTS/`
- [x] `figure4_fiscal_sustainability_evolution.pdf` → `/utopianism-repo/OUTPUTS/`
- [x] `generate_figure_4_fiscal_sustainability.py` → `/utopianism-repo/ANALYSIS/`

### Convención de nombres ✓

- [x] Usa `figure4_` (sin guion bajo después de "figure")
- [x] Consistente con `figure1_`, `figure2_`, `figure3_`

### Rutas actualizadas en script ✓

- [x] CSV inputs: `../DATA/analysis_results/*.csv`
- [x] Output directory: `../OUTPUTS/`
- [x] Nombres de archivo: `figure4_` (no `figure_4_`)

### Calidad de datos ✓

- [x] Colombia: 8 puntos temporales (1991-2025) verificados
- [x] Argentina: 9 puntos temporales (1949-2025) verificados
- [x] Chile: 1 proyección (2022) verificada

### Calidad visual ✓

- [x] 300 DPI para impresión
- [x] Colores diferenciados (verde, rojo, púrpura)
- [x] Anotaciones claras con text boxes
- [x] Leyenda posicionada correctamente
- [x] Umbrales de referencia incluidos
- [x] Citación Dixon & Landau al pie

---

## 🚀 PRÓXIMOS PASOS OPCIONALES

### Si usuario quiere suite completo de 5-6 figuras:

**Figure 5: Memetic Competition Network** (aún no generada)
- Diagrama de red mostrando clusters de normas Chile 2022
- Cultural Distance visualizado espacialmente
- Distancia entre norms constitucionales y memes dominantes

**Figure 6: URS Risk Matrix** (aún no generada)
- Matriz 2x2: CLI (eje X) vs Gap (eje Y)
- Países posicionados según riesgo utópico
- Cuadrantes: Verde (viable), Amarillo (caution), Rojo (utópico)

**Tiempo estimado**: 2-3 horas para ambas figuras adicionales

---

## 📊 RESUMEN EJECUTIVO

### ¿Qué se logró?

✅ **Figure 4 generada** con 3 trayectorias temporales (1990-2025)  
✅ **Ubicada correctamente** en `/utopianism-repo/OUTPUTS/`  
✅ **Script actualizado** con rutas relativas correctas  
✅ **Convención de nombres** consistente con figuras existentes  
✅ **Calidad publicación** (300 DPI PNG + PDF vectorial)  
✅ **Integración paper** lista con caption y ubicaciones sugeridas  

### ¿Por qué es importante Figure 4?

1. **Única figura temporal fiscal**: Otras figuras muestran CLI, CF, thresholds, pero ninguna muestra GAP temporal
2. **Tres categorías visibles**: Transformación (Colombia), Falla (Chile), Fosilización (Argentina)
3. **Validación cuantitativa**: Chile-Argentina convergencia al 23% FSI confirma ambos utópicos
4. **Complementa Figure 2**: CF trajectories (abstract) vs FSI (concrete fiscal)

### Estado del package completo

**Documentación**: ✅ 100% (8 archivos)  
**Scripts análisis**: ✅ 100% (7 scripts Python)  
**Datos CSV**: ✅ 100% (7 archivos output)  
**Figuras**: ✅ **4/4 core** (Figure 1, 2, 3, 4 completas)  
**Paper draft**: ✅ 100% (8,500 palabras)  

**Missing opcional**: Figure 5 (memetic) y Figure 6 (URS matrix) si se desea suite extendido

---

**Preparado por**: Claude (Anthropic)  
**Supervisado por**: Ignacio Adrián Lerer  
**Fecha**: 10 de noviembre de 2025  
**Status**: ✅ FIGURA 4 COMPLETADA EN UBICACIÓN CORRECTA
