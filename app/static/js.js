var images=["static/pictures/second_image.png","static/pictures/third_image.png","static/pictures/first_image.png"]

var currentIndex=0

function changeImage(){
    var imgElement=document.getElementById("image")
    imgElement.src = images[currentIndex]

    currentIndex=(currentIndex+1)% images.length
}

setInterval(changeImage, 5000)
