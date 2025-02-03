                                // 1

// let number = Number(prompt('Введите число: '));

// let sepen = Number(prompt('Введите : '));

// function construction(numbers, sepens){
    
//     if (sepens == 1){
//         return number;

//     } else {
//         return numbers * construction(numbers, sepens -1);
//     }
// }

// alert(`Число ${number} в степени ${sepen} = ${construction(number, sepen)}`)


                                // 2

// let numberOne = Number(prompt('Введите первое число: '));
// let numberTwo = Number(prompt('Введите второе число: '));

// let counter = 1;

// let divider

// function gcd(counter, numberOne, numberTwo){

//     if (counter > numberOne){
//         return divider;
        
//     } else { 
//         numberOne %counter == 0 && numberTwo %counter ==0 ? divider = counter:divider; 
//         gcd(counter + 1,numberOne, numberTwo);
        

//     } return divider;
// }

// alert(`Наибольший общий делитель = ${gcd(counter, numberOne, numberTwo)}`)

                                // 3

let number = (prompt('Введите число: '));

function largestNumber(number, _max = -Infinity) {
    const str = (number + '');
    return str.length > 1 ?
            largestNumber(str.slice(1), Math.max(str[0],_max)) :
            +Math.max(str[0],_max);
}
alert(largestNumber(number, _max = -Infinity))





//                             // 4

// let num = Number(prompt('Введите положительное число: '));

// let counter = 0;

// function dell(Number) {

//     if (Number == 0){
//         return counter <= 2 ? 'простое':'составное';

//     }else{
//         num %Number == 0 ? counter += 1: counter;
//         dell(Number -1)
//     }
//     return counter <= 2 ? 'простое':'составное';
// };

// alert(num !=0 && num !=1 ? `Ваше число ${num}`+ ` ${dell(num)}`:`Ваше число ${num} не является ни простым, ни составным числом`)

                                // 5

// let num = Number(prompt('Введите положительное число: '));

// let factors = []; 

// let divider = 2;

// function mno(Number, dividerIn){

//     if (Number == 1){
//         return 1;

//     }else{
        
//         if (Number %dividerIn != 0){
//             dividerIn += 1;
//             mno(Number, dividerIn);

//         }else{
//             factors.push(dividerIn);
//             mno(Number/dividerIn, divider);

//         }
 
//     }

//     return factors.sort(function(a,b) { return a-b; });
// }
// alert(`Множители числа ${num}: ${mno(num, divider)}`);

                            // 6

// let num = Number(prompt('Введите положительное число: '));

// let numOne = 0;
// let numTwo = 1;
// let numThree = numOne + numTwo;

// function fib(number, numOnes, numTwos, numThrees){

//     if (number <= 3){
//         return number <= 1 ? numOne:numTwo;

//     }else{ 
//         numOnes = numTwos + 0; 
//         numTwos = numThrees + 0; 
//         numThree = numOnes + numTwos; 
//         fib(number-1,numOnes, numTwos, numThree);

//     }
//     return numThree
// }

// alert(`Число Фибоначчи с порядковым номером ${num  
// } это: ${fib(num, numOne, numTwo, numThree)}`)
