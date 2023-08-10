---
layout: default
permalink: /publications/
title: Open Science publications
---

(side-note: this page doesn't work with includes from the theme --> would opt to this)
## Zenodo community

Check out our collection of open science publications on [zenodo](https://zenodo.org/communities/vliz-openscience/)

<div hx-ext="client-side-templates">
    <div 
    hx-get="https://zenodo.org/api/records/?page=1&size=1000&communities=vliz-openscience&sort=mostrecent"
    hx-trigger="load"
    hx-target="#zenodo"
    nunjucks-template="gistlist"
    hx-swap="innerHTML"
    >
    </div>
<script id="gistlist" type="nunjucks">
    \{\{data\}\}
    \{\{.\}\}
    <p>\{\{data\}\}</p>
  </script>
    <div id="zenodo">
    </div>
  </div>

## Scientific Papers
<table style="background-color: #fff7d010;">
    <thead style="background-color: #f7c97c;">
        <tr>
            <th>Title</th>
            <th>Authors</th>
            <th>Abstract</th>
            <th>Date</th>
            <th>Journal</th>
            <th>Access</th>
        </tr>
    </thead>
    <tbody>

    {% for pub in site.data.publications.scientificPapers %}

    <tr style="border-bottom: #f7c97c solid 2px;">
        <td><a href="{{pub.url}}" target="_blank">{{ pub.title }}</a></td>
        <td>{{ pub.authors }}</td>
        <td>{{ pub.abstract }}</td>
        <td>{{ pub.date }}</td>
        <td>{{ pub.journal }}</td>
        <td>{{ pub.access }}</td>
    </tr>

    {% endfor %}

    </tbody>
</table>
<p></p>

## Conference Proceedings

Same here for the conference proceedings ?

{% for pub in site.data.publications.conferenceProceedings %}
<p>{{pub.title}}</p>
{% endfor %}

<script>
    htmx.logger = function(elt, event, data) {
        if(console) {
            console.log(event, elt, data);
        }
    }
  
  document.body.addEventListener('configRequest.htmx', function(evt) {
      // try to remove x-hx-* headers because gist api complains about CORS
      Object.keys(evt.detail.headers).forEach(function(key) { 
        delete evt.detail.headers[key]; 
      });
  });
  
  htmx.defineExtension('client-side-templates', {
      transformResponse : function(text, xhr, elt) {
        var nunjucksTemplate = htmx.closest(elt, "[nunjucks-template]");
          if (nunjucksTemplate) {
              var data = {
                data: JSON.parse(text)
              };
              var templateName = nunjucksTemplate.getAttribute('nunjucks-template');
              var template = htmx.find('#' + templateName);
              console.log(templateName,data);
              return nunjucks.renderString(template.innerHTML, data);
          }
          return text;
      }
  });
</script>