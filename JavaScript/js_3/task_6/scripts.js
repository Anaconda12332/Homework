let voda = 123 //Number(prompt('Укажите обьем воды: '));

let utezka = voda;
let days = 0;

for (let i = 1; utezka >= 10; i++){
    utezka = utezka-((voda/100)* 10);
    days = i;
    alert(utezka)
    alert(days)
}

alert(days);