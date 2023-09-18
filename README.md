# vliz-be-theme

Welcome to your new Jekyll theme! In this directory, you'll find the files you need to be able to package up your theme into a gem. Put your layouts in `_layouts`, your includes in `_includes`, your sass files in `_sass` and any other assets in `assets`.

To experiment with this code, add some sample content and run `bundle exec jekyll serve` – this directory is setup just like a Jekyll site!

TODO: Delete this and the text above, and describe your gem

## Installation

Add this line to your Jekyll site's `Gemfile`:

```ruby
gem "vliz-be-theme"
```

And add this line to your Jekyll site's `_config.yml`:

```yaml
theme: vliz-be-theme
```

And then execute:[README]

    $ bundle

Or install it yourself as:

    $ gem install vliz-be-theme

## Usage

### _includes

| Path | Description | Readme |
| ---- | ----------- | ------ |
| `_includes/banner` | Banner | [DOCUMENTATION](./_includes/banner/README.md) |
| `_includes/footer` | Footer | [DOCUMENTATION](./_includes/footer/README.md) |
| `_includes/item/list/block/colored` | List of items with a colored background blocks | [DOCUMENTATION](./_includes/item/list/block/colored/README.md) |
| `_includes/item/list/card/colored` | List of items with a colored background cards | [DOCUMENTATION](./_includes/item/list/card/colored/README.md) |
| `_includes/item/list/carrousel/block` | List of items with a carrousel of blocks | [DOCUMENTATION](./_includes/item/list/carrousel/block/README.md) |
| `_includes/item/list/carrousel/waved` | List of items with a carrousel with wavy background | [DOCUMENTATION](./_includes/item/list/carrousel/waved/README.md) |
| `_includes/item/list/gallery` | Compact list of items with a gallery | [DOCUMENTATION](./_includes/item/list/gallery/README.md) |
| `_includes/item/list/row/image_text_link` | Item with image, text and link | [DOCUMENTATION](./_includes/item/list/row/image_text_link/README.md) |
| `_includes/item/list/row/text_image` | Item with text, image | [DOCUMENTATION](./_includes/item/list/row/text_image/README.md) |
| `_includes/item/single/row_and_wave` | Item with text, image and wavy background | [DOCUMENTATION](./_includes/item/single/row_and_wave/README.md) |
| `_includes/navigation` | Navigation | [DOCUMENTATION](./_includes/navigation/README.md) |

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/[USERNAME]/vliz-be-theme. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](https://www.contributor-covenant.org/) code of conduct.

## Development

To set up your environment to develop this theme, run `bundle install`.

Your theme is setup just like a normal Jekyll site! To test your theme, run `bundle exec jekyll serve` and open your browser at `http://localhost:4000`. This starts a Jekyll server using your theme. Add pages, documents, data, etc. like normal to test your theme's contents. As you make modifications to your theme and to your content, your site will regenerate and you should see the changes in the browser after a refresh, just like normal.

When your theme is released, only the files in `_layouts`, `_includes`, `_sass` and `assets` tracked with Git will be bundled.
To add a custom directory to your theme-gem, please edit the regexp in `vliz-be-theme.gemspec` accordingly.

## License

The theme is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).
