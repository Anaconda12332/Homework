let contribution = Number(prompt('Введите величину вклада: '));

let num = Number(prompt('Введите ставку в процентах: '));


let money = contribution;
let count = 0;

for (let i = 1; contribution <= money*2; i++){
    contribution = contribution+((contribution/100)*num);
    count = i;
    //alert(contribution);
};


alert(`Вклад увеличится вдвое через ${count} лет`);