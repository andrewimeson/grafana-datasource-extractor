# Grafana Datasource Extractor
This is a Python script for extracting the datasource configuration from the
Grafana database and outputting it in the YAML format needed to make use of the
[provisioning feature in
Grafana](https://grafana.com/docs/grafana/latest/administration/provisioning/#datasources)

*Warning:* This is a very basic and very bad script. This is my first Python
script and it was written to meet some very basic MVP criteria. It's probably
not in a very useful state without modification to match the particular
datasource you are trying to extract, at which point you've probably spent more
time than this has saved.

# Requirements
1. Python 3.x
2. A Grafana system using MySQL/MariaDB as the database for configuration
