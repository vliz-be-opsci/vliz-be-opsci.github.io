---
layout: default
curly: true

banner:
  title: "Open Science"
  quotes:
    - title: " ...90% of scientists agreeing that the replicability crisis is real"
      clickthrough_text: "Hensel, 2023"
      clickthrough_url: "https://www.tandfonline.com/action/showCitFormats?doi=10.1080%2F08989621.2021.1981870"
    - title: " The replication crisis has stimulated a movement for open science, encouraging or even requiring researchers to publish their raw data and analysis code... One common response to the replication crisis has been to call for open science"
      clickthrough_text: "Hicks, 2021"
      clickthrough_url: "https://www.tandfonline.com/doi/full/10.1080/08989621.2021.1962713"
    - title: "Between the dawn of time and 2003, five exabytes of data had been created at Google. By 2010, this amount of data was being created every two days, and by 2021 it was being created every 40 minutes. There are approximately 400,000 bytes of data for every grain of sand on earth"
      clickthrough_text: "Datacamp.com, 2023"
      clickthrough_url: "https://www.datacamp.com/blog/25-interesting-facts-about-data-science"
    - title: " 80% of data scientist's time is spent organizing data"
      clickthrough_text: "Ruiz, 2023"
      clickthrough_url: "https://www.infoworld.com/article/3228245/the-80-20-data-science-dilemma.html"
    - title: "The global datasphere has 90% replicated data and 10% unique data. In the worldwide digital universe, between 80 and 90% of the data is unstructured"
      clickthrough_text: "Simplilearn.com, 2023"
      clickthrough_url: "https://www.simplilearn.com/data-science-facts-article"
    - title: "90% of the data in the global datasphere is replicated data"
      clickthrough_text: "Petroc, 2020"
      clickthrough_url: "https://www.statista.com/statistics/1185888/worldwide-global-datasphere-unique-replicated-data/"
  clickthrough_text: "More About The VLIZ approach"
  clickthrough_url: "/open-science"
  media: "/assets/media/img/cover/graph-nodes-blue-gradient.webp"

mission:
  title: "Our mission and values"
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

priorities:
  - title: Adoption of the FAIR Principles
    description: "The FAIR (Findable, Accessible, Interoperable, and Reusable) Principles
                  provide a framework for making research data more accessible and
                  reusable. These principles emphasize the importance of data
                  discoverability, accessibility, and interoperability, enabling
                  researchers to find and use data more effectively. By adopting the FAIR
                  Principles, researchers and institutions can contribute to the overall
                  goal of open science and fair data."
  - title: "Implementation of Data Management Plans"
    description: "Data management plans (DMPs) are essential for ensuring that research
                  data is properly managed, preserved, and shared. DMPs outline the
                  strategies and practices for data collection, organization,
                  documentation, storage, and sharing throughout the research process. By
                  implementing robust DMPs, researchers can ensure that their data is
                  properly managed and made available to others in a fair and transparent
                  manner."
  - title: "Promotion of Data Sharing and Collaboration"
    description: "Open sharing of research data promotes collaboration and accelerates
                  scientific progress. Researchers and institutions can prioritize the
                  sharing of research data through data repositories, data archives, and
                  open data platforms. This not only enhances the visibility and impact of
                  research but also allows others to validate and build upon existing
                  findings. Encouraging a culture of data sharing and collaboration can
                  significantly contribute to the advancement of open science and fair
                  data practices"
  - title: Education and Training on Open Science and Fair Data
    description: "To foster a culture of open science and fair data, it is important to
                  provide education and training opportunities to researchers, students,
                  and other stakeholders. Workshops, webinars, and online resources can be
                  developed to raise awareness about the benefits and best practices of
                  open science and fair data. By equipping individuals with the necessary
                  skills and knowledge, we can ensure the widespread adoption of open
                  science principles and fair data practices"
  - title: "Support from Funding Agencies and Institutions"
    description:  "Funding agencies and institutions play a crucial role in promoting open
                  science and fair data practices. They can develop policies and
                  guidelines that encourage researchers to adopt open science principles
                  and adhere to fair data practices. By providing support, resources, and
                  incentives, funding agencies and institutions can create an environment
                  that fosters the sharing and reuse of research data"
---

{% include banner/main.html banner=page.banner %}

{% include item/single/row_and_wave/main.html item=page.mission %}


{% include item/list/carrousel/block/main.html 
    title="Core values and guiding principles"
    items=page.core_principles 
%}

{% include item/list/card/colored/main.html 
    title="Priority areas of action"
    items=page.priorities 
%}

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
