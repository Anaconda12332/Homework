let list = [];
let count = 0;
let sample = /\d/g;


document.getElementById('button').addEventListener('click', function mean(){
    let text =  document.getElementById('input').value;

    text.match(sample) ? list.push(text):list;
    text = document.getElementById('input').value= "";
    
});




document.getElementById('button2').addEventListener('click', function stringFrom(){


    const massage = document.getElementById('massage');

    for (let i = 0; i < list.length; i++){
        count += Number(list[i]);
        
    }
    massage.textContent = `Среднее значение чисел: ${count / list.length} `

});



