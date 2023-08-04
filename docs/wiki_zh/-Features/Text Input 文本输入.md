
> 自 v 5.0 以来已重新引入该功能
{.is-info}
# Text Input 文本输入

让用户输入消息。
![text-input-feature.png](https://wiki.cryptovoxels.com/text-input-feature.png)

## Editor 编辑器

![text-input-editor.png](https://wiki.cryptovoxels.com/text-input-editor.png)

### Placeholder 占位符

当没有用户输入时显示为占位符的文本。


# Scripting Properties
# Scripting Properties {.tabset}
## text
`String`; 

### get()

```js
feature.get('text')
// returns: "my text"
```

### set()

```js
feature.set({'text':"my text"})
```

### default

`""`

## placeholder
`String`; 

### get()

```js
feature.get('placeholder')
// returns: "my text"
```

### set()

```js
feature.set({'placeholder':"my text"})
```

### default

`"placeholder"`

## type
`String`;

### get()

```js
feature.get('type')
/* or */
feature.type

// returns: 'text-input'
```
