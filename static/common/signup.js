const username=document.getElementById('username'); //사용자이름
const username_warning=document.getElementById('username_warning');
const password1=document.getElementById('password1'); //비밀번호 1
const p1_warning=document.getElementById('p1_warning');
const password2=document.getElementById('password2'); //비밀번호 2
const p2_warning=document.getElementById('p2_warning');
const submit_button=document.getElementById('submit-button');
const submitform=document.getElementById('ff')

username.addEventListener('input',function(){
 const llll=username.value.length
 if (llll <=4){
     username_warning.innerText=`아이디는 5자 이상이어야 합니다 현재${llll}자`
     username_warning.style="color:red; background-color:whihte;"
 }else{
     username_warning.innerText='😀'.repeat(17)
     username_warning.style="background-color:#3fe87f"
 }
})

password1.addEventListener('input',function(){
 const llll=password1.value.length
 if (llll <=4){
     p1_warning.innerText=`비밀번호는4자 이상이어야 합니다 현재${llll}자`
     p1_warning.style="color:red; background-color:whihte;"
 }else{
     p1_warning.innerText='😀'.repeat(17)
     p1_warning.style="background-color:#3fe87f"
 }
})

password2.addEventListener('input',function(){
 const p1=password1.value
 const p2=password2.value
 if (p1===p2 & p2.length>4){
     p2_warning.innerText='😀'.repeat(17)
     p2_warning.style="background-color:white;"

 }
 else{
     p2_warning.innerText=`비밀번호가 일치하지 않습니다`
     p2_warning.style="color:red; background-color:whihte;"
 }
});

// 중복검사
    const btn=document.getElementById('btn')


    btn.addEventListener('click',()=>{
    const user_name=username.value
    const id_check=document.getElementById('idcheck')
    const xhr= new XMLHttpRequest();
        xhr.open('GET',`./id_check?username=${user_name}`,true) //방식, 주소 ,비동기여부

        xhr.send(); //요청 전송

        xhr.onload=() =>{
            //통신 성공

            if (xhr.status==200){
                const jsondata=JSON.parse(xhr.response)
                if(jsondata.data=='good'){ //이미 존재하는 경우
                      alert('이미 존재하는 아이디입니다;;')
                }else{ //아이디 만들어도 ㄱㅊ
                    username.readOnly=true
                    id_check.innerText='SUCESS!'
                    id_check.style="background-color:#3fe87f"
                    btn.disabled=true
                }
            }else{
                console.log('실패')
            }
        }

    })


    submit_button.addEventListener('click',()=>{
        if(password1.value===password2.value & password2.value.length>=4 & username.readOnly==true){
            submitform.submit()
        }else{
            alert('something wrong')
        }

    })

