These nested templates visualise so called 'items' in different ways

## Which ones to use:

### item/block/colored
Renders each item in a 1/3rd block with a prominent background color from the vliz-scheme.
Only shows title and applies click-through.

### item/row/logo_text_link
Renders each item in a full row with 1-9-2 dsitributed cells.
These hold: image | title/tags + description | specific links

### item/carrousel/block
Renders each item as a block in a carrousel.
These blocks hold title and description.

### item/carrousel/waved
Renders each item as a block in a carrousel. Blocks-bottoms are wave-shaped.
These blocks hold title and description.


## way to use them

Some of these (see above) will take an additional title= 

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

## way to implement additional ones

* documentation 
  * add docs here
* css pickup, make sure to
  * introduce a div.included-item around the smallest group of tags that makes up one item
  * introduce a div.included-item-list.«your-name-here» around the included items
