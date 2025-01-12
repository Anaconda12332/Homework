
// function myFunction1(){
//     let name = prompt("Ввидите ваше имя: ");
//     alert(`Привет ${name} !`)
// };


// window.onload= myFunction1;



                                                // 1

let names = prompt("Ввидите ваше имя: ");

alert(`Привет,${names}!`);

                                                // 2 
let yearUser = prompt("Ввидите ваш год рождения: ");
const year = 2025

alert(`Вам ${year-yearUser} лет`)

                                                // 3
let line = prompt("Ввидите сторону квадрата: ");
alert(`Периметр квадрата равен: ${line*4} `)

                                                // 4
let x = prompt("Ввидите радиус окружности: ");
alert(`Площадь окружности равна: ${(x**2) * 3.14} `)

                                                // 5
let distance = prompt("Ввидите растояние: ");
let time = prompt("Укажите желаемое время: ");

alert(`Скорость, с которой необходимо двигаться: ${distance/time} `)

                                                // 6
let dollar = prompt("Введите колличество долларов: ");
const euro = 0.98;

alert(`Ваши доллары в евро: ${dollar*euro}`)

                                                // 7
let gb = prompt("Введите количество гигабайтов: ");
const sizeFile = 0.82;

alert(`Количество помещаемых файлов: ${Math.floor(gb/sizeFile)}`)

                                                // 8

let cout = prompt("Введите сумму денег: ");
let chocolate = prompt("Введите цену одной шоколадки: ");


alert(`Можно купить ${Math.floor(cout/chocolate)
} шоколадок. Ваша сдача: ${cout%chocolate}`)

                                                // 9

let number = prompt("Введите трехзначное число: ");
if (number.length == 3){
    let numb = '';
    while(number) {
        numb = numb + number % 10; 
        number = Math.floor(number/10);
}
alert(numb);
}else{
    alert("Введите трехзначное число!")
}

                                                // 10
let numb = prompt('Введите целое число: ');
alert(numb%2 == 0 && 'Ваше число четное' ||  'Ваше число нечетное')
