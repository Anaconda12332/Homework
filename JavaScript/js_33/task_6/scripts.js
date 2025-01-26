let water = Number(prompt('Укажите обьем воды: '));

let days = 0;

for (let i = 1; water >= 10; i++){  //18 16.2 14.58 13.122 11.8098 10.62882 9
    water = water-((water/100)* 10);
    days = i;
}

alert(`Воды в бочке хватит на ${days} дней`);