# Polytext

![polytext-example.png](https://wiki.cryptovoxels.com/polytext-example.png)

## Editor 编辑器

![polytext-editor.png](https://wiki.cryptovoxels.com/polytext-editor.png)

### Text 文本

polytext 的文本

### Color 颜色

polytext 的颜色

### Edges 边

polytext是否会用黑边勾勒出轮廓。

![polytext-edges.png](https://wiki.cryptovoxels.com/polytext-edges.png)

# Scripting Properties
# Scripting Properties {.tabset}
## url
`String`; 

### get()

```js
feature.get('text')
// returns: "My new text"
```

### set()

```js
feature.set({'text':"My new text"})
```

### default

`""`


## edges
`Boolean`

### get()

```js
feature.get('edges')
// returns: false
```

### set()

```js
feature.set({'edges': true})
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
// returns: "polytext"
```

