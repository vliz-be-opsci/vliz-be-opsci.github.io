---
layout: default
curly: true

banner:
  title: "Open Science"
  description: "Todo -- one liner?"
  clickthrough_text: "More About The VLIZ approach to Open Science"
  clickthrough_url: "/open-science"
  media: "/assets/media/img/cover/graph-nodes-blue-gradient.webp"

mission_item:
  title: "Open science mission and values"
  image: "/assets/media/img/open-science-logo-flask.svg"
  description: "VLIZ is committed to open science. We believe that open science is the best way to advance 
      science and to make it more efficient, reliable and transparent. We are convinced that open science is the best way to make science more inclusive and to increase its societal impact. We are committed to open science because we believe that it is the best way to make science more fun."

core_principles:
  - title: Objectivity
    description: "Open science promotes an attitude of impartiality in research, 
      where researchers strive to approach their work without bias or personal interests."
  - title: Honesty
    description: "Open science emphasizes the importance of honesty in all aspects of research, 
      including reporting findings accurately and transparently. 
      Researchers are expected to be truthful and avoid fabrication or falsification of data."
  - title: Openness
    description: "Open science values transparency and accessibility. 
      It encourages researchers to eliminate barriers to accessing and sharing data, materials, experiences, and tools. 
      This includes making research outputs, such as data sets and publications, 
      openly available to the scientific community and the public."
  - title: Accountability
    description: "Open science promotes accountability by holding researchers responsible for their actions 
      and ensuring that they adhere to ethical standards and research integrity. 
      Researchers are expected to be accountable for their methodologies, results, and interpretations."
  - title: Fairness
    description: "Open science advocates for fairness in research practices. This includes fair attribution of 
      credit to contributors, fair evaluation of research outputs, and fair access to research opportunities and 
      resources. Open science strives to create an inclusive and equitable research environment."
  - title: Stewardship
    description: "Open science recognizes the responsibility of researchers to protect and promote the research 
      enterprise. This involves taking care of the research process, resources, and relationships within 
      the scientific community. Researchers are encouraged to contribute to the development and improvement of 
      research practices and policies."
---

{% include banner/main.html banner=page.banner %}

{% include item/single/row_and_wave/main.html item=page.mission_item %}


{% include item/list/carrousel/block/main.html 
    title="Core values and guiding principles"
    items=page.core_principles 
%}

{% include no_bg_colored_blocks/main.html data=site.data.priority_areas_action %}

{% include light_bg.html content=
"<h2>FAIR values</h2>
<p>
    The FAIR Guiding Principles for scientific data management and stewardship are intended to help improve the
    Findability, Accessibility, Interoperability, and Reuse of digital assets. The FAIR Principles emphasize
    machine-actionability (i.e., the capacity of computational systems to find, access, interoperate, and reuse data
    with none or minimal human intervention) because humans increasingly rely on computational support to deal with
    data as a result of the increase in volume, complexity, and creation speed of data.
</p>
"
%}