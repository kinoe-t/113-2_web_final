<!DOCTYPE html>
<html lang="zh-Hant">
<head>
  <meta charset="UTF-8">
  <title>抽一個幹片看看！</title>
  <style>
    body {
      font-family: 'Noto Sans TC', sans-serif;
      background-color: #fefefe;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
      margin: 0;
      padding: 20px;
    }
    h1 {
      margin-bottom: 20px;
    }
    button {
      padding: 12px 24px;
      font-size: 1.2em;
      background-color: #b583d6;
      color: #fff;
      border: none;
      border-radius: 8px;
      cursor: pointer;
    }
    button:disabled {
      opacity: 0.6;
      cursor: not-allowed;
    }
    #result {
      margin-top: 30px;
      font-size: 1.1em;
      text-align: center;
    }
  </style>
</head>
<body>

  <h1>抽一個幹片看看！</h1>
  <button onclick="draw()">開始抽幹片</button>
  <div id="result"></div>

  <script>
    const memes = [
      { name: '不會讓你上', url: 'https://www.youtube.com/embed/dQw4w9WgXcQ' },
      { name: '中立國特殊課程', url: 'https://www.youtube.com/watch?v=G2NngxegUBc' },
      { name: '這樣太危險', url: 'https://www.youtube.com/watch?v=1GG3YQ0P5_Y' },
      { name: '雲門舞集', url: 'https://www.youtube.com/watch?v=ZkNMZlkrzaU' },
      { name: 'Die with a smile', url: 'https://www.youtube.com/watch?v=1bd4XSNGvJc' },
      { name: '怎麼愛你都不嫌多', url: 'https://www.youtube.com/watch?v=FtutLA63Cp8' },
    { name: '多喝水', url: 'https://www.youtube.com/watch?v=ZlHRhzXezAc' },
      { name: '高級海鮮', url: 'https://www.youtube.com/watch?v=ywthKNqI7uI' },
      { name: '侏羅紀世界', url: 'https://www.youtube.com/watch?v=q6EoRBvdVPQ' },
      { name: '細胞壁', url: 'https://www.youtube.com/watch?v=Zd8bNW4DG5E' },
      { name: '進擊的巨人', url: 'https://www.youtube.com/watch?v=yBLdQ1a4-JI' },
      { name: '黃猿', url: 'https://www.youtube.com/watch?v=NfuiB52K7X8' },
      { name: '阿罵', url: 'https://www.youtube.com/embed/ZhLDlYkb1K4' },
      { name: '你鄰居很生氣', url: 'https://www.youtube.com/watch?v=dE7DCF_s7HQ' },
      { name: '芒果美語', url: 'https://www.youtube.com/watch?v=fzDZrPZ8s5c' },
      { name: '印度浦島太郎', url: 'https://www.youtube.com/watch?v=SfT4FMkh1-w' },
      { name: '牛奶好棒棒', url: 'https://www.youtube.com/watch?v=nOJd3xoKMyI' },
      { name: '萬年不敗音質', url: 'https://www.youtube.com/watch?v=IOOvanZ-RYk' },
      { name: '鼻塞什麼眼', url: 'https://www.youtube.com/watch?v=vFef_Dp0Vfc' },
      { name: '竟然！', url: 'https://www.youtube.com/watch?v=y8Kyi0WNg40' },
      { name: '讚', url: 'https://www.youtube.com/watch?v=lg5WKsVnEA4' },
      { name: 'ㄣˋ', url: 'https://www.youtube.com/watch?v=lgh6p-JySK4' },
      { name: '拉拉拉拉', url: 'https://www.youtube.com/watch?v=6xbEmdgNQJQ' },
      { name: '雞腿換駕照', url: 'https://www.youtube.com/watch?v=7VFTcmGRM-k' },
      { name: '不可以', url: 'https://www.youtube.com/shorts/cPa0db6A9uc' },
      { name: '唧唧復唧唧', url: 'https://www.youtube.com/watch?v=WdA8AWKGE8w' },
      { name: '喔喔喔喔喔喔喔喔', url: 'https://www.youtube.com/embed/Qkfyr-UpUp0' },
      { name: '鳥', url: 'https://www.youtube.com/watch?v=nd0DtRU6M_c' },
      { name: '才沒有黃腔', url: 'https://www.youtube.com/watch?v=mBw3qzf4s18' },
      { name: 'That’s beautiful ', url: 'https://www.youtube.com/watch?v=e0OggOfjiUE' },  
      { name: '小尖頭', url: 'https://www.youtube.com/embed/o7zqouVuFZY' },
      { name: '丹丹漢堡', url: 'https://www.youtube.com/watch?v=CxoXItNERPM' },
      { name: '嘟嘟嘟', url: 'https://www.youtube.com/embed/BbeeuzU5Qc8' },
    ];

    function draw() {
      const result = memes[Math.floor(Math.random() * memes.length)];
      const videoId = extractYouTubeID(result.url);

      if (videoId) {
        document.getElementById('result').innerHTML = `
          <strong>你抽到了：${result.name}</strong><br>
          <iframe width="560" height="315"
            src="https://www.youtube.com/embed/${videoId}"
            title="YouTube video player" frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen>
          </iframe>
        `;
      } else {
        document.getElementById('result').innerHTML =
          `<strong>你抽到了：${result.name}</strong><br>這個影片沒有連結喔！`;
      }
    }

    function extractYouTubeID(url) {
      if (!url) return null;
      const regex = /(?:youtube\.com\/(?:watch\?v=|embed\/|shorts\/)|youtu\.be\/)([a-zA-Z0-9_-]{11})/;
      const match = url.match(regex);
      return match ? match[1] : null;
    }
  </script>

</body>
</html>
