# SES Dashboard v1.0.2

SES Dashboard es una plataforma de datos enlazados desarrollada para gestionar información sobre las plataformas marinas (boyas, animales instrumentados, etc.) del Atlántico Sur, específicamente de la colonia de elefantes marinos del sur (Mirounga leonina, Linnaeus 1758) en la Península Valdés, Patagonia, Argentina. Esta aplicación integra datos abiertos enlazados (Linked Open Data, LOD), proporcionando una herramienta robusta para la visualización y análisis de datos marinos.

## Características

- **Análisis de plataformas**: Visualiza estadísticas de inmersiones, profundidad máxima, mínima y promedio, y el número total de plataformas e inmersiones.
- **Sensores y plataformas**: Consulta información detallada sobre los sensores y plataformas, incluyendo fechas de colocación y recuperación, tipo de sensor, fabricante y modelo.
- **Análisis de inmersiones**: Analiza inmersiones específicas por plataforma, visualizando datos de profundidad, duración, temperatura del fondo y superficie.
- **Datos de boyas**: Consulta y visualiza datos de boyas, incluyendo altura significativa de olas, velocidad del viento y temperaturas.
- **Análisis de clusters**: Realiza análisis de clusters utilizando el algoritmo DBSCAN para identificar patrones en los datos geoespaciales.
- **Estadísticas de censo**: Visualiza el censo de especies por año y categoría.
- **Datos enlazados**: Accede a información de especies desde puntos de acceso BiGe-Onto y Wikidata, y consulta enlaces a bases de datos de biodiversidad y NCBI Taxonomy.

## Requisitos

Para ejecutar esta aplicación, asegúrate de tener instalados los siguientes paquetes de R:

```r
library(flexdashboard)
library(knitr)
library(stringr)
library(DT)
library(rpivotTable)
library(ggplot2)
library(plotly)
library(plyr)
library(dplyr)
library(highcharter)
library(ggvis)
library(leaflet)
library(dbscan)
library(factoextra)
library(shiny)
library(mregions)
library(sf)
library(zoo)
library(shinyWidgets)
library(tidyr)
library(reticulate)
```
## Archivos de datos

La aplicación utiliza varios archivos CSV para cargar los datos necesarios:

- `ALLplatform.csv`
- `Instruments.csv`
- `censusByCategories.csv`
- `papers.csv`
- `data_site_buoy.csv`

## Uso

Para ejecutar la aplicación, sigue estos pasos:

1. Clona el repositorio en tu máquina local.
2. Asegúrate de tener los paquetes de R mencionados anteriormente instalados.
3. Ejecuta el script principal `SES_Dashboard.Rmd` utilizando RStudio o cualquier entorno compatible con R Markdown.

```r
rmarkdown::run("DiveAnalysisDashboard.Rmd")
```
## Integración con datos abiertos enlazados (LOD)

SES Dashboard sigue los principios de los datos abiertos enlazados, permitiendo la reutilización de datos y ampliando el rango de posibilidades para la investigación y la toma de decisiones en la conservación de especies.

## Licencia

Este proyecto está licenciado bajo los términos de la [MIT License](LICENSE).

## Contribuciones

¡Se agradecen las contribuciones! Si tienes sugerencias o encuentras algún problema, no dudes en abrir un issue o enviar un pull request.

## Contacto

Para más información, puedes [contactarme en Twitter](https://twitter.com/MarcosdZarate84).
