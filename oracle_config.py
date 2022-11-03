import os

import oracledb

user = os.environ.get("DB_USER", "SYSTEM")
password = os.environ.get("DB_PASSWORD", "SysPassword1")
dsn = os.environ.get("CONNECT_STRING", "10.0.2.26:1522/xe")

