let list = [];

document.getElementById('button').addEventListener('click', function stringFrom(){
    let text =  document.getElementById('input').value;

    list.push(text);
})



document.getElementById('button2').addEventListener('click', function stringFrom(){

    //const text = document.getElementById('input').value;
    //const text2 = document.getElementById('input2').value;
    const massage = document.getElementById('massage');

    massage.textContent = list //text + text2 

})

// function stringFrom(){
//     alert(arguments)
// }

// let a =prompt(': ');

// stringFrom(a)