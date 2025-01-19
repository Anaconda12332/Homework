document.getElementById('button').addEventListener('click', function(){

    // const text = 
    // document.getElementById('xz').value;
    // const message =
    // document.getElementById('message');


    result = confirm('Продолжить?');

    if (result){
        message.textContent = 'Подтверждено'
    }else{
        message.textContent = 'Отменено'
    }
})