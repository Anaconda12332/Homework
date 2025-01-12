// //                     // 1
// // let old = prompt("Укажите ваш возраст: ");
// // if (old >=0 && old <= 12){
// //     alert("Вы ребенок");

// // }else if (old >=12 && old <= 18){
// //     alert("Вы подросток");
// // }else if (old >=18 && old <= 60){
// //     alert("Вы взрослый");
// // }else if (old >=60){
// //     alert("Вы пенсионер");
// // }else{
// //     alert("Укажите реальный возраст!")
// // }

// //                     // 2
// // let num = prompt("Укажите число от 0 дл 9: ");

// // switch (num){
// //     case "0":
// //         alert(")");
// //         break;

// //     case "1":
// //         alert("!");
// //         break;

// //     case "2":
// //         alert("@");
// //         break;

// //     case "3":
// //         alert("#");
// //         break;

// //     case "4":
// //         alert("$");
// //         break;

// //     case "5":
// //         alert("%");
// //         break;

// //     case "6":
// //         alert("^");
// //         break;

// //     case "7":
// //         alert("&");
// //         break;

// //     case "8":
// //         alert("*");
// //         break;

// //     case "9":
// //         alert("(");
// //         break;
// //     default:
// //         alert("Укажите цифру в диапазоне 0-9!")

// // }
// //                     // 3

// let number = prompt("Введите трехзначное число: ");

// if (number[0] == number[1] || number[1] == number[2] || number[0] == number[2]){
//     alert("У вас есть одинаковые цифры в числе!");
// }else { 
//     alert ("У вас нет одинковых чисел!")
// }

//                         // 4

// let years = prompt ("Введите год: ");

// if (years%400==0 && years%100 !=0 || years%4 == 0 && years%100 !=0){
//     alert("Ваш год високосный!")
// } else {
//     alert("Ваш год не високосный")
// }


//                         //5
// const numb = prompt("Введите число: ");

// let numberNew = "";
// let numbOld = numb;
// while(numbOld){
//     numberNew = numberNew + numbOld % 10;
//     numbOld = Math.floor(numbOld/10);
// }
// alert(numb == numberNew ? "Ваше число является палиндромом":"Ваше число не является палиндромом") 
                          //6

// let usdUser = prompt("Введите вашу сумму долларов: ")
// let choiseUser = prompt("В какую валюты Вы хотите перевести: 1. EUR 2. UAN 3. AZN");

// switch (choiseUser){
//     case "1":
//         euro = usdUser * 0.98;
//         alert(`${euro} Евро`);
//         break;
//     case "2": 
//         uan = usdUser * 7.33;
//         alert(`${uan} Юань`);
//         break;
//     case "3":
//         azn = usdUser * 1.7;
//         alert(`${azn} Евро`)
//         break;
//     default:
//         alert("Выберите число в диапозоне от 1 до 3!")
// }

                        // 7
// let summ = prompt("Введите сумму покупки: ");
// let discount

// if (summ >= 1 && summ <= 199){
//     discount = 0;
// }else if (summ >= 200 && summ <= 299){
//     discount = 3;
// }else if (summ >= 300 && summ <= 499){
//     discount = 5;
// }else if (summ >= 500){
//     discount = 7;
// }else{
//     discount = 8;
// }

// alert(discount != 8 ? `К оплате со скидкой: ${summ - (summ*discount / 100
// )}` : "Введите корректное число!")

                        // 8

// let lenCircle = prompt ("Введите длину окружности в см.: ");
// let pSquare = prompt("Введите перемитор квадрата в см.: ");

// let dCircle = lenCircle/3.14
// let sideSquare = pSquare/4

// if (dCircle<=sideSquare){
//     alert("Ваша окружность помещается в квадрат!")
// } else {
//     alert("Ваша окружность не помещается в квадрат!")
// }


                        // 9
// function test(){
//     let ball = 0
//     let one = prompt('Сколько дней в году? 1. 336 2. 345 3. 365 ');
//     let two = prompt('Какой из этих мультфильмов кукольный? 1. "38 попугаев" 2. "Холодное сердце" 3. "Маугли" ');
//     let three = prompt('Как называли Маугли в волчьей стае? 1. Слоненок 2. Лягушонок 3. Тигренок ');
  
//     if (one == 3){
//         ball =  ball + 2;
//     }
//     if (two == 1){
//         ball =  ball + 2;
//     }
//     if (three == 2){
//         ball =  ball + 2;
//     }
    
  
        
//         // switch (one, two, three){
//         //     case "1":
//         //         ball = two == 1 ? ball + 2 : ball + 0;
//         //         break
//         //     case "2":
//         //         ball = three == 2 ? ball + 2 : ball + 0;
//         //         break
//         //     case "3":
//         //         ball = one == 3 ? ball + 2 : ball + 0;
//         //         break
//         // }
//     return ball;
// }

// alert(`Вы набрали : ${window.onload=test()} баллов!`);

                            // 10


// let day = Number(prompt("Введите день (1-31): "));
// let month = Number(prompt("Введите месяц (1-12): "));
// let year = Number(prompt("Введите год (хххх): "));


// if (month != 2 && month != 4 && month != 6 && month != 9 && month !=11){   //31 день
//     if (day <= 30){
//         day += 1;
//         alert(`${day}.${month}.${year}.`);
//     }else if (day == 31){
//         day = 1;
//         month = month + 1;
//         alert(`${day}.${month}.${year}.`);
//         } if (month == 12){
//             day = 1;
//             month = 1;
//             year += 1
//             alert(`${day}.${month}.${year}.`);
        
//     }else {
//         alert("Введите правильную дату!");
//     }

// }else if (month != 1 && month != 3 && month != 5 && month !=7  && month !=8 && month !=9 && month !=12){ //30 дней и февраль
//     if (month == 2){ // февраль 28
//         if (year%400==0 && year%100 !=0 || year%4 == 0 && year%100 !=0){ //високос
//             month = day == 29 ? 3:month;
//             day = day == 29 ? 1:day + 1;
//             alert(`${day}.${month}.${year}.`);
//         }else if (day == 28){
//             day = 1;
//             month = 3;
//             alert(`${day}.${month}.${year}.`);
//         } else { 
//             alert("Введите правильную дату!");       
//         }

//     }else if (day <= 29){
//         day = day + 1;
//         alert(`${day}.${month}.${year}.`);

    
//     }else if (day == 30){
//         day = 1;
//         month = month + 1;
//         alert(`${day}.${month}.${year}.`);
//     } else { 
//         alert("Введите правильную дату!");       
//     }

// }else {
//     alert("Введите правильную дату!")
// }


