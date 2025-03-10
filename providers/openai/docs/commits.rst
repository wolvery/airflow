
 .. Licensed to the Apache Software Foundation (ASF) under one
    or more contributor license agreements.  See the NOTICE file
    distributed with this work for additional information
    regarding copyright ownership.  The ASF licenses this file
    to you under the Apache License, Version 2.0 (the
    "License"); you may not use this file except in compliance
    with the License.  You may obtain a copy of the License at

 ..   http://www.apache.org/licenses/LICENSE-2.0

 .. Unless required by applicable law or agreed to in writing,
    software distributed under the License is distributed on an
    "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.

 .. NOTE! THIS FILE IS AUTOMATICALLY GENERATED AND WILL BE OVERWRITTEN!

 .. IF YOU WANT TO MODIFY THIS FILE, YOU SHOULD MODIFY THE TEMPLATE
    `PROVIDER_COMMITS_TEMPLATE.rst.jinja2` IN the `dev/breeze/src/airflow_breeze/templates` DIRECTORY

 .. THE REMAINDER OF THE FILE IS AUTOMATICALLY GENERATED. IT WILL BE OVERWRITTEN!

Package apache-airflow-providers-openai
------------------------------------------------------

`OpenAI <https://platform.openai.com/docs/introduction>`__


This is detailed commit list of changes for versions provider package: ``openai``.
For high-level changelog, see :doc:`package information including changelog <index>`.



1.5.1
.....

Latest change: 2025-02-16

==================================================================================================  ===========  ==============================================================================
Commit                                                                                              Committed    Subject
==================================================================================================  ===========  ==============================================================================
`4d5846f58f <https://github.com/apache/airflow/commit/4d5846f58fe0de9b43358c0be75dd72e968dacc4>`__  2025-02-16   ``Move provider_tests to unit folder in provider tests (#46800)``
`e027457a24 <https://github.com/apache/airflow/commit/e027457a24d0c6235bfed9c2a8399f75342e82f1>`__  2025-02-15   ``Removed the unused provider's distribution (#46608)``
`240a147fcd <https://github.com/apache/airflow/commit/240a147fcd7f4ccec51c22a2f5bccc1fd031f8df>`__  2025-01-26   ``refactor(providers/openai): move openai provider to new structure (#46099)``
`f616c62209 <https://github.com/apache/airflow/commit/f616c62209d6b51d293ecf6f5c900f89a7fdc3a3>`__  2025-01-15   ``AIP-72: Support better type-hinting for Context dict in SDK  (#45583)``
==================================================================================================  ===========  ==============================================================================

1.5.0
.....

Latest change: 2024-12-20

==================================================================================================  ===========  ========================================================================================
Commit                                                                                              Committed    Subject
==================================================================================================  ===========  ========================================================================================
`2723508345 <https://github.com/apache/airflow/commit/2723508345d5cf074aeb673955ce72996785f2bc>`__  2024-12-20   ``Prepare docs for Nov 1st wave of providers Dec 2024 (#45042)``
`4b38bed76c <https://github.com/apache/airflow/commit/4b38bed76c1ea5fe84a6bc678ce87e20d563adc0>`__  2024-12-16   ``Bump min version of Providers to 2.9 (#44956)``
`1275fec92f <https://github.com/apache/airflow/commit/1275fec92fd7cd7135b100d66d41bdcb79ade29d>`__  2024-11-24   ``Use Python 3.9 as target version for Ruff & Black rules (#44298)``
`a53d9f6d25 <https://github.com/apache/airflow/commit/a53d9f6d257f193ea5026ba4cd007d5ddeab968f>`__  2024-11-14   ``Prepare docs for Nov 1st wave of providers (#44011)``
`857ca4c06c <https://github.com/apache/airflow/commit/857ca4c06c9008593674cabdd28d3c30e3e7f97b>`__  2024-10-09   ``Split providers out of the main "airflow/" tree into a UV workspace project (#42505)``
==================================================================================================  ===========  ========================================================================================

1.4.0
.....

Latest change: 2024-09-21

==================================================================================================  ===========  ===============================================================================
Commit                                                                                              Committed    Subject
==================================================================================================  ===========  ===============================================================================
`7628d47d04 <https://github.com/apache/airflow/commit/7628d47d0481966d9a9b25dfd4870b7a6797ebbf>`__  2024-09-21   ``Prepare docs for Sep 1st wave of providers (#42387)``
`00e73e6089 <https://github.com/apache/airflow/commit/00e73e6089f2d54a38944ec47303aa00f9d211d7>`__  2024-08-22   ``feat(providers/openai): support batch api in hook/operator/trigger (#41554)``
==================================================================================================  ===========  ===============================================================================

1.3.0
.....

Latest change: 2024-08-19

==================================================================================================  ===========  =======================================================================
Commit                                                                                              Committed    Subject
==================================================================================================  ===========  =======================================================================
`75fb7acbac <https://github.com/apache/airflow/commit/75fb7acbaca09a040067f0a5a37637ff44eb9e14>`__  2024-08-19   ``Prepare docs for Aug 2nd wave of providers (#41559)``
`fcbff15bda <https://github.com/apache/airflow/commit/fcbff15bda151f70db0ca13fdde015bace5527c4>`__  2024-08-12   ``Bump minimum Airflow version in providers to Airflow 2.8.0 (#41396)``
==================================================================================================  ===========  =======================================================================

1.2.2
.....

Latest change: 2024-06-22

==================================================================================================  ===========  ==================================================
Commit                                                                                              Committed    Subject
==================================================================================================  ===========  ==================================================
`6e5ae26382 <https://github.com/apache/airflow/commit/6e5ae26382b328e88907e8301d4b2352ef8524c5>`__  2024-06-22   ``Prepare docs 2nd wave June 2024 (#40273)``
`65dbf86f72 <https://github.com/apache/airflow/commit/65dbf86f72ed7be779e7dadd8e8e57c1216c7c07>`__  2024-06-07   ``Fix openai 1.32 breaking openai tests (#40110)``
==================================================================================================  ===========  ==================================================

1.2.1
.....

Latest change: 2024-05-26

==================================================================================================  ===========  ================================================
Commit                                                                                              Committed    Subject
==================================================================================================  ===========  ================================================
`34500f3a2f <https://github.com/apache/airflow/commit/34500f3a2fa4652272bc831e3c18fd2a6a2da5ef>`__  2024-05-26   ``Prepare docs 3rd wave May 2024 (#39738)``
`2b1a2f8d56 <https://github.com/apache/airflow/commit/2b1a2f8d561e569df194c4ee0d3a18930738886e>`__  2024-05-11   ``Reapply templates for all providers (#39554)``
`2c05187b07 <https://github.com/apache/airflow/commit/2c05187b07baf7c41a32b18fabdbb3833acc08eb>`__  2024-05-10   ``Faster 'airflow_version' imports (#39552)``
`73918925ed <https://github.com/apache/airflow/commit/73918925edaf1c94790a6ad8bec01dec60accfa1>`__  2024-05-08   ``Simplify 'airflow_version' imports (#39497)``
==================================================================================================  ===========  ================================================

1.2.0
.....

Latest change: 2024-05-01

==================================================================================================  ===========  ==================================================================================
Commit                                                                                              Committed    Subject
==================================================================================================  ===========  ==================================================================================
`fe4605a10e <https://github.com/apache/airflow/commit/fe4605a10e26f1b8a180979ba5765d1cb7fb0111>`__  2024-05-01   ``Prepare docs 1st wave May 2024 (#39328)``
`da6c2bcf3c <https://github.com/apache/airflow/commit/da6c2bcf3cb270cb305dd407b34e411ee4a6e440>`__  2024-05-01   ``OpenAI Files & Vector Store Hooks (#39248)``
`ead9b00f7c <https://github.com/apache/airflow/commit/ead9b00f7cd5acecf9d575c459bb62633088436a>`__  2024-04-25   ``Bump minimum Airflow version in providers to Airflow 2.7.0 (#39240)``
`2674a69780 <https://github.com/apache/airflow/commit/2674a69780bd1aa0768ad035b96c6e5e551ce529>`__  2024-04-19   ``OpenAI Chat & Assistant hook functions (#38736)``
`5fa80b6aea <https://github.com/apache/airflow/commit/5fa80b6aea60f93cdada66f160e2b54f723865ca>`__  2024-04-10   ``Prepare docs 1st wave (RC1) April 2024 (#38863)``
`83316b8158 <https://github.com/apache/airflow/commit/83316b81584c9e516a8142778fc509f19d95cc3e>`__  2024-03-04   ``Prepare docs 1st wave (RC1) March 2024 (#37876)``
`5a0be392e6 <https://github.com/apache/airflow/commit/5a0be392e66f8e5426ba3478621115e92fcf245b>`__  2024-02-16   ``Add comment about versions updated by release manager (#37488)``
`bfb054e9e8 <https://github.com/apache/airflow/commit/bfb054e9e867b8b9a6a449e43bfba97f645e025e>`__  2024-02-12   ``Prepare docs 1st wave of Providers February 2024 (#37326)``
`f61ffe58d3 <https://github.com/apache/airflow/commit/f61ffe58d3cd0bcb51f6f9036a3acbfa4443d977>`__  2024-02-11   ``Remove extra package headers in provider indexes (#37324)``
`cead3da4a6 <https://github.com/apache/airflow/commit/cead3da4a6f483fa626b81efd27a24dcb5a36ab0>`__  2024-01-26   ``Add docs for RC2 wave of providers for 2nd round of Jan 2024 (#37019)``
`2b4da0101f <https://github.com/apache/airflow/commit/2b4da0101f0314989d148c3c8a02c87e87048974>`__  2024-01-22   ``Prepare docs 2nd wave of Providers January 2024 (#36945)``
`19ebcac239 <https://github.com/apache/airflow/commit/19ebcac2395ef9a6b6ded3a2faa29dc960c1e635>`__  2024-01-07   ``Prepare docs 1st wave of Providers January 2024 (#36640)``
`6937ae7647 <https://github.com/apache/airflow/commit/6937ae76476b3bc869ef912d000bcc94ad642db1>`__  2023-12-30   ``Speed up autocompletion of Breeze by simplifying provider state (#36499)``
`9b5d6bfe27 <https://github.com/apache/airflow/commit/9b5d6bfe273cf6af0972e28ff97f99ea325cd991>`__  2023-12-28   ``Add documentation for 3rd wave of providers in Deember (#36464)``
`b15d5578da <https://github.com/apache/airflow/commit/b15d5578dac73c4c6a3ca94d90ab0dc9e9e74c9c>`__  2023-12-23   ``Re-apply updated version numbers to 2nd wave of providers in December (#36380)``
==================================================================================================  ===========  ==================================================================================

1.1.0
.....

Latest change: 2023-12-08

==================================================================================================  ===========  =======================================================================
Commit                                                                                              Committed    Subject
==================================================================================================  ===========  =======================================================================
`999b70178a <https://github.com/apache/airflow/commit/999b70178a1f5d891fd2c88af4831a4ba4c2cbc9>`__  2023-12-08   ``Prepare docs 1st wave of Providers December 2023 (#36112)``
`d0918d77ee <https://github.com/apache/airflow/commit/d0918d77ee05ab08c83af6956e38584a48574590>`__  2023-12-07   ``Bump minimum Airflow version in providers to Airflow 2.6.0 (#36017)``
`d2514b408c <https://github.com/apache/airflow/commit/d2514b408cb98f792289a5d032aaf85fe605350d>`__  2023-12-06   ``Bump up openai version to >=1.0 & use get_conn (#36014)``
==================================================================================================  ===========  =======================================================================

1.0.1
.....

Latest change: 2023-11-24

==================================================================================================  ===========  ======================================================================================
Commit                                                                                              Committed    Subject
==================================================================================================  ===========  ======================================================================================
`0b23d5601c <https://github.com/apache/airflow/commit/0b23d5601c6f833392b0ea816e651dcb13a14685>`__  2023-11-24   ``Prepare docs 2nd wave of Providers November 2023 (#35836)``
`99534e47f3 <https://github.com/apache/airflow/commit/99534e47f330ce0efb96402629dda5b2a4f16e8f>`__  2023-11-19   ``Use reproducible builds for provider packages (#35693)``
`99df205f42 <https://github.com/apache/airflow/commit/99df205f42a754aa67f80b5983e1d228ff23267f>`__  2023-11-16   ``Fix and reapply templates for provider documentation (#35686)``
`acb9458d09 <https://github.com/apache/airflow/commit/acb9458d096f956b319c2b121cbcd01489492491>`__  2023-11-14   ``Refine Type Handling in OpenAI Embedding Operator to Match OpenAI Typings (#35547)``
==================================================================================================  ===========  ======================================================================================

1.0.0
.....

Latest change: 2023-11-08

==================================================================================================  ===========  =============================================================
Commit                                                                                              Committed    Subject
==================================================================================================  ===========  =============================================================
`1b059c57d6 <https://github.com/apache/airflow/commit/1b059c57d6d57d198463e5388138bee8a08591b1>`__  2023-11-08   ``Prepare docs 1st wave of Providers November 2023 (#35537)``
`cca4aa4e9a <https://github.com/apache/airflow/commit/cca4aa4e9ab545c8aab01b05941a372044668a67>`__  2023-11-07   ``Add OpenAI Provider (#35023)``
==================================================================================================  ===========  =============================================================
