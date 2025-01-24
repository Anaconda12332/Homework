let num = Number(prompt('Введите число: '));

let a= [];


for (let i = 1; i<num; i++){
    num%i == 0 ? a.push(i):a
}


alert(a)