<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Dino Game</title>
  <style>
    html, body {
      margin: 0;
      padding: 0;
      overflow: hidden;
      background: #fff;
    }
    canvas {
      display: block;
    }
    #gameOver {
      position: absolute;
      top: 40%;
      width: 100%;
      text-align: center;
      font-size: 48px;
      color: red;
      font-family: Arial, sans-serif;
      display: none;
    }
    #restart {
      position: absolute;
      top: 55%;
      width: 100%;
      text-align: center;
      font-size: 24px;
      font-family: Arial, sans-serif;
      display: none;
    }
  </style>
</head>
<body>
  <canvas id="game" width="800" height="400"></canvas>
  <div id="gameOver">Finis Ludus</div>
  <div id="restart">Press ↑ to restart</div>

  <script>
    const canvas = document.getElementById("game");
    const ctx = canvas.getContext("2d");

    const dinoImg = new Image();
    dinoImg.src = "dino.png";

    const obstacleImg = new Image();
    obstacleImg.src = "obstacle.png";

    const bgImg = new Image();
    bgImg.src = "background.png";

    let dino = { x: 50, y: 300, width: 50, height: 50, vy: 0, jumping: false };
    let gravity = 1.5;
    let jumpPower = -20;

    let obstacle = { x: 800, y: 310, width: 40, height: 40, speed: 6 };

    let bgX = 0;

    let score = 0;
    let gameOver = false;

    function resetGame() {
      dino.y = 300;
      dino.vy = 0;
      dino.jumping = false;
      obstacle.x = 800;
      score = 0;
      gameOver = false;
      document.getElementById("gameOver").style.display = "none";
      document.getElementById("restart").style.display = "none";
      loop();
    }

    function drawBackground() {
      bgX -= 2;
      if (bgX <= -canvas.width) bgX = 0;
      ctx.drawImage(bgImg, bgX, 0, canvas.width, canvas.height);
      ctx.drawImage(bgImg, bgX + canvas.width, 0, canvas.width, canvas.height);
    }

    function drawDino() {
      ctx.drawImage(dinoImg, dino.x, dino.y, dino.width, dino.height);
    }

    function drawObstacle() {
      ctx.drawImage(obstacleImg, obstacle.x, obstacle.y, obstacle.width, obstacle.height);
    }

    function drawScore() {
      ctx.fillStyle = "black";
      ctx.font = "20px Arial";
      ctx.fillText("Score: " + Math.floor(score), 650, 30);
    }

    function checkCollision() {
      return (
        dino.x < obstacle.x + obstacle.width &&
        dino.x + dino.width > obstacle.x &&
        dino.y < obstacle.y + obstacle.height &&
        dino.y + dino.height > obstacle.y
      );
    }

    function loop() {
      if (gameOver) return;

      ctx.clearRect(0, 0, canvas.width, canvas.height);
      drawBackground();

      // Dino physics
      dino.vy += gravity;
      dino.y += dino.vy;
      if (dino.y >= 300) {
        dino.y = 300;
        dino.jumping = false;
      }

      // Obstacle movement
      obstacle.x -= obstacle.speed;
      if (obstacle.x < -obstacle.width) {
        obstacle.x = 800 + Math.random() * 200;
      }

      drawDino();
      drawObstacle();
      drawScore();

      // Increase score
      score += 0.1;

      if (checkCollision()) {
        gameOver = true;
        document.getElementById("gameOver").style.display = "block";
        document.getElementById("restart").style.display = "block";
        return;
      }

      requestAnimationFrame(loop);
    }

    document.addEventListener("keydown", (e) => {
      if (e.key === "ArrowUp") {
        if (!gameOver && !dino.jumping) {
          dino.vy = jumpPower;
          dino.jumping = true;
        } else if (gameOver) {
          resetGame();
        }
      }
    });

    window.onload = () => {
      loop();
    };
  </script>
</body>
</html>
