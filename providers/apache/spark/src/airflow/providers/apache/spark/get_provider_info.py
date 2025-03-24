# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# NOTE! THIS FILE IS AUTOMATICALLY GENERATED AND WILL BE OVERWRITTEN!
#
# IF YOU WANT TO MODIFY THIS FILE, YOU SHOULD MODIFY THE TEMPLATE
# `get_provider_info_TEMPLATE.py.jinja2` IN the `dev/breeze/src/airflow_breeze/templates` DIRECTORY


def get_provider_info():
    return {
        "package-name": "apache-airflow-providers-apache-spark",
        "name": "Apache Spark",
        "description": "`Apache Spark <https://spark.apache.org/>`__\n",
        "state": "ready",
        "source-date-epoch": 1741508415,
        "versions": [
            "5.0.1",
            "5.0.0",
            "4.11.3",
            "4.11.2",
            "4.11.1",
            "4.11.0",
            "4.10.0",
            "4.9.0",
            "4.8.2",
            "4.8.1",
            "4.8.0",
            "4.7.2",
            "4.7.1",
            "4.7.0",
            "4.6.0",
            "4.5.0",
            "4.4.0",
            "4.3.0",
            "4.2.0",
            "4.1.5",
            "4.1.4",
            "4.1.3",
            "4.1.2",
            "4.1.1",
            "4.1.0",
            "4.0.1",
            "4.0.0",
            "3.0.0",
            "2.1.3",
            "2.1.2",
            "2.1.1",
            "2.1.0",
            "2.0.3",
            "2.0.2",
            "2.0.1",
            "2.0.0",
            "1.0.3",
            "1.0.2",
            "1.0.1",
            "1.0.0",
        ],
        "integrations": [
            {
                "integration-name": "Apache Spark",
                "external-doc-url": "https://spark.apache.org/",
                "how-to-guide": ["/docs/apache-airflow-providers-apache-spark/operators.rst"],
                "logo": "/docs/integration-logos/spark.png",
                "tags": ["apache"],
            }
        ],
        "operators": [
            {
                "integration-name": "Apache Spark",
                "python-modules": [
                    "airflow.providers.apache.spark.operators.spark_jdbc",
                    "airflow.providers.apache.spark.operators.spark_sql",
                    "airflow.providers.apache.spark.operators.spark_submit",
                ],
            }
        ],
        "hooks": [
            {
                "integration-name": "Apache Spark",
                "python-modules": [
                    "airflow.providers.apache.spark.hooks.spark_connect",
                    "airflow.providers.apache.spark.hooks.spark_jdbc",
                    "airflow.providers.apache.spark.hooks.spark_jdbc_script",
                    "airflow.providers.apache.spark.hooks.spark_sql",
                    "airflow.providers.apache.spark.hooks.spark_submit",
                ],
            }
        ],
        "connection-types": [
            {
                "hook-class-name": "airflow.providers.apache.spark.hooks.spark_connect.SparkConnectHook",
                "connection-type": "spark_connect",
            },
            {
                "hook-class-name": "airflow.providers.apache.spark.hooks.spark_jdbc.SparkJDBCHook",
                "connection-type": "spark_jdbc",
            },
            {
                "hook-class-name": "airflow.providers.apache.spark.hooks.spark_sql.SparkSqlHook",
                "connection-type": "spark_sql",
            },
            {
                "hook-class-name": "airflow.providers.apache.spark.hooks.spark_submit.SparkSubmitHook",
                "connection-type": "spark",
            },
        ],
        "task-decorators": [
            {
                "class-name": "airflow.providers.apache.spark.decorators.pyspark.pyspark_task",
                "name": "pyspark",
            }
        ],
        "dependencies": [
            "apache-airflow>=2.9.0",
            "apache-airflow-providers-common-compat>=1.5.0",
            "pyspark>=3.1.3",
            "grpcio-status>=1.59.0",
        ],
        "optional-dependencies": {"cncf.kubernetes": ["apache-airflow-providers-cncf-kubernetes>=7.4.0"]},
        "devel-dependencies": [],
    }
