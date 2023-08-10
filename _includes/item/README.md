These nested templates visualise so called 'items' in different ways


## Which ones to use:

### item/block/colored
Gives each block a prominent background color from the vliz-scheme.
Only shows title and applies click-through.


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

```


