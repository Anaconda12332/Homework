document.getElementById('button').addEventListener('click', function(){

    const text = document.getElementById('xz').value;

    const message = document.getElementById('message');

    // const num = ['Ноль', 'Один', 'Два', 'Три', 'Четыре', 'Пять', 'Шесть', 'Семь', 'Восемь', 'Девять'];
    
    // // // message.textContent = num[2];
    // let a 

    // for (let i = 0; i < 10; i++) {

    //     if (i == text) {
    //         message.textContent = num[i];
    //         break;
    //     } else {
    //         message.textContent = 'aa';
    //         break;
    //     }
                
    // }

    // message.textContent = a

    // if (Number(text) >= 0 && Number(text) <= 100){
    //     message.textContent = `Число ${text} принадлежит диапазону 0 - 100`;
    // }else if (Number(text) >= 101 && Number(text) <= 200){
    //     message.textContent = `Число ${text} принадлежит диапазону 101 - 200`;
    // }else if (Number(text) >= 201 && Number(text) <= 300){
    //     message.textContent = `Число ${text} принадлежит диапазону 201 - 300`;
    
    // }else{
    //     message.textContent = `Число ${text} не принадлежит никакому диапазону`;
    // }


    switch(text){
        case '0':
            message.textContent = 'Ноль';
            break;
        case '1':
            message.textContent = 'Один';
            break;
        case '2':
            message.textContent = 'Два';
            break;
        case '3':
            message.textContent = 'Три';
            break;
        case '4':
            message.textContent = 'Четыре';
            break;
        case '5':
            message.textContent = 'Пять';
            break;
        case '6':
            message.textContent = 'Шесть';
            break;
        case '7':
            message.textContent = 'Семь';
            break;
        case '8':
            message.textContent = 'Восемь';
            break;
        case '9':
            message.textContent = 'Девять';
            break;
  
    }
})