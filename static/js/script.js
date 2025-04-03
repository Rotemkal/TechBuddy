function enter_your_email() {
    const email_field = document.getElementById("email_field");
    const yes_email = document.getElementById("yes_email");
    
    if (yes_email.checked) {
        email_field.style.display = "block"; // let the user fill his email
    } else {
        email_field.style.display = "none"; // do not let the user fill his email
    }
}

function preferred_video_way(){
    const pref_video_way = document.getElementById("pref_video_way");
    const yes_video = document.getElementById("yes_video");
    console.log("preferred_video_way is called");
    if (yes_video.checked){
        pref_video_way.style.display = "block"; // let the user choose his preferred way 
    } else {
        pref_video_way.style.display = "none"; // do not let the user choose his preferred way 
    }
}