# Boombox 扬声器
A boombox allows you to stream audio from your computer into the world. To use a boombox, simply click on it and then select `Start Broadcasting` from the pop-up.
扬声器可让您将声音传输到世界中。要使用扬声器，只需单击它，然后从弹出窗口中选择“开始广播”。

![boombox-feature-double.png](https://wiki.cryptovoxels.com/boombox-feature-double.png)
## 编辑器
![boombox_editor_v4.25.png](https://wiki.cryptovoxels.com/boombox_editor_v4.25.png)

### Spatial roll off 空间衰减

当玩家离开音频播放器时声音消失的速度。
值在 0 到 5 之间。

# Scripting Properties
# Scripting Properties {.tabset}
## rollOffFactor
`Double`; Value ranging from 0 to 5

### get()

```js
feature.get('rolloffFactor')
// returns: 1.6
```

### set()

```js
feature.set({'rolloffFactor':1.6})
```

### default

`1`

# How to use?
Click on the Boombox and hit start Broadcasting
![boombox-broadcast.png](https://wiki.cryptovoxels.com/boombox-broadcast.png)

