---
layout: default
permalink: /applications-tools/software-packages
cover: /assets/media/img/cover/cover-code-python.jpg
title: Software Packages

items:
  - title: "pysubyt"
    description: "SU-By-t stands for 'Semantic Uplifting BY Templates'. This python package delivers a pragmatical jinja-templating approach to generating turtle syntax files from provided tabular data sources. It is a very basic andj 'good enough' take on this, and should be considered as a low-level-entry alternative to things like linkml, rml.io or csvw. \n
    It bridges the gap from the comfortable table-view and the RDF based graph-view. The latter might be opening to a world of endless flexibility, but it refrains from being the natural modus operandi for a lot of natural data entry and data management where xls and csv remain the popular choice."
    clickthrough_url: https://github.com/vliz-be-opsci/pysubyt
    image: "/assets/media/img/GitHub-Mark.png"
    tags:
      - templating
      - semantic uplifting
    icon_url:
        github: https://github.com/vliz-be-opsci/pysubyt



  - title: "pykg2tbl"
    description: "KG-2-Tbl stands for 'Knowledge-Graph to Tables'. This python package delivers an abstraction layer to querying into RDF graphs that reside either on remote triplestores providing a SPARQL endpoint, or can be downloaded in dump files in standard RDF serializations.  \n
    This bridges the gap between the linked interoperable semantic world where graphs rule and the classic table-view all data-processing tools (and their users) keep demanding: dataframes, graph-plot-tools, spreadsheets, ... Since those remain the goto access-points to the analysis and visualisation of data, we believe this abstraction library can help out matching up those environments to the information linked up in knowledge graphs." 
    clickthrough_url: https://github.com/vliz-be-opsci/pykg2tbl
    image: "/assets/media/img/GitHub-Mark.png"
    tags:
      - tables
      - knowledge graph
    icon_url:
        github: https://github.com/vliz-be-opsci/pykg2tbl 
        cube: https://pypi.org/project/pykg2tbl/
---

{% include item/list/row/image_text_link/main.html items=page.items %}