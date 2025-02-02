const gameArea = document.querySelector('.game-area');
let snake = [{x: 10, y: 10}];
let food = {x: 200, y: 200};

let direction = 'right';
let gameInterval;

function draw(){
    gameArea.innerHTML = '';
    snake.forEach(segment => {
        const snakeElement = document.createElement('div');
        snakeElement.style.left = segment.x + 'px';
        snakeElement.style.top = segment.y + 'px';
        snakeElement.classList.add('snake');
        gameArea.appendChild(snakeElement);


    })


    const foodElement = document.createElement('div');
    foodElement.style.left = food.x + 'px';
    foodElement.style.top = food.y + 'px';
    foodElement.classList.add('food');
    gameArea.appendChild(foodElement);
}

function update(){
    const head = {x: snake[0].x, y: snake[0].y};

    if (direction === 'right') head.x += 10;
    if (direction === 'left') head.x -= 10;
    if (direction === 'up') head.y -= 10;
    if (direction === 'down') head.y += 10;

    if (head.x < 0 || head.x >= window.innerWidth || head.y < 0 || head.y >= window.innerHeight){
        clearInterval(gameInterval);
        alert('Игра окончена! Столлкновение со стеной');
        return;
    }

    snake.unshift(head);

    if (head.x === food.x && head.y === food.y){
        food.x = Math.floor(Math.random() * window.innerWidth / 10) * 10;
        food.y = Math.floor(Math.random() * window.innerHeight / 10) * 10;
 
    }else{
        snake.pop();
    }


}

function gameLoop(){
    update();
    draw();
}

document.addEventListener('keydown', (event) => {
    if (event.key === 'ArrowRight' && direction !== 'left'){
        direction = 'right';
    }else if (event.key === 'ArrowLeft' && direction !== 'right'){
        direction = 'left';
    }else if (event.key === 'ArrowUp' && direction !== 'down'){
        direction = 'up';
    }else if (event.key === 'ArrowDown' && direction !== 'up'){
        direction = 'down';
    }
});

gameInterval = setInterval(gameLoop, 100);