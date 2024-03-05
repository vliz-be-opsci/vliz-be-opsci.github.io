---
layout: default
permalink: /publications/
title: Open Science publications
description: "Delve into a diverse collection of open science publications fostering innovation and collaboration in research."
items:
  - title: "DMBON Assistant publication"
    description: "DMBON is a tool to assist in the creation of a Data Management Plan (DMP). 
      It is a web application that guides the user through the process of creating a DMP. 
      It is based on the DCC DMPonline tool, but has been adapted to the needs of the Belgian marine research community. 
      The tool is available in English."
    clickthrough_url: "https://example.org/publication_url/01"
    authors: 
        - name: "Bart Vanhoorne"
        - name: "Jan Seys"
        - name: "Jan Haspeslagh"
        - name: "Pieter Provoost"
    tags:
      - open data
      - data management
    documents: 
      - url: "https://example.org/documents/01"

---

<div class="col-12 field__item">
    <div class="pb-4 pt-4 paragraph paragraph--type--container paragraph--view-mode--default">
        <div class="field field--name-field-paragraph-container-items field--type-entity-reference-revisions field--label-hidden">
            <div class="row field__items included-item-list">
              {% for pub in site.data.vliz-openscience.hits.hits %}
              <div class="col-lg-11 field__item publication publication">
                  <div class="paragraph paragraph--type--basic-text paragraph--view-mode--default">
                      <div class="clearfix text-formatted field field--name-field-body field--type-text-long field--label-hidden field__items">
                          <h5>
                              <a href="{{pub.links.doi}}">
                                  {{pub.metadata.title}} 
                              </a>
                          </h5>
                          <p class="blue authors">
                          <b>
                              {% for author in pub.metadata.creators %}
                                {% if forloop.last %}
                                  {{author.name}} 
                                {% else %}
                                  {{author.name}};
                                {% endif %}
                              {% endfor %}
                          </b>
                          </p>
                          {% for tag in pub.metadata.communities %}
                              {% if tag %}
                                  <a href="#" class="field__news_teaser">{{ tag.id }}</a>
                              {% endif %}
                          {% endfor %}
                          <div class="description">
                              {{pub.metadata.description}}
                          </div>
                      </div>
                  </div>
              </div>
              <div class="col-lg-1 field__item">
                  <div class="row file_links">
                      {% if pub.files %}
                      {% for file in pub.files %}
                      <div class="col-lg-12 field__item gy-3">
                          <a class="basic-button" href="{{file.links.self}}" target="_blank" rel="noopener noreferrer" style="margin-right: 5px;">
                              <span class="fa fa-download"></span>
                          </a>
                      </div>
                      {% endfor %}
                      {% endif %}
                  </div>
              </div>
              {% endfor %}
            </div>
        </div>
    </div>
</div>

{% include publications/main.html items=page.items %}

## Conference Proceedings

Same here for the conference proceedings ?

{% for pub in site.data.publications.conferenceProceedings %}

<p>{{pub.title}}</p>
{% endfor %}