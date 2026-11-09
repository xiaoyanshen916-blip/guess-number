 <!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>猜数字</title>
<style>
body{font-family:sans-serif;max-width:400px;margin:40px auto;padding:0 20px;text-align:center}
input,button{font-size:20px;padding:10px;margin:5px}
#msg{font-size:20px;min-height:30px}
</style>
</head>
<body>
<h1>猜数字</h1>
<p>我想了一个 1 到 100 的数,你有 7 次机会!</p>
<input id="guess" type="number" inputmode="numeric">
<button onclick="play()">猜</button>
<p id="msg"></p>
<button id="again" onclick="start()" style="display:none">再玩一局</button>
<script>
let answer, count, max = 7;

function start() {
  answer = Math.floor(Math.random() * 100) + 1;
  count = 0;
  msg.textContent = "";
  guess.value = "";
  guess.disabled = false;
  again.style.display = "none";
}

function play() {
  const g = parseInt(guess.value);
  if (isNaN(g)) { msg.textContent = "请输入数字"; return; }
  count++;
  const left = max - count;
  if (g === answer) end("猜对了!你用了 " + count + " 次");
  else if (left === 0) end("没猜中,答案是 " + answer);
  else msg.textContent = (g < answer ? "小了" : "大了") + ",还剩 " + left + " 次";
  guess.value = "";
}

function end(text) {
  msg.textContent = text;
  guess.disabled = true;
  again.style.display = "inline-block";
}

start();
</script>
</body>
</html>
