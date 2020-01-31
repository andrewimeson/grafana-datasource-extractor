#!/usr/bin/env python3
import pymysql.cursors
import sys
import json as json
# TODO: Support multiple database types (SQLite, etc.)
# TODO: Add parameterization for which data sources to dump
# TODO: Add support for grabbing more than one data source at a time

connection = pymysql.connect(
    host='',
    user='',
    password='',
    db='grafanadb',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with connection.cursor() as cursor:
        sql = """
        SELECT name, type, access, url, json_data AS jsonData, version
        FROM `data_source` 
        WHERE type = 'grafana-influxdb-flux-datasource'
        ORDER BY created LIMIT 1
        """
        cursor.execute(sql)
        result = cursor.fetchone()
        result['jsonData'] = json.loads(result['jsonData'])
        print('- name:', result["name"])
        for key, value in result.items():
            if key == "name":
                pass
            elif key == "jsonData":
                print("  " + key + ":")
                for dataKey, dataValue in value.items():
                    print("    " + dataKey + ": " + str(dataValue))
            else:
                print("  " + key + ": " + str(value))
finally:
    connection.close()
