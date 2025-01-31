// Предложите имя (согласно правилам именования)
// и создайте функцию, которая будет возвращать названия дней недели по их номеру: 
// 0-Sunday, 1-Monday, 2-Tuesday, 3-Wednesday, 4-Thursday, 5-Friday, 6-Saturday.

days = prompt('Введите номер дня (от 0 до 6): ')

function week(days){
    switch(days){
        case '0':
            return 'Sunday';

        case '1':
            return 'Monday';

        case '2':
            return 'Tuesday';

        case '3':
            return 'Wednesday';

        case '4':
            return 'Thursday';

        case '5':
            return 'Friday';

        case '6':
            return 'Saturday';
        default:
            return 'Введите число от 0 до 6!';
    }
}

alert(week(days))