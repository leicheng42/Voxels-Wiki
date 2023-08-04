# Megavox 巨型Vox

Megavoxes是一个大小为126x126x126 `.vox` 模型，目前每个地块Parcel限制为5个。

![megavox-example.png](https://wiki.cryptovoxels.com/megavox-example.png)

## Editor 编辑器

![megavox-editor.png](https://wiki.cryptovoxels.com/megavox-editor.png)

### URL

`.vox` 文件的 URL。

### Hyperlink 超链接

`（可选）`；使 megavox 成为可点击的链接。

# Scripting Properties
# Scripting Properties {.tabset}
## url
`String`; Links must be `https://` and must finish with a vox extension `.vox`
Has to link to a 126x126x126 vox model.

### get()

```js
feature.get('url')
// returns: "https://..."
```

### set()

```js
feature.set({'url':"https://www.myurl.com/file.vox"})
```

### default

`""`

## link
`String`; Links must be `https://`.

### get()

```js
feature.get('link')
// returns: "https://..."
```

### set()

```js
feature.set({'link':"https://www.myurl.com/"})
```

### default

`""`

## collidable
`Boolean`

### get()

```js
feature.get('collidable')
// returns: false
```

### set()

```js
feature.set({'collidable': true})
```

### default

`false`

## type
`String`;

### get()

```js
feature.get('type')
/* or */
feature.type

// returns: 'megavox'
```