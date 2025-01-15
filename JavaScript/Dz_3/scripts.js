//                     // 1

let start = Number(prompt("Укажите начало диапазона: "));
let stop = Number(prompt("Укажите конец диапазона: "));
let sum = 0;

for (let i = start; i < stop +1 ; i++ ){
    sum += i
}
alert(`Сумма всех чисел равна: ${sum}`);

//                     // 2

let num = Number(prompt("Укажите первое число: "));
let numTwo = Number(prompt("Укажите второе число: "));
let divide = 0;

for (let i = 0; i < numTwo +1 ; i++ ){
    if (num % i == 0 && numTwo % i == 0 ){
        divide = i;
    } 
}
alert(`Наибольший общий делитель: ${divide}`);

//                     // 3

let num = Number(prompt("Укажите число: "));
let divide = [];

for (let i = 1; i < num +1; i++){
   num % i == 0 ? divide.push(i) : num;
   
}
alert(`Делители числа ${num} : ${divide}`);

//                     // 4

let num = prompt("Укажите число: ");
alert(`В указанном числе ${num.length} цифр`)

//                     // 5

let spis =[]
for (let i = 1; i < 11; i++){
    let num =  Number(prompt(`Введите ${i} число: `));
    spis.push(num);
}                    

let positive = 0;
let negative = 0;
let zero = 0;
let chet = 0;
let noChet = 0;

for (let i = 0; i < spis.length; i++){
    if (spis[i] == 0){
        zero += 1;
    }else if (spis[i] > 0){
        positive += 1;
    }else if (spis[i] < 0){
        negative += 1;
    }

    if (spis[i] %2 == 0){
        chet += 1;
    }else{
        noChet += 1;
    }
}

alert(`Положительных чисел: ${positive}, Отрицательных чисел: ${negative
    }, Нулей: ${zero}, Четных чисел: ${chet
    }, Нечетных чисел: ${noChet}`)

                        // 6

let exit = 1;

while (exit){

    let numOne = Number(prompt("Введите первое число: "));
    let numTwo = Number(prompt("Введите второе число: "));
    let sign = prompt("Введите знак (+ - / *): ");

    switch(sign){
        case "+":
            alert(numOne + numTwo);
            break;
        case "-":
            alert(numOne - numTwo);
            break;
        case "/":
            alert(numOne / numTwo);
            break;
        case "*":
            alert(numOne * numTwo);
            break;
        default:
            alert("Укажите знак из предложенных!");
 
    }
    let answer = prompt("Хотите продолжить?\n (1.Да 2.Нет): ")
    answer == 1 ? exit = 1 : exit = 0;

}

//                         // 7

let num = prompt("Введите число: ");
let answer = Number(prompt("На сколько цифр сдвинуть число?: "));

for (let i = 0; i < answer; i++){
    num += num[i];
    if (answer >= num.length){
        num = num.replace(num[i], '0');

    }else{
        num = num.replace(num[i], ' ');

    }
}
alert(num.replace(/\s+/g, ''));

//                         // 8

let count = 1
let days = ["Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье"];

while (count){
    for (let i=0; i < 7; i++){
        alert(`День недели: ${days[i]}`);
        let user = prompt("Хотите продолжить? (1. Да 2. Нет) : ");

        if (user == '2'){
            count = 0;
            break;
        }  
    }
                
}       

//                         // 9

for (let i =2; i < 10; i ++){
    alert(`Таблица умножения для числа : ${i}`)
    for (let j = 2; j <10; j++){
        alert (` ${i} * ${j} = ${i * j}`);
    }
}

//                         // 10
                        
alert("Загадайте число от 0 до 100!");
let num = 100;
let n = num / 2;

let count = 1;

while (count){

    let answer = prompt(`Ваше число: > ${n}, < ${n}, == ${n} ?`);

    switch (answer){
        case '>': 
            n = n + Math.ceil(num / 4);
            num = Math.ceil(num / 2);
            break;
        case '<':
            n = n - Math.ceil(num / 4);
            num = Math.ceil(num / 2);
            break;
        case '==':
            count = 0;
            alert(`Поздравляю! Ваше число ${n}!`);
            break;
    
    };
};