---
layout: default
title: Tools
permalink: /tools/
---

# Tools

All opsci-vliz tools are open source blabla ...

<div class="col-12 field__item">
  <div class="background-light-2 container-full-width pb-6 pt-6 paragraph paragraph--type--container paragraph--view-mode--default">
    <div class="field field--name-field-paragraph-container-items field--type-entity-reference-revisions field--label-hidden">
      <div class="row field__items">
        <div class="col-12 field__item">
          <div  class="ticker-count-3 ticker-autoplay ticker-nav paragraph paragraph--type--ticker paragraph--view-mode--default">
            <div class="ticker-items field field--name-field-paragraph-container-items field--type-entity-reference-revisions field--label-hidden">
              <div class="field__items">
                {%assign data=site.data.tools%}
                {%for tool in data%}
                 <div class="field__item">
                    <div class="paragraph paragraph--type--basic-text paragraph--view-mode--default">
                        <div
                        class="clearfix text-formatted field field--name-field-body field--type-text-long field--label-hidden field__items">
                        <h2 class="highlighted-heading text-align-center">{{ tool.title }}</h2>
                        <p class="text-align-center">{{ tool.short-description }}</p>
                        <p class="text-align-center">
                            <a class="more-link" href="{{ tool.url }}">{{ tool.title }}</a>
                        </p>
                        </div>
                    </div>
                </div>
                {%endfor%}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>