#!/usr/bin/env python3
import pymysql.cursors
from ruamel.yaml import YAML
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
            SELECT name,
                org_id AS orgId,
                version,
                type,
                access,
                url,
                password,
                user,
                `database`,
                basic_auth AS basicAuth,
                basic_auth_user AS basicAuthUser,
                basic_auth_password AS basicAuthPassword,
                is_default AS isDefault,
                json_data AS jsonData,
                created,
                updated,
                with_credentials AS withCredentials,
                secure_json_data AS secureJsonData
            FROM `data_source`
            WHERE TYPE = 'grafana-influxdb-flux-datasource'
            ORDER BY created
            LIMIT 1
        """
        cursor.execute(sql)
        result = cursor.fetchone()
        yaml = YAML()
        for key, value in list(result.items()):
            if type(value) == str:
                if "{}" == value or "" == value:
                    del result[key]
        if 'jsonData' in result:
            result['jsonData'] = json.loads(result['jsonData'])
        if 'secureJsonData' in result:
            result['secureJsonData'] = json.loads(result['secureJsonData'])
        yaml.dump([result], sys.stdout)
finally:
    connection.close()
