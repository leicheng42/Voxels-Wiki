# Slider Input 滑动输入

让用户输入一定范围内的数值。

![example_v5.18.png](https://wiki.cryptovoxels.com/features/[slider_input]example_v5.18.png)

## Editor 编辑器
![editor_7.18.2.png](https://wiki.cryptovoxels.com/features/[slider_input]editor_7.18.2.png)

### Text 文本

滑块输入上方的文本。

# Scripting Properties
# Scripting Properties {.tabset}
## value
`String`; 

### get()

```js
feature.get('value')
// returns: the value of the slider
```

### set()

```js
feature.set({'value':0.2})
```

### default

`0.25`

## text
`String`; 

### get()

```js
feature.get('text')
// returns the text above the slider
```

### set()

```js
feature.set({'text':"my text"})
```

### default

`""`

## minimum
`number`; 

### get()

```js
feature.get('minimum')
// returns: the minimum value of the slider
```

### set()

```js
feature.set({'minimum':0.01}) // a minimum of 0 will not work
```

### default

`0.01`

## maximum
`number`; 

### get()

```js
feature.get('maximum')
// returns: the maximum value of the slider
```

### set()

```js
feature.set({'maximum':1})
```

### default

`1`


## type
`String`;

### get()

```js
feature.get('type')
/* or */
feature.type

// returns: 'slider-input'
```
