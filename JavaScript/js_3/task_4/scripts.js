let vkl = Number(prompt('Введите величину вклада: '));20

let num = Number(prompt('Введите ставку в процентах: '));5


let a
let count

for (let i = 1; a <= vkl*2; i++){
    a = vkl+((vkl/100)*num);
    count=i
    alert(count)
}


alert(count, a)