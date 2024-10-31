#!/bin/bash
set -e

# Wait for the database to be ready
until sqlplus -L sys/${ORACLE_PWD}@//localhost:1521/XE as sysdba <<EOF
exit;
EOF
do
  echo "Waiting for Oracle database to be ready..."
  sleep 2
done

# Run the setup script
sqlplus -L sys/${ORACLE_PWD}@//localhost:1521/XE as sysdba @/docker-entrypoint-initdb.d/setup.sql

echo "Database initialization completed."