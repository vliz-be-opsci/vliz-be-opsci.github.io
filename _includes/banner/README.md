## Banner

### Usage

```html
{% include banner/banner.html %}
```

### Options

| Option | Description | Type | Default |
| ------ | ----------- | ---- | ------- |
| `banner` | Banner object | Object | `null` |
| `banner.title` | Banner title | String | `null` |
| `banner.description` | Banner description | String | `null` |
| `banner.media` | Banner image or viedo | String | `/assets/media/video/Homepage_website_SimonStevin.mp4` |
| `banner.clickthrough_url` | Banner clickthrough url | String | `null` |
| `banner.clickthrough_text` | Banner clickthrough text | String | `null` |
| `banner.quotes` | Banner quotes | Object | `null` | 
| `banner.quotes.title` | Banner quotes title | String | `null` |
| `banner.quotes.clickthrough_url` | Banner quotes clickthrough url | String | `null` |
| `banner.quotes.clickthrough_text` | Banner quotes clickthrough text | String | `null` |
| `banner.topics` | Banner topics | Object | `null` |
| `banner.topics.title` | Banner topics title | String | `null` |
| `banner.topics.clickthrough_url` | Banner topics clickthrough url | String | `null` |
| `banner.topics.clickthrough_text` | Banner topics clickthrough text | String | `null` |
| `banner.topics.image` | Banner topics image | String | `null` |
| `banner.topics.colw` | Banner topics column width | String | `4` |

### Example with options
<>
```yml
---
banner:
  title: "Open Science"
  quotes:
    - title: " ...90% of scientists agreeing that the replicability crisis is real"
      clickthrough_text: "Hensel, 2023"
      clickthrough_url: "https://www.tandfonline.com/action/showCitFormats?doi=10.1080%2F08989621.2021.1981870"
    - title: " The replication crisis has stimulated a movement for open science, encouraging or even requiring researchers to publish their raw data and analysis code... One common response to the replication crisis has been to call for open science"
      clickthrough_text: "Hicks, 2021"
      clickthrough_url: "https://www.tandfonline.com/doi/full/10.1080/08989621.2021.1962713"
  clickthrough_text: "More About The VLIZ approach"
  clickthrough_url: "/open-science"
  media: "/assets/media/img/cover/graph-nodes-blue-gradient.webp"
  topics:
    - title: "Open Science Topics"
      clickthrough_text: "More About The VLIZ approach"
      clickthrough_url: "/open-science"
      image: "/assets/media/img/open-science-logo-flask.svg"
      colw: "4"
   -  title: "Open Science Topics"
      clickthrough_text: "More About The VLIZ approach"
      clickthrough_url: "/open-science"
      image: "/assets/media/img/open-science-logo-flask.svg"
      colw: "4"
---
{% include banner/banner.html banner=page.banner %}
```