const clock=document.querySelector('#clock');
const WEEKDAY = ['일', '월', '화', '수', '목', '금', '토'];
function getClock(){
    
    const date=new Date();
    const month=date.getMonth()+1
    const today=date.getDate()
    const day=WEEKDAY[date.getDay()]
    const hours=String(date.getHours()).padStart(2,'0');
    const minutes = String(date.getMinutes()).padStart(2,'0');
    const seconds = String(date.getSeconds()).padStart(2,'0');
    // clock.innerText=`${day} ${hours}:${minutes}:${seconds}`;
    clock.innerText=`${month}-${today} ${day} ${hours}:${minutes}:${seconds}`;
}
getClock()
setInterval(getClock,1000);