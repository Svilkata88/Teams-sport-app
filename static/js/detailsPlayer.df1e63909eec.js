let imgBox = document.getElementsByClassName('card-image');
let img = imgBox[0].getElementsByTagName('img')[0];
let inputImg = document.getElementById('playerImg');

inputImg.addEventListener('change', (e) => {
    const file = e.target.files[0];

    let imageUrl;
    imageUrl = URL.createObjectURL(file);
    img.src = imageUrl;
})