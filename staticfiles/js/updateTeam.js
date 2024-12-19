let imgBox = document.getElementsByClassName('imgBox');
let img = imgBox[0].getElementsByTagName('img')[0];
let inputImg = document.querySelector('input[type="file"]');

inputImg.addEventListener('change', (e) => {
    const file = e.target.files[0];

    console.log(img)
    let imageUrl;
    imageUrl = URL.createObjectURL(file);
    img.src = imageUrl;
})