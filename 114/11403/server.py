<!DOCTYPE html>
<html lang="zh-Hant">
<head>
  <meta charset="UTF-8" />
  <title>釣魚遊戲</title>
  <style>
    body {
      margin: 0;
      font-family: "Arial", sans-serif;
      background: linear-gradient(to top, #87ceeb, #ffffff);
      overflow: hidden;
    }
    #game-container {
      position: relative;
      width: 100vw;
      height: 100vh;
      overflow: hidden;
    }
    #hook {
      position: absolute;
      width: 50px;
      height: auto;
      top: 0;
      left: 50%;
      transform: translateX(-50%);
      transition: top 0.3s;
    }
    .fish {
      position: absolute;
      width: 80px;
      height: auto;
      animation: swim 6s linear infinite;
    }
    @keyframes swim {
      from {
        left: -100px;
      }
      to {
        left: 110%;
      }
    }
    #start-button {
      position: absolute;
      top: 20px;
      left: 20px;
      padding: 10px 20px;
      font-size: 18px;
      z-index: 10;
    }
    #score-board {
      position: absolute;
      top: 20px;
      right: 20px;
      font-size: 18px;
      background: rgba(255,255,255,0.7);
      padding: 10px;
      border-radius: 10px;
    }
  </style>
</head>
<body>
  <div id="game-container">
    <button id="start-button">開始釣魚</button>
    <div id="score-board">分數：0<br>時間：60</div>
    <img src="魚鉤.jfif" id="hook" />
    <audio id="bg-music" loop>
      <source src="relax.mp3" type="audio/mpeg" />
      您的瀏覽器不支援音樂播放。
    </audio>
  </div>

  <script>
    const startBtn = document.getElementById('start-button');
    const hook = document.getElementById('hook');
    const container = document.getElementById('game-container');
    const scoreBoard = document.getElementById('score-board');
    const music = document.getElementById('bg-music');

    const fishTypes = [
      { src: '尼莫.jpg', score: 1 },
      { src: '多莉.jpg', score: 2 },
      { src: '海龜.jpg', score: 3 },
      { src: '神仙魚.jpg', score: -1 }
    ];

    let score = 0;
    let timeLeft = 60;
    let gameInterval, timerInterval;

    function startGame() {
      score = 0;
      timeLeft = 60;
      updateScoreBoard();
      music.play();
      hook.style.top = '50%';

      gameInterval = setInterval(spawnFish, 1200);
      timerInterval = setInterval(() => {
        timeLeft--;
        updateScoreBoard();
        if (timeLeft <= 0) {
          endGame();
        }
      }, 1000);
    }

    function endGame() {
      clearInterval(gameInterval);
      clearInterval(timerInterval);
      music.pause();
      alert(`時間到！你的分數是 ${score}`);
      document.querySelectorAll('.fish').forEach(f => f.remove());
    }

    function updateScoreBoard() {
      scoreBoard.innerHTML = `分數：${score}<br>時間：${timeLeft}`;
    }

    function spawnFish() {
      const fishData = fishTypes[Math.floor(Math.random() * fishTypes.length)];
      const fish = document.createElement('img');
      fish.src = fishData.src;
      fish.className = 'fish';
      fish.style.top = `${Math.random() * 80 + 10}%`;
      container.appendChild(fish);

      // 移除游出畫面的魚
      setTimeout(() => fish.remove(), 7000);

      // 點擊魚鉤時判斷有無魚在範圍
      fish.addEventListener('click', () => {
        const hookRect = hook.getBoundingClientRect();
        const fishRect = fish.getBoundingClientRect();
        if (Math.abs(fishRect.top - hookRect.top) < 40 && Math.abs(fishRect.left - hookRect.left) < 40) {
          score += fishData.score;
          updateScoreBoard();
          fish.remove();
        }
      });
    }

    // 點擊畫面移動魚鉤
    container.addEventListener('click', (e) => {
      const y = e.clientY;
      hook.style.top = `${y}px`;
    });

    startBtn.addEventListener('click', () => {
      startGame();
    });
  </script>
</body>
</html>
