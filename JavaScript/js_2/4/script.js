document.getElementById('button').addEventListener('click', function(){

    const text = 
    document.getElementById('xz').value;
    const textTwo = 
    document.getElementById('xz2').value;

    const message =
    document.getElementById('message');



    if (Number(text) == Number(textTwo)){
        message.textContent = `Указанные числа равны`;
    }else if (Number(text) >= Number(textTwo)){
        message.textContent = `Число ${text} больше числа ${textTwo}`;
    }else{
        message.textContent = `Число ${text} меньше числа ${textTwo}`;
    }
})