let list = [];
let count = 0;
let sample = /\d/g;


document.getElementById('button').addEventListener('click', function numbers(){
    let text =  document.getElementById('input').value;

    list.push(text);
    text = document.getElementById('input').value= "";
    
});




document.getElementById('button2').addEventListener('click', function stringFrom(){


    const massage = document.getElementById('massage');

    for (let i = 0; i < list.length; i++){
        if (list[i].match(sample)){
            count += 1;
        }
    }
    
    massage.textContent = `Вы ввели ${count} чисел`

});



