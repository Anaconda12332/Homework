let num = Number(prompt('Введите число: '));

let a= []
if (num%2 == 0){
    for (let i = 1; i<num; i++){
        i%2 != 0 ? a.push(i):a
    }
}else{
    for (let i = 1; i<=num; i++){
        i%2 != 0 ? a.push(i):a
    }
}
alert(a.reverse())