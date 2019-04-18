var b=0

function right() {
    window.alert('You are correct!');
    b++;
}
function wrong() {
    window.alert('You are incorrect');
}
function qe2() {
    document.getElementById('q1').innerHTML = 'What company owns comedy central?'
    document.getElementById('a1').innerHTML = 'FOX'
    document.getElementById('a2').innerHTML = 'Disney'
    document.getElementById('a3').innerHTML = 'Warner Brothers'
    document.getElementById('b1').setAttribute('onclick','wrong();qe3();')
    document.getElementById('b2').setAttribute('onclick','right();qe3();')
    document.getElementById('b3').setAttribute('onclick','wrong();qe3();')
}
function qe3() {
    document.getElementById('q1').innerHTML = 'Where in the human body would you find the medulla oblongata?'
    document.getElementById('a1').innerHTML = 'Head'
    document.getElementById('a2').innerHTML = 'Arm'
    document.getElementById('a3').innerHTML = 'Along the Spinal Cord'
    document.getElementById('b1').setAttribute('onclick','right();qe4();')
    document.getElementById('b2').setAttribute('onclick','wrong();qe4();')
    document.getElementById('b3').setAttribute('onclick','wrong();qe4();')
}
function qe4() {
    document.getElementById('q1').innerHTML = 'Which gas is formed when a hydrogen bomb is detonated?'
    document.getElementById('a1').innerHTML = 'Hydrogen'
    document.getElementById('a2').innerHTML = 'Radon'
    document.getElementById('a3').innerHTML = 'Helium'
    document.getElementById('b1').setAttribute('onclick','right();qe5();')
    document.getElementById('b2').setAttribute('onclick','wrong();qe5();')
    document.getElementById('b3').setAttribute('onclick','wrong();qe5();')
}
function qe5() {
    document.getElementById('q1').innerHTML = 'Aconcagua is the highest mountain in the Andes. But in which country does it lie?'
    document.getElementById('a1').innerHTML = 'Chile'
    document.getElementById('a2').innerHTML = 'Argentina'
    document.getElementById('a3').innerHTML = 'Bolivia'
    document.getElementById('b1').setAttribute('onclick','wrong();qe6();')
    document.getElementById('b2').setAttribute('onclick','right();qe6();')
    document.getElementById('b3').setAttribute('onclick','wrong();qe6();')
}
function qe6() {
    document.getElementById('title').innerHTML = 'Thank you for playing!'
    document.getElementById('q1').innerHTML = ''
    document.getElementById('buttons').innerHTML = 'You answered ' + b + ' correctly!'
}
