# 音频

音频功能是一个 MP3 的小播放器。您可以链接到任何 mp3，我们将尝试对其进行流式传输。

![audio-feature.png](https://wiki.cryptovoxels.com/audio-feature.png)

## 编辑器

![editor_v8.1.png](https://wiki.cryptovoxels.com/features/[audio]editor_v8.1.png)

### Sprite 小画面

显示一个较小的音频元素

### Streaming 流式传输

直接流式传输音频，无需通过我们的服务器进行代理。应该可以加快音频播放速度，但如果您在托管服务器上有奇怪的规则，则可能不行。

### Autoplay  自动播放

一旦有人进入您的包裹，立即开始播放这段音频。（拥有权利的同时也被赋予了重大的责任）。

### Loop 循环

始终循环播放。

### Spatial rolloff factor 空间衰减因子

当玩家离开音频播放器时声音消失的速度。
值在 0 到 5 之间。

### Volume 音量

音频的声音的大小
值在0到1之间。

### URL

Links must be `https://` since we force https:// for everything.
链接必须是 `https://` 开头，因为我们强制所有东西都是  `https://` 。

# Scripting Properties
# Scripting Properties {.tabset}
## url
`String.`; Links must be `https://` and must finish with an audio extension such as `.mp3`

### get()

```js
feature.get('url')
// returns: "https://..."
```

### set()

```js
feature.set({'url':"https://www.myurl.com/file.mp3"})
```

### default

`""`

## sprite
`Boolean.`

### get()

```js
feature.get('sprite')
// returns: false
```

### set()

```js
feature.set({'sprite': true})
```

### default

`false`

## streaming
`Boolean.`

### get()

```js
feature.get('streaming')
// returns: false
```

### set()

```js
feature.set({'streaming': true})
```
### default

`false`

## autoplay
`Boolean.`

### get()

```js
feature.get('autoplay')
// returns: false
```

### set()

```js
feature.set({'autoplay': true})
```
### default

`false`

## loop
`Boolean.`

### get()

```js
feature.get('loop')
// returns: false
```

### set()

```js
feature.set({'loop': true})
```

### default

`false`

## rolloffFactor
`double`; Value ranging from 0 to 5

### get()

```js
feature.get('rolloffFactor')
// returns: 1.6
```

### set()

```js
feature.set({'rolloffFactor': 1.6})
```

### default
`1.6`

## volume
`double`; Value ranging from 0 to 1

### get()

```js
feature.get('volume')
// returns: 0.5
```

### set()

```js
feature.set({'volume': 0.5})
```

### default
`0.5`

## type
`String`;

### get()

```js
feature.get('type')
/* or */
feature.type

// returns: 'audio'
```

# Scripting Methods

::::{tab-set}

:::{tab-item} play()
```js
feature.play()
```
plays the audio
:::

:::{tab-item} pause()
```js
feature.pause()
```
pauses the audio
:::

:::{tab-item} stop()
```js
feature.stop()
```
stops the audio
:::

::::


::::{tab-set}

:::{tab-item} Label1
Content 1
:::

:::{tab-item} Label2
Content 2
:::

::::


::::::{myst-example}

::::{tab-set}

:::{tab-item} Label1
Content 1
:::

:::{tab-item} Label2
Content 2
:::

::::

::::::

# Scripting Methods
# Scripting Methods {.tabset}
## play()
```js
feature.play()
```
plays the audio

## pause()
```js
feature.pause()
```
pauses the audio

## stop()
```js
feature.stop()
```
stops the audio