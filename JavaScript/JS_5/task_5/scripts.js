document.getElementById('button2').addEventListener('click', function mean(){

    let text =  document.getElementById('input').value;
    let count = 0;

    const massage = document.getElementById('massage');

    function sepen(b){

        if (Number(b) %2 == 0){
            count += 1;
            sepen(Number(b)/2);
        }else{
            2 ** count == text ?  massage.textContent = `Число ${text} это 2 в ${count} степени` : massage.textContent = `Число ${text} нельзя разложить на степени 2`;

        
    
        };
    };

    sepen(text);
    text = document.getElementById('input').value= "";
    
});




