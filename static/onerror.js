

const all_img=document.querySelectorAll('img')

all_img.forEach(img=>{
img.addEventListener('error',()=>{
img.src="https://thumbs.dreamstime.com/b/no-image-available-icon-flat-vector-no-image-available-icon-flat-vector-illustration-132482953.jpg";
img.style="width:100px; height:100px;"
})

})





