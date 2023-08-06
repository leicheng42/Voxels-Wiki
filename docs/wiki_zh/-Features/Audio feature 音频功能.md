(audio)=
# 音频 Audio

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

链接必须是 `https://` 开头，因为我们强制所有东西都是  `https://` 。

## 脚本属性
::::{tab-set}

:::{tab-item} url

`String.`; 链接必须是以 `https://` 开头，并缺必须是以音频扩展后缀结尾，例如 `.mp3`

**get()**

```js
feature.get('url')
// returns: "https://..."
```

**set()**

```js
feature.set({'url':"https://www.myurl.com/file.mp3"})
```

**default**

`""`
:::

:::{tab-item} sprite
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

:::

:::{tab-item} streaming
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

:::

:::{tab-item} autoplay
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

:::

:::{tab-item} loop
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

:::

:::{tab-item} rolloffFactor
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

:::

:::{tab-item} volume
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

:::

:::{tab-item} type
`String`;

### get()

```js
feature.get('type')
/* or */
feature.type

// returns: 'audio'
```

:::
::::

## 脚本方法

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