HEARTBEATS Fravored Markdown extension
=========================================

- Inline Coloring
- Inline List
- Cross Reference

# Inline Coloring

```
{{color(red)::some_text}}
```

![](README.assets/red.png)

```
{{color(blue)::some_text}}
```

![](README.assets/blue.png)

`mkdocs.yml` example:

```yaml
markdown_extensions:
  - hbfm.inline_coloring
```

# Inline List

List in Table.

```
|a|b|c|d|
|:---|---:|---|:---:|
|左寄せ|右寄せ|寄せ指定なし|中央寄せ|
|左寄せ|右寄せ|{{inline(list)::
- a
- b
- c
}}|中央寄せ|
|左寄せ|右寄せ|寄せ指定なし|中央寄せ|
```

![](README.assets/inline_list.png)

`mkdocs.yml` example:

```yaml
markdown_extensions:
  - hbfm.inline_list
```

# Internal Link / Cross Reference

Link from `[Some Text](#Some Text)` to `## Some Text` .

`mkdocs.yml` example:

```yaml
markdown_extensions:
  - toc:
      slugify: !!python/name:hbfm.toc.slugify
  - hbfm.number_headers
  - hbfm.quote_uri_hash
```
