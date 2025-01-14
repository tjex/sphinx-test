# Note formats

To keep your notebooks [future-proof](future-proof.md), `zk` uses a simple plain
text format for your notes. Only Markdown is supported at the moment, but more
formats may be added in the future.

## Markdown

You can set up some features of `zk`'s Markdown parser from your
[configuration file](config.md), under the `[format.markdown]` section.

| Setting               | Default         | Description                                                                    |
| --------------------- | --------------- | ------------------------------------------------------------------------------ |
| `link-format`         | `"markdown"`    | Format used to generate internal links (`markdown`, `wiki` or custom template) |
| `link-encode-path`    | `-`<sup>1</sup> | Percent-encode paths of generated internal links                               |
| `link-drop-extension` | `true`          | Remove the path file extension of generated internal links                     |
| `hashtags `           | `true`          | Enable `#hashtags` support                                                     |
| `colon-tags`          | `false`         | Enable `:colon:separated:tags:` support                                        |
| `multiword-tags`      | `false`         | Enable Bear's [`#multi-word tags#`][1]. Hashtags must also be enabled.         |

1. Paths are not percent-encoded by default, unless the `link-format` is
   `markdown`.

[1]: https://blog.bear.app/2017/11/bear-tips-how-to-create-multi-word-tags/

### Customizing the Markdown links generated by `zk`

By default, `zk` will generate regular Markdown links for internal links. If you
prefer to use `[[Wiki Links]]` instead, set the `link-format` setting to `wiki`.
If you want to override completely the link format, you can also set
`link-format` to a [custom template](template.md). For example, to generate a
wiki link using an ID from the frontmatter and a title:

```toml
[format.markdown]
link-format = "[[{{metadata.id}}|{{title}}]]"
```

The following variables are available in the template:

| Variable   | Type   | Description                                               |
| ---------- | ------ | --------------------------------------------------------- |
| `filename` | string | Filename of the note                                      |
| `path`     | string | File path to the note, relative to the notebook directory |
| `abs-path` | string | Absolute file path to the note                            |
| `rel-path` | string | File path to the note, relative to the current directory  |
| `title`    | string | Note title                                                |
| `metadata` | map    | YAML frontmatter metadata, e.g. `metadata.id`<sup>1</sup> |

1. YAML keys are normalized to lower case.
