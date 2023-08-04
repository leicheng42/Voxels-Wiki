# YouTube / Twitch 油管&Twitch直播

嵌入 YouTube 视频/直播 或 Twitch 直播。

![youtube-example.png](https://wiki.cryptovoxels.com/youtube-example.png)

## Editor 编辑器

![youtube_editor_v4.25.png](https://wiki.cryptovoxels.com/youtube_editor_v4.25.png)

### Screen ratio 屏幕比例

视频的屏幕比例：`16:9` 或 `4:3`

### URL

要播放的视频的 YouTube/Twitch URL。

### Thumbnail url 缩略图URL

`（可选）` 让用户为视频设置自定义缩略图。

# Scripting Properties
# Scripting Properties {.tabset}
## url
`String`; Links must be `https://` and must either be a `youtube, twitch, soundcloud, spotify`.

### get()

```js
feature.get('url')
// returns: "https://..."
```

### set()

```js
feature.set({'url':"https://www.youtube.com/?v=..."})
```

### default

`""`

## previewUrl
`String`; Links must be `https://` and must either be a `.png,.gif,jpg`.

### get()

```js
feature.get('previewUrl')
// returns: "https://..."
```

### set()

```js
feature.set({'previewUrl':"https://..."})
```

### default

`""`

## screenRatio
`String`; Links must be `https://` and must either be a `.png,.gif,jpg`.

### get()

```js
feature.get('screenRatio')
// returns: "43"
```

### set()

```js
feature.set({'screenRatio':"169"})
```

### default

`"169"`

## type
`String`;

### get()

```js
feature.get('type')
/* or */
feature.type

// returns: 'youtube'
```

# Scripting methods
# Scripting methods {.tabset}

## play()

```js
feature.play()
```
plays the video

## feature.pause()
```js
feature.pause()
```
pauses the video