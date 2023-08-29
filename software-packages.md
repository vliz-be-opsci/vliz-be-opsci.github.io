---
layout: default
permalink: /applications-tools/software-packages
cover: /assets/media/img/cover/cover-code-python.jpg
title: Software Packages

items:
  - title: "py-data-rules"
    description: "python library for data quality assessment"
    clickthrough_url: https://github.com/vliz-be-opsci/py-data-rules
    image: "/assets/media/img/socials/github-mark.svg"
    tags:
      - data-quality
    icon_url:
        github: https://github.com/vliz-be-opsci/py-data-rules

  # - title: "py-maris-cdi"
  #   description: "py library to consume the maris cdi api to retrieve ODV datasets programmatically"
  #   clickthrough_url: https://github.com/vliz-be-opsci/py-maris-cdi
  #   image: "/assets/media/img/socials/github-mark.svg"
  #   tags:
  #     - ...
  #   icon_url:
  #       github: https://github.com/vliz-be-opsci/py-maris-cdi

  - title: "py-rabbit"
    description: "A wrapper around Kombu to use RabbitMQ, especially on docker images"
    clickthrough_url: https://github.com/vliz-be-opsci/py-rabbit
    image: "/assets/media/img/socials/github-mark.svg"
    tags:
      - rabbitmq
    icon_url:
        github: https://github.com/vliz-be-opsci/py-rabbit
        cube: https://pypi.org/project/rab_the_bit/

  - title: "py-sdn-cdi-client"
    description: "Python client for the SDN API"
    clickthrough_url: https://github.com/vliz-be-opsci/py-sdn-cdi-client
    image: "/assets/media/img/socials/github-mark.svg"
    tags:
      - openapi-client
    icon_url:
        github: https://github.com/vliz-be-opsci/py-sdn-cdi-client

  - title: "py-xmlasdict"
    description: "python library to approach xml DOM trees as python dicts with iterating and attribute-getting behavior"
    clickthrough_url: https://github.com/vliz-be-opsci/py-xmlasdict
    image: "/assets/media/img/socials/github-mark.svg"
    tags:
      - xml
    icon_url:
        github: https://github.com/vliz-be-opsci/py-xmlasdict
        cube: https://pypi.org/project/xmlasdict/

  - title: "py-yaml-for-pema"
    description: "tool to mix yaml structured schema description with actual text based parameters files"
    clickthrough_url: https://github.com/vliz-be-opsci/py-yaml-for-pema
    image: "/assets/media/img/socials/github-mark.svg"
    tags:
      - yaml
    icon_url:
        github: https://github.com/vliz-be-opsci/py-yaml-for-pema

  - title: "pykg2tbl"
    description: "KG-2-Tbl stands for 'Knowledge-Graph to Tables'. This python package delivers an abstraction layer to querying into RDF graphs that reside either on remote triplestores providing a SPARQL endpoint, or can be downloaded in dump files in standard RDF serializations.  \n
    This bridges the gap between the linked interoperable semantic world where graphs rule and the classic table-view all data-processing tools (and their users) keep demanding: dataframes, graph-plot-tools, spreadsheets, ... Since those remain the goto access-points to the analysis and visualisation of data, we believe this abstraction library can help out matching up those environments to the information linked up in knowledge graphs." 
    clickthrough_url: https://github.com/vliz-be-opsci/pykg2tbl
    image: "/assets/media/img/socials/github-mark.svg"
    tags:
      - tables
      - knowledge graph
    icon_url:
        github: https://github.com/vliz-be-opsci/pykg2tbl 
        cube: https://pypi.org/project/pykg2tbl/

  - title: "pyodv"
    description: "Python package for reading ODV (Ocean Data Variables) files"
    clickthrough_url: https://github.com/vliz-be-opsci/pyodv
    image: "/assets/media/img/socials/github-mark.svg"
    tags:
      - bio-odv
    icon_url:
        github: https://github.com/vliz-be-opsci/pyodv
        cube: https://pypi.org/project/pyodv/

  - title: "pyrdfj2"
    description: "Python wrapper on jinja SPARQL templating"
    clickthrough_url: https://github.com/vliz-be-opsci/pyrdfj2
    image: "/assets/media/img/socials/github-mark.svg"
    tags:
      - jinja
      - sparql
    icon_url:
        github: https://github.com/vliz-be-opsci/pyrdfj2
        cube: https://pypi.org/project/pyrdfj2/

  - title: "pysembench"
    description: "semantic web workbench"
    clickthrough_url: https://github.com/vliz-be-opsci/pysembench
    image: "/assets/media/img/socials/github-mark.svg"
    tags:
      - semantic-web
      - task-manager
    icon_url:
        github: https://github.com/vliz-be-opsci/pysembench

  - title: "pysepca"
    description: "Sparql End Point Compliance Assessment - Ad hoc set of checks for deployed sparql services"
    clickthrough_url: https://github.com/vliz-be-opsci/pysepca
    image: "/assets/media/img/socials/github-mark.svg"
    tags:
      - sparql
    icon_url:
        github: https://github.com/vliz-be-opsci/pysepca

  - title: "pysubyt"
    description: "SU-By-t stands for 'Semantic Uplifting BY Templates'. This python package delivers a pragmatical jinja-templating approach to generating turtle syntax files from provided tabular data sources. It is a very basic and 'good enough' take on this, and should be considered as a low-level-entry alternative to things like linkml, rml.io or csvw. \n
    It bridges the gap from the comfortable table-view and the RDF based graph-view. The latter might be opening to a world of endless flexibility, but it refrains from being the natural modus operandi for a lot of natural data entry and data management where xls and csv remain the popular choice."
    clickthrough_url: https://github.com/vliz-be-opsci/pysubyt
    image: "/assets/media/img/socials/github-mark.svg"
    tags:
      - templating
      - semantic uplifting
    icon_url:
        github: https://github.com/vliz-be-opsci/pysubyt
---

{% include item/list/row/image_text_link/main.html items=page.items %}