let list = [];
let newList = [];

document.getElementById('button').addEventListener('click', function numbers(){
    let text =  document.getElementById('input').value;

    let ss = /\d/g;

    list.push(text);
    text = document.getElementById('input').value= "";

    for (let i = 0; i < list.length; i++){
        if (list[i].match(ss)){
            newList.push(list[i])
        }
    }

});




document.getElementById('button2').addEventListener('click', function stringFrom(){


    const massage = document.getElementById('massage');
    
    massage.textContent = `Введенные числа ${newList.join(" ")}`

});



