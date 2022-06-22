/*var g=document.getElementById('pop')
function pop(){
g.style.display='block';
};


var Pop=setTimeout(pop, 5000)

function close(){
var l=document.getElementById('pop')
clearTimeout(Pop);
l.style.display='none';
}*/

/*function pop(){

time=setInterval(function(){

var date=new Date()
var seconds=date.getSeconds()
var second=date.getSeconds() + 10;

g=document.getElementById('date').innerHTML=date

},1000);

}*/
/*
var V=document.getElementById('view');
g=V.value;
function count(){
a=window.localStorage.getItem('view')
if(a){
var b=a+1;
V.value=b
V.textContent=b
}
else{
window.localStorage.setItem('view',g)
var b=1;
V.value=b;
V.textContent=b
}
}
*/
function count(){
if (localStorage.clickcount) {
  localStorage.clickcount = Number(localStorage.clickcount) + 1;
} else {
  localStorage.clickcount = 1;
}
document.getElementById('view').innerHTML=localStorage.clickcount
}