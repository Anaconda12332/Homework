document.getElementById('button2').addEventListener('click', function mean(){

    let text =  document.getElementById('input').value;
    let numNew = '';

    const massage = document.getElementById('massage');
    let count = 0;

    
        function num(b){  
            while(count < String(text).length){
                numNew += b%10;
                count += 1;
                num(parseInt(b/10));
            }  
        };

    num(text);
    text = document.getElementById('input').value= "";

    massage.textContent = numNew;
    
});




