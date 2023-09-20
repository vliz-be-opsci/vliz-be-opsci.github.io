---
layout: default
permalink: /applications-tools/vocab-term-lookup
curly: false
---

# Vocab Term Lookup

## Background

Early in our semantic web approach to open science data management we identified the need to support end-users in creating the factual links that are essential to the linked-data enterprise.

Even if we provide approaches to hide direct knowledge graph usage behind the more familiar tabular views (and do so in both directions of providing or retrieving data) we realised that there is no way to actually avoid having actual data-values (content) that reference linked-data terms, concepts or values from controlled vocabularies. Vocabularies that will inevitably be remotely managed.

To facilitate in this we have developed a vocab-term-lookup-server and -widget.


## What does it do

Looking at the relevant life-cycle of this particular aspect of the data management we set out to build a system that covers the following distinct use cases:

![UML UseCase Diagram for the vocab-term-lookup](/assets/media/img/content/vocab-term-lookup-uml-ucd.svg){:.image-style-content-center} 

| Who           | Does What                                    | To Achieve What                                       | 
|---------------|----------------------------------------------|-------------------------------------------------------|
| Vocab Admin   | adds selected vocabularies to the service    | so they become available for integration and lookup   | 
| App Developer | configures and embeds a widget into an app   | so the selected URI terms of the found values will be used in the content managed by the application | 
| App User      | just used the widget in the app              | to make a link to the actual concept it knows about, without having to worry about the RDF technical details | 


Note: this does not include:
 - the actual development and management of vocabularies.
 - the development of the application or its backend to actually store the selected values
 - an approach to regularly check up on the continued existence / relevance / possible deprecation of the linked content


## Where can I find it?

The VLIZ deployed vocab server is running at [https://todo.vliz.be/](https://todo.vliz.be){:target=”_blank”}

The application is [developed in open source](https://github.com/vlizBE/vocabserver-app){:target=”_blank”} and being shared under the liberal MIT license.

As you can read in the documentation over there, the system is build as a collection of microservices that are expected to be launched via `docker-compose`


## Which vocabs do you serve?

By running your own instance one is in full control to configure their own list of available vocabularies.

The VLIZ instance is setup to service the marine research domain. Therefore the available vocabularise consist off:
* a selection of important skos collections from [NERC Vocab Server(NVS)](https://vocab.nerc.ac.uk/collection){:target=”_blank”} maintained by the [British Oceanographic Data Centre (BODC)](https://www.bodc.ac.uk/){:target=”_blank”}
* the maintained lists of [Marine Species](https://marinespecies.org/) and [Marine Regions](https://marineregions.org){:target=”_blank”}   
* relevant additional concepts (projects, people, organizations, ...) from [MarineInfo.org](https://marineinfo.org){:target=”_blank”} 



## Introductory presentation

{% include presentation/google-slides.html
   document_id="2PACX-1vQdoAd8Cq5CFsS7gC5Q1aGhYEW0dAA_sOQ_RN2U9giR6cI9l2R75o9USHCMgxItHyD21-4BZ_0QErSY"
%}
