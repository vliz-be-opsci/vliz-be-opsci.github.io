### Navigation

This is the navigation for the site. It is a list of links to other pages on the site. It is used in the default layout.

### Usage

```liquid
{% include navigation/main.html %}
```

### Options

| Option | Description | Type | Default |
| ------ | ----------- | ---- | ------- |
| `navigation` | Navigation object | Object | `null` |
| `navigation.title` | Navigation title | String | `null` |
| `navigation.url` | Navigation links | Object | `null` |
| `navigation.items` | Navigation items | Object | `null` |

#### items options

| Option | Description | Type | Default |
| ------ | ----------- | ---- | ------- |
| `items.title` | Navigation item title | String | `null` |
| `items.url` | Navigation item url | String | `null` |
| `items.items` | Navigation item items | Object | `null` |

### Example with options

in _data/navigation.yml add:

```yml
  - title: About
  url: /
  items:
    - title: Open Science
      url: /open-science
      items:
        - title: Open principles
          url: /open-science#principles
        - title: Ambitions
          url: /open-science#ambitions
        - title: Components
          url: /open-science#components
    - title: Across Departments
      url: /open-science-at-departments
      items:
        - title: Research
          url: /open-science-at-departments#research
        - title: Data Centre
          url: /open-science-at-departments#vmdc
        - title: Library
          url: /open-science-at-departments#lib
        - title: Policy and valorization
          url: /open-science-at-departments#innoval
        - title: Science Communication
          url: /open-science-at-departments#wcomm
    - title: FAIR & Open Data
      url: /fair-open-data
      items:
        - title: Vision
          url: /fair-open-data#vision
        - title: Technical approach
          url: /fair-open-data#technical
        - title: Examples
          url: /fair-open-data#examples

- title: Community
  items:
    - title: Partners
      url: /partners
    - title: Projects
      url: /projects
    - title: Initiatives
      url: /initiatives
      items:
        - title: Read the LOD
          url: https://readthelod.org/
        - title: RO-Crate Community
          url: https://www.researchobject.org/ro-crate/community.html
    - title: Events
      url: /events

- title: Achievements
  items:
    - title: Linked data
      url: /linked-data
      items:
        - title: marineinfo.org
          url: https://marineinfo.org/
        - title: marineregions.org
          url: https://www.marineregions.org/gazetteer.php?p=webservices
        - title: marinespecies.org
          url: https://www.marinespecies.org/
    - title: Applications & tools
      url: /applications-tools
      items:
        - title: DMBON Assistant
          url: /applications-tools/dmbon-assistant
        - title: RO-Crate demo
          url: /applications-tools/ro-crate-demo
        - title: Vocab Term Lookup
          url: /applications-tools/vocab-term-lookup
        - title: Software packages
          url: /applications-tools/software-packages
    - title: Publications
      url: /publications
    
- title: Documents
  items:
    - title: Conventions
      url: /conventions
      items:
        - title: Github management
          url: /conventions/github-management
        - title: Python
          url: /conventions/python
```