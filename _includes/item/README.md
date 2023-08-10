These nested templates visualise so called 'items' in different ways

## Which ones to use:

### item/block/colored
Renders each item in a 1/3rd block with a prominent background color from the vliz-scheme.
Only shows title and applies click-through.

### item/row/logo_text_link
Renders each item in a full row with 1-9-2 dsitributed cells.
These hold: image | title/tags + description | specific links


## way to use them

These all expect an attribute items=... to be passed into them that looks like this

```yml
items:
  - title: «required label for the thing»
    description: «optional description - not all templates use this»
    clickthrough_url: «optional link to follow»
    tags:
      - «optional tag#1»
      - «optional tag#2»
    more_url:
      gith: «github-url»
      pypi: «pypi-url»
      demo: «demo-url»
      docs: «docs-link»

```


