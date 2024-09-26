---
layout: default
permalink: /applications-tools/
title: Applications and tools
cover: /assets/media/img/cover/cover-code-python.jpg
description: "Explore our suite of applications and tools at VLIZ, designed to support open science. From DMBON Assistant for data management to Open-AIS.org for vessel traffic data, we have a tool for every need!"

items:
  - title: "DMBON Assistant"
    description:
      "DMBON is a tool to assist in the creation of a Data Management Plan (DMP).
      It is a web application that guides the user through the process of creating a DMP.
      It is based on the DCC DMPonline tool, but has been adapted to the needs of the Belgian marine research community.
      The tool is available in English."
    clickthrough_url: "/applications-tools/dmbon-assistant"
    image: "/assets/media/img/app/dmbon-assistant-logo.svg"
    tags:
      - open data
      - data management
    icon_url:
      github: "https://github.com/vliz-be-opsci/dmbon-assistant"

  - title: "Open-AIS.org"
    description: "VLIZ Open-Science has a historic affiliation and vetted interest into the development of open-ais.org: a set of tools and solutions for exploring captured vessel traffic data in a research context."
    clickthrough_url: "/applications-tools/open-ais"
    image: "/assets/media/img/app/open-ais-logo.svg"
    tags:
      - open data
      - vessels
    icon_url:
      github: https://gitlab.com/openais/
      book: https://open-ais.org

  - title: "Marine Info Affordances"
    description: "MIA or Marine Info Affordances is a project that aims to provide information about the marine environment to the user. All information that comes from marineinfo.org has been tripelised and can be retrieved via accessing their respective ttl URI's. This information can then be displayed in a user-friendly way to the user via pop-up cards."
    clickthrough_url: "/MIA"
    image: "/assets/media/img/app/marine_info_affordances.jpg"
    tags:
      - open data
      - demo
    icon_url:
      github: https://gitlab.com/vliz-be-opsci/MIA

  - title: "RO-Crate demo"
    description: "Applying RO-Crates is a practical way to achieve an elegant a FAIR and open linked data publication of your research data.  We have created a number of tools to exploit that in combination with using git."
    clickthrough_url: "/applications-tools/ro-crate-demo"
    image: "/assets/media/img/app/ro-crate.svg"
    tags:
      - ro-crate
      - demo
    icon_url:
      github: https://github.com/vliz-be-opsci/demo-rocrate
      eye: /demo-rocrate/

  - title: "Vocab Term Lookup Server and Widget"
    description: "VLIZ commissioned to develop and deploy an open source system to let end-users easily find selected vocabulary terms by full-text-search into label and description. Operational since 2023."
    clickthrough_url: "/applications-tools/vocab-term-lookup"
    image: "/assets/media/img/app/rdf-logo.svg"
    tags:
      - vocabularies
      - linked data
      - rdf
    icon_url:
      github: https://github.com/vlizBE/vocabserver-app

  - title: "Knowledge Graph Analysis Platform"
    description: "The Knowledge Graph Analysis Platform is a web-based platform that allows users to explore and analyze knowledge graphs. It is designed to be user-friendly and intuitive, with a focus on visualizing and analyzing complex data structures."
    clickthrough_url: "/applications-tools/kgap"
    image: "/assets/media/img/app/kgap.jpg"
    tags:
      - knowledge graph
      - analysis
      - RDF
    icon_url:
      github: https://github.com/vliz-be-opsci/k-gap
---

{% include item/list/row/image_text_link/main.html items=page.items %}
