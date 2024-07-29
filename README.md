# SES Dashboard v1.0.2

SES Dashboard is a linked data platform developed to manage information about marine platforms (buoys, instrumented animals, etc.) in the South Atlantic, specifically the southern elephant seal colony (Mirounga leonina, Linnaeus 1758) at Península Valdés, Patagonia, Argentina. This application integrates Linked Open Data (LOD), providing a robust tool for marine data visualization and analysis.

## Features

- **Platform analysis**: Visualize dive statistics, maximum, minimum, and average depth, and the total number of platforms and dives.
- **Sensors and platforms**: Query detailed information about sensors and platforms, including placement and recovery dates, sensor type, manufacturer, and model.
- **Dive analysis**: Analyze specific dives by platform, visualizing depth data, duration, bottom and surface temperature.
- **Buoy data**: Query and visualize buoy data, including significant wave height, wind speed, and temperatures.
- **Cluster analysis**: Perform cluster analysis using the DBSCAN algorithm to identify patterns in geospatial data.
- **Census statistics**: Visualize species census by year and category.
- **Linked data**: Access species information from BiGe-Onto and Wikidata access points, and query links to biodiversity databases and NCBI Taxonomy.

## Requirements

To run this application, make sure you have the following R packages installed:

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
## Data Files

The application uses several CSV files to load the necessary data:

- `ALLplatform.csv`
- `Instruments.csv`
- `censusByCategories.csv`
- `papers.csv`
- `data_site_buoy.csv`

## Usage

To run the application, follow these steps:
1. Clone the repository to your local machine.
2. Make sure you have the aforementioned R packages installed.
3. Run the main script `SES_Dashboard.Rmd` using RStudio or any R Markdown compatible environment.

```r
rmarkdown::run("DiveAnalysisDashboard.Rmd")
```
## Linked Open Data (LOD) Integration

SES Dashboard follows the principles of Linked Open Data, allowing data reuse and expanding the range of possibilities for research and decision-making in species conservation.

## Licence

This project is licensed under the terms of the [MIT License](LICENSE).

## Contact

Contributions are welcome! If you have suggestions or find any issues, feel free to open an issue or send a pull request.

## Contacto

For more information, you can [contact me on Twitter](https://twitter.com/MarcosdZarate84).
