---
layout: default
permalink: /applications-tools/open-ais
description: "OpenAIS is an open-source initiative supported by VLIZ and CSIR to process, decode, and transform raw AIS vessel tracking data for marine and scientific research."
---

# OpenAIS <a name="open-ais"></a>

## Background

The **Automatic Identification System (AIS)** is a VHF-based real-time anti-collision system used globally in maritime navigation. While vessels continually broadcast GPS positions, speed, heading, identification, and voyage metadata to avoid collisions at sea, this rich stream holds immense value for marine science, conservation, and ocean policy.

**[OpenAIS](https://open-ais.org/){:target=”_blank”}** is an open-source initiative sponsored by the **[Flanders Marine Institute (VLIZ)](https://www.vliz.be/en){:target=”_blank”}** and the **[Council for Scientific and Industrial Research (CSIR)](https://www.csir.co.za/){:target=”_blank”}**. The project provides a modular, containerized toolset designed to lower technical barriers and domain expertise needed to ingest, decode, and transform raw vessel tracking streams into usable scientific datasets.

---

## VLIZ Setup & Data Pipeline

VLIZ maintains an active interest and operational deployment within the OpenAIS ecosystem:

* **VHF Receiver Network**: VLIZ operates an AIS receiver stationed at the Marine Station Ostend (MOC), contributing to the global [AISHub](https://www.aishub.net/){:target=”_blank”} network and covering the Belgian Part of the North Sea (Belgian EEZ).
* **Ingestion & Streaming**: Raw VHF streams (~800 messages/sec) pass through a message queue (RabbitMQ) where they are decoded, cleaned, and filtered down to ~300 messages/sec.
* **Spatio-Temporal Storage**: Filtered messages are persisted in a specialized **PostgreSQL + PostGIS + TimescaleDB** database (~1 GB/day of position fixes plus helper indexes and aggregate tables), maintaining historical records since late 2021.

---

## Scientific Applications & Use Cases

OpenAIS supports diverse ocean research questions and monitoring efforts:

* **Oceanographic Sensor & Mooring Tracking**: Correlating vessel traffic with deployed sensors (e.g., investigating gear entanglement or lost acoustic sensor moorings).
* **Underwater Noise Modeling**: Using high-resolution traffic density and speed profiles as proxies for anthropogenic underwater noise to inform sensor placement and marine life impact studies.
* **Habitat Protection & Fishing Effort**: Analyzing spatial density, class distributions, and speed profiles across Marine Protected Areas (MPAs), wind farm zones, and sensitive benthic habitats (including anchor scarring mapping).
* **Sensor & Data Fusion**: Combining AIS tracks with satellite remote sensing (such as Sentinel-1 SAR radar imagery for dark ship detection) or animal telemetry tracking.

---

## Access & Development

The OpenAIS platform is built as open-source, containerized microservices:

* **Documentation & Project Hub**: Learn more and follow tutorials at **[open-ais.org](https://open-ais.org/){:target=”_blank”}**.
* **Source Code**: Explore repositories, deployment guides, and data pipeline components on the **[OpenAIS GitLab Group](https://gitlab.com/openais/){:target=”_blank”}**.
* **Use Cases & Data Requests**: Browse recipes and register research requirements in the **[OpenAIS Examples Repository](https://gitlab.com/openais/examples){:target=”_blank”}**.

---

## Introductory Presentation <a name="presentation"></a>

{% include presentation/google-slides.html
   document_id="2PACX-1vSAaX8MO12_E35C8EbM6t8VHAbScH6Y195ZM9KmXrUNM9J6aIW16c2_ek0ydHee0pcA87fjtCoL1jei" 
%}


