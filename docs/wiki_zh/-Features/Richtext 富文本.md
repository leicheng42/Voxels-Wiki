# Richtext 富文本

Richtext 功能允许您显示多行格式化文本。但与 [signs](https://wiki.cryptovoxels.com/features/sign) 不同，它们不能用作超链接。

![richtext-example.png](https://wiki.cryptovoxels.com/richtext-example.png)

## Editor 编辑器

![richtext-editor.png](https://wiki.cryptovoxels.com/richtext-editor.png)

### Text 文本

您要显示的文本，采用 Markdown 格式。
> 可以使用 css 来设置文本样式，方法是在文本后面放置下面类似的内容：`{:style="color:red;background:green;font-size:18px"}`
{.is-info}

### Blend mode 混合模式

这用于确定文本如何与其后面的内容混合。可用选项有 `Combine 组合` 、`Multiply 乘法` 和 `Screen 屏幕` 。

### Inverted 反转

当勾选时，文本将以白色显示在黑色背景上，而不是相反。


# Scripting Properties
# Scripting Properties {.tabset}
## text
`String`; 

### get()

```js
feature.get('text')
// returns: "https://..."
```

### set()

```js
feature.set({'text':"my paragraph"})
```

### default

`""`
## blendMode
`String`

### get()

```js
feature.get('blendMode')
// returns: 'Combine'
```

### set()

```js
feature.set({'blendMode': 'Combine'})
```

### default

`"Multiply"`

## inverted
`Boolean`; 

### get()

```js
feature.get('inverted')
// returns: false
```

### set()

```js
feature.set({'inverted': true})
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

// returns: 'richtext'
```


