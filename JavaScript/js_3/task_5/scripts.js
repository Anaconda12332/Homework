let a= [];

for (let i = 1; i <= 20; i++){
    if (i%4 != 0){
        a.push(i)
    }
}
alert(a.sort(function b(c) {return Math.random() - 0.5}));