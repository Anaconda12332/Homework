                                                // 1
const prompt = require('prompt-sync')();

let name = prompt("Ввидите ваше имя: ");

console.log(`Привет,${name}!`);

                                                // 2 
let yearUser = prompt("Ввидите ваш год рождения: ");
const year = 2025

console.log(`Вам ${year-yearUser} лет`)

                                                // 3
let x = prompt("Ввидите сторону квадрата: ");
console.log(`Периметр квадрата равен: ${x*4} `)

                                                // 4
let x = prompt("Ввидите радиус окружности: ");
console.log(`Площадь окружности равна: ${(x**2) * 3.14} `)

                                                // 5
let distance = prompt("Ввидите растояние: ");
let time = prompt("Укажите желаемое время: ");

console.log(`Скорость, с которой необходимо двигаться: ${distance/time} `)

                                                // 6
let dollar = prompt("Введите колличество долларов: ");
const euro = 0.98;

console.log(`Ваши доллары в евро: ${dollar*euro}`)

                                                // 7
let gb = prompt("Введите количество гигабайтов: ");
const sizeFile = 0.82;

console.log(`Количество помещаемых файлов: ${Math.floor(gb/sizeFile)}`)

                                                // 8

let cout = prompt("Введите сумму денег: ");
let chocolate = prompt("Введите цену одной шоколадки: ");


console.log(`Можно купить ${Math.floor(cout/chocolate)
} шоколадок. Ваша сдача: ${cout%chocolate}`)

                                                // 9

let number = prompt("Введите трехзначное число: ");
if (number.length == 3){
    let numb = '';
    while(number) {
        numb = numb + number % 10; 
        number = Math.floor(number/10);
}
console.log(numb);
}else{
    console.log("Введите трехзначное число!")
}

                                                // 10
let numb = prompt('Введите целое число: ');
console.log(numb%2 == 0 && 'Ваше число четное' ||  'Ваше число нечетное')
