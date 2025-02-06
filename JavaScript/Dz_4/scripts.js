                            // 1

// function number(numOne, numTwo) {
//     if (numOne > numTwo){
//         return 1
//     }else if (numOne < numTwo){
//         return -1
//     }else{
//         return 0
//     }
// }

// let numOne = prompt('Введите первое число: ');
// let numTwo = prompt('Введите второе число: ');

// alert(number(numOne, numTwo))

                            // 2

// function frac(num){
//     let proud = 1;
//     for (let i = 1; i <= num; i++){
//         proud *=i;
//     }
//     return proud
// }                            

// let num = prompt('Введите  число: ');
// alert(`Фракториал числа ${num} равен ${frac(num)}`)

                            // 3

// function number(number){
//     // for (let i = 0; i < number.length; i++){
//     //     nums += number[i]
//     // }
//     // return nums
// }                            
// let nums 

// let num =  [prompt('Введите  числа через пробел: ').split(" ")];
// //alert(num)

// alert(`Фракториал числа ${num} равен ${number(num)}`)





// function number(numOne, numTwo, numThree){
//    return numOne + numTwo + numThree
// }                            


// let numOne =  prompt('Введите число 1: ');
// let numTwo =  prompt('Введите число 2: ');
// let numThree =  prompt('Введите число 3: ');


// alert(number(numOne, numTwo, numThree));

                                // 4

// function number(a = 1, b = 1){
//    return a * b;
// }                            


// let width = Number(prompt('Введите ширину прямоугольника: '));
// let length = Number(prompt('Введите длинну прямоугольника: '));

                               
// let choice = width != 0 & length != 0 ? number(width, length

// ):width != 0 ? number(width):number(length);

// alert(`Периметр равен ${choice}`);

                                // 5

// function perfect(num){
//    let del = 0;
//    for (let i = 0; i < num; i++){
//     num %i == 0 ? del += i:del;

//    }
//    return del == num ?  `Число ${num} является совершенным`:`Число ${num} не является совершенным`
// }                            

// let userNum = Number(prompt('Введите число: '));

// alert(perfect(userNum));    

                            // 6

// function perfect(num, numTwo){ 
//    let perfectNum = [];

//    for (let i = num; i < numTwo; i++){ 
//         let del = 0;

//         for (let j = 0; j < i; j++){ 
//             i %j == 0 ? del += j:del;
//         }

//         del == i ? perfectNum.push(del):del = 0;

//    }
//    return perfectNum
// }                            

// let userNum = Number(prompt('Введите начало диапазона: '));
// let userNumTwo = Number(prompt('Введите конец диапазона: '));


// alert(`Совершенные числа: ${perfect(userNum, userNumTwo)}`);  

                            // 7

// function time(a, b = '00', v = '00'){ 

//     if (b == 0 && v ==0){
//         return a + ':' + '00' + ':' + '00' 
    

//     }else if (b == 0 || v ==0 ){
//         return b == 0 ?  a + ':' + '00' + ':' + v: a + ':' + b + ':' + '00'

//     }else{
//         return a + ':' + b + ':' + v 

//     }
// }                            

// let hours = prompt('Введите часы: ');
// let min = prompt('Введите минуты: ');
// let sec = prompt('Введите секунды: ');    

// alert(`Время: ${time(hours, min, sec)}`);   

                        // 8

// function time(a, b, v){ 
//     return (a * 3600) + (b * 60) + v
        
// }                            

// let hours = Number(prompt('Введите часы: '));
// let min = Number(prompt('Введите минуты: '));
// let sec = Number(prompt('Введите секунды: '));    

// alert(`Время в секундах: ${time(hours, min, sec)}`);    1 20 23 4823

                        // 9

// function time(a){ 
//     let hours = Math.floor(a / 3600); 1
//     let min = Math.floor(a% 3600 / 60);
//     let secc = a - (hours * 3600) - (min * 60);
//     return hours + ':'+ min + ':' + secc
        
// }                            

// let sec = Number(prompt('Введите секунды: '));    

// alert(`Полное время из секунд: ${time(sec)}`);                          

                        // 10

// function time(a, b){ 
//     let allSec = (b - a) * 86400

//     let hours = Math.floor(allSec / 3600); 1
//     let min = Math.floor(allSec% 3600 / 60);
//     let secc = allSec - (hours * 3600) - (min * 60);
//     return hours + ':'+ min + ':' + secc
        
// }                            

// let dataOne = Number(prompt('Введите первую дату: '));  

// let dataTwo = Number(prompt('Введите вторую дату: '));   

// alert(`Полное время между датами: ${time(dataOne, dataTwo)}`);                               

// function day(чис, мес, месс, год){
//     let del = мес == 4 || мес == 6 || мес == 9 || мес == 11 ? del = 30: год %4 == 0 || год %400 == 0 || год %100 == 0? del = 28 : del = 29 

//     for (let i = чис; i < (месс - мес); i++){

//     }
// }

// function day(год, годсс ){
//     let del = год %4 == 0 || год %400 == 0 || год %100 == 0? del = 28 : del = 29 

//     for (let i = чис; i < (месс - мес); i++){

//     }
// }

function sec(allDays){
    let allSec = allDays * 86400; 

    let hours = Math.floor(allSec / 3600); 
    let min = Math.floor(allSec% 3600 / 60);
    let secc = allSec - (hours * 3600) - (min * 60);

    return hours + ':'+ min + ':' + secc

};


function time(num, mount, year, numT, mountT, yearT){ 
   
    
    let allDays = ((yearT-year) * 365) + Math.floor(((mountT - mount) * 31)) + (numT-num);
    alert(allDays)

    if (mount != mountT){
        for (let i = mount ; i <= mountT; i++){
            i == 4 || i  == 6 ||  i == 9 || i  == 11 ? allDays -= 1 : i == 2 ? allDays -= 3: allDays -= 0;
        }
    
    };
    
    for (let i = year; i <= yearT; i++){
        i %4 == 0 || i %400 == 0 ? allDays += 1 : allDays += 0
    }
    
    alert(allDays)

    // let allSec = allDays * 86400 

    // let hours = Math.floor(allSec / 3600); 
    // let min = Math.floor(allSec% 3600 / 60);
    // let secc = allSec - (hours * 3600) - (min * 60);
    // return hours + ':'+ min + ':' + secc
    return sec(allDays)
        
}                            

let numOne = Number(prompt('Введите число первой даты: '));  
let mountOne = Number(prompt('Введите месяц первой даты: ')); 
let yearOne = Number(prompt('Введите год первой даты: ')); 

let numTwo = Number(prompt('Введите число второй даты: ')); 
let mountTwo = Number(prompt('Введите месяц второй даты: '));   
let yearTwo = Number(prompt('Введите год второй даты: '));   


alert(`Полное время между датами: ${time(
    numOne, mountOne, yearOne, numTwo, mountTwo, yearTwo)}`);   

// let allDays = ((26-25) * 360) + ((1 - 1) * 30.417) + (14-12);
// alert(allDays) 