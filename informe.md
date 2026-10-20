# Informe de Pruebas de Carga y Optimización

## Objetivo

Evaluar el rendimiento del modelo local Gemma4:E4B utilizando pruebas de carga concurrentes con asyncio y aiohttp.

## Entorno

- Ollama
- Gemma4:E4B
- Python
- aiohttp
- asyncio
- psutil

## Escenarios probados

- 5 usuarios concurrentes
- 10 usuarios concurrentes
- 20 usuarios concurrentes

## Resultados antes de optimizar

| Usuarios | Tiempo medio (s) | Errores |
|-----------|-----------|-----------|
| 5 | 199.79 | 3 |
| 10 | 221.49 | 9 |
| 20 | 195.57 | 19 |

## Cuellos de botella detectados

El principal cuello de botella fue la CPU, alcanzando valores cercanos al 100% durante todas las pruebas.

La memoria RAM se mantuvo estable alrededor del 50%, por lo que no se identificó como limitación principal.

## Optimizaciones aplicadas

### Optimización 1

Reducción de la temperatura:

```json
"temperature": 0.2
