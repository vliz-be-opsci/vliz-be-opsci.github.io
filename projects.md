---
layout: default
graph_logo_bg: true
permalink: /projects/
cover: /assets/media/img/cover/graph_concept_art.jpg
description: "Dive into our Open Science Projects, featuring initiatives like Marco-Bolo and FAIR-EASE. Explore how we're revolutionizing marine and environmental data management!"
title: "Open Science Projects"

projects:
  - title: "Marco-Bolo"
    description: >-
      MARCO-BOLO aims to structure and strengthen European coastal and marine biodiversity observation capabilities, linking 
      them to global efforts to understand and restore ocean health, hence ensuring that outputs respond to explicit 
      stakeholder needs from policy, planning and industry. MBO will establish and engage with a Community of Practice to 
      determine end-user needs with the aim of optimising marine data flows, knowledge uptake, and improving governance based 
      on biodiversity observations.
    clickthrough_url: https://marcobolo-project.eu/
    image: "/assets/media/img/project/MARCO-BOLO_logo_col.png"
    tags:
      - EOSC-Association
      - EU

  - title: "FAIR-EASE"
    description: >-
      Earth and environmental sciences require a large panel and volume of data from satellite, in-situ observations, models, 
      omics experiments. Earth system domains are interconnected and even if interfaces between domains appear of primary 
      importance for several studies with large societal impacts, such as climate change, agriculture and food, human safety 
      and health, the present digital architecture is based essentially on distributed and domain-dependent data repositories 
      inducing real difficulties for integrated uses of all the environmental data. To go beyond this state-of-the-art, the 
      overall objective of FAIR-EASE is to customize and operate distributed and integrated services for observation and 
      modelling of the Earth system, environment and biodiversity by improving the TRL of their different components 
      implemented in close cooperation with user-communities, the European Open Science Cloud and research infrastructures in 
      their design and sustainable availability.
    clickthrough_url: https://www.fairease.eu/
    image: "/assets/media/img/project/fairease-logo.svg"
    tags:
      - EOSC-Association
      - EU

  - title: "MareGraph"
    description: >-
      The MAREGRAPH project will provide an open linked data production and publication of three high impact datasets in the 
      marine domain (the World Register of Marine Species (WoRMS), Marine Regions and EurOBIS (the European Node of the 
      international Ocean Biodiversity Information System) using state of the art technologies.
    clickthrough_url: https://www.maregraph.eu 
    image: "/assets/media/img/project/maregraph-text-horizontal-600x200.svg"
    tags:
      - EU
      - RDF

  - title: "George"
    description: >-
      GEORGE is a Horizon Europe-funded project that develops novel technologies to improve ocean observations. The technologies developed
      will represent the next level in systematic long-term autonomous ocean observations.
    clickthrough_url: https://george-project.eu/
    image: "/assets/media/img/project/george-logo.png"
    tags:
      - EU

  - title: "Blue-Cloud-2026"
    description: >- 
      The European H2020 Blue-Cloud project aims to achieve a range of innovative services through a practical approach, 
      demonstrating the potential of how the European Open Science Cloud (EOSC) can serve marine research and the blue 
      economy. VLIZ is the initiator and partner in two 'Plankton demonstrators' and is also involved in this project as a 
      data infrastructure (EurOBIS).
    clickthrough_url: https://blue-cloud.org/
    image: "/assets/media/img/project/bluecloud2026-logo.png"
    tags:
      - EOSC-Association
      - EU

  - title: "Mission Atlantic"
    description: >-
      The “mission” of Mission Atlantic is to investigate how multiple pressures within and across important sub-areas
      affect the resilience of the Atlantic Ocean to future climate and societal changes. 
      The project will tackle this question by advancing knowledge on ecosystem processes as well as applying new 
      observation technology and state-of-the-art predictive capacity to develop an operational regional and basin-scale 
      Integrated Ecosystem Assessment (IEA)."
    clickthrough_url: https://missionatlantic.eu/
    image: "/assets/media/img/project/missionatlantic-logo.png"
    tags:
      - EOSC-Association
      - EU

  - title: "EDITO Infra"
    description: >-
      The main aim of EDITO-Infra, the “EU Public Infrastructure for the European Digital Twin”, is to build the 
      EU Public Infrastructure backbone for the European Digital Twin of the Ocean (DTO) by upgrading, combining and 
      integrating key service components of the existing EU ocean observing, monitoring and data programmes 
      Copernicus Marine Service (Copernicus Marine Service) and the European Marine Observation and Data Network (EMODnet) 
      into a single digital framework."
    clickthrough_url: https://edito-infra.eu/
    image: "/assets/media/img/project/edito-logo.png"
    tags:
      - EOSC-Association
      - EU

# coming soon:
#- AQUASERV
#- BioDT
#- EDNAAqua Plan
#- Open AIS

# passed ones:
#- ENVRI-FAIR
#- EOSC Future
#- EOSC-Life

---

{% include item/list/row/text_image/main.html items=page.projects %}
